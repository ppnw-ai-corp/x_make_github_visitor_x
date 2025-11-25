"""Utility to validate visitor failure reports and their artifacts."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from jsonschema import ValidationError as _JsonSchemaValidationError
else:  # pragma: no cover - runtime fallback
    try:
        from jsonschema import ValidationError as _JsonSchemaValidationError
    except ModuleNotFoundError:
        class _JsonSchemaValidationError(Exception):
            """Raised when jsonschema dependency is unavailable."""

if TYPE_CHECKING:
    from x_make_common_x.json_contracts import validate_payload as _validate_payload
else:  # pragma: no cover - runtime fallback
    try:
        from x_make_common_x.json_contracts import validate_payload as _validate_payload
    except ModuleNotFoundError:
        from x_4357_make_common_x.json_contracts import (  # type: ignore[attr-defined]
            validate_payload as _validate_payload,
        )

validate_payload = _validate_payload

from .json_contracts import VISITOR_REPORT_SCHEMA

JSONValue = str | int | float | bool | None | dict[str, "JSONValue"] | list["JSONValue"]


@dataclass(slots=True)
class ValidationOutcome:
    """Summary of the validation pass."""

    checked: list[Path]
    errors: list[tuple[Path, str]]


def _default_reports_dir() -> Path:
    return Path(__file__).resolve().parent / "reports"


def _canonicalize_payload(payload: Mapping[str, object]) -> bytes:
    return json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")


def compute_payload_checksum(payload: Mapping[str, object]) -> str:
    """Return the canonical SHA256 checksum for a report payload."""

    normalized = dict(payload)
    normalized.pop("payload_checksum", None)
    return hashlib.sha256(_canonicalize_payload(normalized)).hexdigest()


def _hash_file_bytes(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def _load_report_payload(path: Path) -> Mapping[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        raw: object = json.load(handle)
    if not isinstance(raw, Mapping):
        message = f"report must be a JSON object: {path}"
        raise TypeError(message)
    return dict(raw)


def _read_sidecar_checksum(sidecar_path: Path) -> str:
    text = sidecar_path.read_text(encoding="utf-8").strip()
    if not text:
        raise ValueError("checksum file empty")
    digest = text.split()[0]
    if len(digest) != 64:
        raise ValueError("checksum entry malformed")
    return digest


def _artifact_path(value: object, artifact_root: Path | None) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        return None
    candidate = Path(value)
    if not candidate.is_absolute() and artifact_root is not None:
        return (artifact_root / candidate).resolve()
    return candidate


def _validate_artifact_ref(
    *,
    ref: object,
    field: str,
    artifact_root: Path | None,
) -> list[str]:
    if ref is None:
        return []
    if not isinstance(ref, Mapping):
        return [f"{field} must be an object"]
    path_value = ref.get("path")
    artifact_path = _artifact_path(path_value, artifact_root)
    if artifact_path is None:
        return [f"{field} missing path"]
    errors: list[str] = []
    if not artifact_path.exists():
        errors.append(f"{field} path missing: {artifact_path}")
        return errors
    expected_bytes = ref.get("bytes")
    expected_sha = ref.get("sha256")
    data = artifact_path.read_bytes()
    actual_bytes = len(data)
    actual_sha = hashlib.sha256(data).hexdigest()
    if isinstance(expected_bytes, int) and expected_bytes >= 0:
        if expected_bytes != actual_bytes:
            errors.append(
                f"{field} byte length mismatch: expected {expected_bytes}, got {actual_bytes}"
            )
    if isinstance(expected_sha, str):
        if expected_sha.lower() != actual_sha:
            errors.append(
                f"{field} sha256 mismatch: expected {expected_sha}, got {actual_sha}"
            )
    return errors


def validate_report_path(path: Path) -> list[str]:
    """Validate a single visitor report and return a list of issues."""

    errors: list[str] = []
    try:
        payload = _load_report_payload(path)
    except (OSError, ValueError, TypeError) as exc:
        return [f"failed to load report: {exc}"]

    try:
        validate_payload(payload, VISITOR_REPORT_SCHEMA)
    except _JsonSchemaValidationError as exc:
        return [f"schema validation failed: {exc.message}"]

    checksum_value = payload.get("payload_checksum")
    if not isinstance(checksum_value, str):
        errors.append("payload_checksum missing or invalid")
    else:
        expected_checksum = compute_payload_checksum(payload)
        if checksum_value != expected_checksum:
            errors.append(
                "payload_checksum mismatch:"
                f" expected {expected_checksum}, got {checksum_value}"
            )

    sidecar_path = path.with_suffix(path.suffix + ".sha256")
    try:
        recorded_digest = _read_sidecar_checksum(sidecar_path)
    except (OSError, ValueError) as exc:
        errors.append(f"checksum sidecar invalid: {exc}")
        recorded_digest = None
    actual_digest = _hash_file_bytes(path)
    if recorded_digest and recorded_digest != actual_digest:
        errors.append(
            "checksum sidecar mismatch:"
            f" expected {recorded_digest}, got {actual_digest}"
        )

    artifact_root_value = payload.get("artifact_root")
    artifact_root = None
    if isinstance(artifact_root_value, str) and artifact_root_value:
        artifact_root = Path(artifact_root_value)
        if not artifact_root.exists():
            errors.append(f"artifact_root missing: {artifact_root}")

    failures_obj = payload.get("failures")
    if isinstance(failures_obj, Sequence):
        for index, entry in enumerate(failures_obj, 1):
            if not isinstance(entry, Mapping):
                errors.append(f"failure #{index} is not an object")
                continue
            errors.extend(
                _validate_artifact_ref(
                    ref=entry.get("stdout_artifact"),
                    field=f"failure #{index} stdout_artifact",
                    artifact_root=artifact_root,
                )
            )
            errors.extend(
                _validate_artifact_ref(
                    ref=entry.get("stderr_artifact"),
                    field=f"failure #{index} stderr_artifact",
                    artifact_root=artifact_root,
                )
            )
    return errors


def validate_reports_dir(reports_dir: Path, *, limit: int | None = None) -> ValidationOutcome:
    reports_path = reports_dir.resolve()
    if not reports_path.exists():
        message = f"reports directory does not exist: {reports_path}"
        raise FileNotFoundError(message)
    json_files = sorted(reports_path.glob("visitor_failures_*.json"))
    if limit is not None and limit >= 0:
        json_files = json_files[:limit]
    checked: list[Path] = []
    errors: list[tuple[Path, str]] = []
    for report_path in json_files:
        checked.append(report_path)
        for error in validate_report_path(report_path):
            errors.append((report_path, error))
    return ValidationOutcome(checked=checked, errors=errors)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x_make_github_visitor_validate_reports",
        description=(
            "Validate visitor failure reports for schema compliance,"
            " checksum integrity, and artifact availability."
        ),
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=_default_reports_dir(),
        help="Path containing visitor_failures_*.json files (defaults to package reports dir).",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Validate at most N reports.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        outcome = validate_reports_dir(args.reports_dir, limit=args.limit)
    except FileNotFoundError as exc:
        parser.error(str(exc))
        return 2

    print(f"checked={len(outcome.checked)} errors={len(outcome.errors)}")
    if outcome.errors:
        for path, message in outcome.errors:
            print(f"ERROR {path}: {message}")
        return 1
    return 0


__all__ = [
    "ValidationOutcome",
    "compute_payload_checksum",
    "main",
    "validate_report_path",
    "validate_reports_dir",
]


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
