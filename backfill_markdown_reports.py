from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import cast

from .runner import JSONValue, render_markdown_todo_report


@dataclass(slots=True)
class BackfillOutcome:
    created: list[Path]
    skipped: list[Path]
    errors: list[tuple[Path, str]]


def _default_reports_dir() -> Path:
    return Path(__file__).resolve().parent / "reports"


def _atomic_write_text(path: Path, content: str) -> None:
    tmp = path.with_name(path.name + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        handle.write(content)
        handle.flush()
    tmp.replace(path)


def _load_json_payload(path: Path) -> Mapping[str, object]:
    with path.open("r", encoding="utf-8") as handle:
        raw: object = json.load(handle)
    if not isinstance(raw, Mapping):
        message = f"report must be a JSON object: {path}"
        raise TypeError(message)
    normalized: dict[str, object] = {}
    for key, value in raw.items():
        normalized[str(key)] = value
    return normalized


def _parse_generated_at(value: object, *, fallback_timestamp: float) -> datetime:
    if isinstance(value, str):
        text = value.strip()
        if text:
            candidate = text[:-1] + "+00:00" if text.endswith("Z") else text
            try:
                parsed = datetime.fromisoformat(candidate)
            except ValueError:
                parsed = None
            if parsed is not None:
                if parsed.tzinfo is None:
                    parsed = parsed.replace(tzinfo=UTC)
                return parsed.astimezone(UTC)
    return datetime.fromtimestamp(fallback_timestamp, tz=UTC)


def _coerce_summary(value: object) -> Mapping[str, object]:
    if isinstance(value, Mapping):
        return cast("Mapping[str, object]", value)
    return {}


def _coerce_failures(value: object) -> list[Mapping[str, JSONValue]]:
    if not isinstance(value, Sequence) or isinstance(value, (str, bytes, bytearray)):
        return []
    failures: list[Mapping[str, JSONValue]] = []
    for entry in value:
        if isinstance(entry, Mapping):
            normalized = {str(key): cast("JSONValue", val) for key, val in entry.items()}
            failures.append(normalized)
    return failures


def backfill_markdown_reports(
    reports_dir: Path,
    *,
    force: bool = False,
    limit: int | None = None,
) -> BackfillOutcome:
    """Generate Markdown TODO reports for JSON visitor outputs."""

    reports_path = reports_dir.resolve()
    if not reports_path.exists():
        message = f"reports directory does not exist: {reports_path}"
        raise FileNotFoundError(message)

    json_files = sorted(reports_path.glob("visitor_failures_*.json"))
    if limit is not None and limit >= 0:
        json_files = json_files[:limit]

    created: list[Path] = []
    skipped: list[Path] = []
    errors: list[tuple[Path, str]] = []

    for json_path in json_files:
        markdown_path = json_path.with_suffix(".md")
        if markdown_path.exists() and not force:
            skipped.append(markdown_path)
            continue
        try:
            payload = _load_json_payload(json_path)
            summary = _coerce_summary(payload.get("summary"))
            failures = _coerce_failures(payload.get("failures"))
            stat = json_path.stat()
            generated_at = _parse_generated_at(
                payload.get("generated_at"), fallback_timestamp=stat.st_mtime
            )
            workspace_root = payload.get("workspace_root") or reports_path.parent
            markdown_text = render_markdown_todo_report(
                workspace_root=workspace_root,
                generated_at=generated_at,
                summary=summary,
                failures=failures,
            )
            _atomic_write_text(markdown_path, markdown_text)
        except Exception as exc:  # noqa: BLE001 - defensive for report parsing
            errors.append((json_path, str(exc)))
        else:
            created.append(markdown_path)

    return BackfillOutcome(created=created, skipped=skipped, errors=errors)


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x_make_github_visitor_backfill",
        description="Backfill Markdown TODO reports from existing visitor JSON outputs.",
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=_default_reports_dir(),
        help="Path containing visitor_failures_*.json files (defaults to package reports dir).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Regenerate Markdown even when a .md file already exists.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Process at most N JSON reports (useful for spot checks).",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    try:
        outcome = backfill_markdown_reports(
            args.reports_dir,
            force=bool(getattr(args, "force", False)),
            limit=getattr(args, "limit", None),
        )
    except FileNotFoundError as exc:
        parser.error(str(exc))
        return 2

    summary_line = (
        f"created={len(outcome.created)} skipped={len(outcome.skipped)} "
        f"errors={len(outcome.errors)}"
    )
    print(summary_line)
    if outcome.errors:
        for path, message in outcome.errors:
            print(f"ERROR {path}: {message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
