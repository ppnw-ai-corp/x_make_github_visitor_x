from __future__ import annotations

import argparse
import hashlib
import importlib
import json
import os
import platform
import shutil
import subprocess
import sys
import time
import uuid
from collections import Counter
from collections.abc import Callable, Iterable, Mapping, MutableMapping, Sequence
from contextlib import suppress
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from subprocess import CompletedProcess
from typing import TYPE_CHECKING, cast

from jsonschema import ValidationError as _JsonSchemaValidationError

from .json_contracts import (
    INPUT_SCHEMA,
    OUTPUT_SCHEMA,
    VISITOR_REPORT_SCHEMA,
    VISITOR_REPORT_SCHEMA_VERSION,
)

JSONSchemaValidationError = cast("type[Exception]", _JsonSchemaValidationError)

_WORKSPACE_ROOT = Path(__file__).resolve().parent.parent.parent
_workspace_root_str = str(_WORKSPACE_ROOT)

try:
    from x_make_github_visitor_x.inspection_flow import VisitorRunResult
except ModuleNotFoundError:  # pragma: no cover - fallback for script execution
    if _workspace_root_str not in sys.path:
        sys.path.insert(0, _workspace_root_str)
    from x_make_github_visitor_x.inspection_flow import VisitorRunResult

if _workspace_root_str not in sys.path:
    sys.path.insert(0, _workspace_root_str)

if TYPE_CHECKING:  # Static analyzers see the local package for precise types
    from x_make_common_x.json_contracts import validate_payload
    from x_make_common_x.stage_progress import RepoProgressReporter
    from x_make_common_x.x_logging_utils_x import get_logger
else:  # Prefer local workspace package, fall back to PyPI distribution
    try:
        from x_make_common_x import get_logger, validate_payload
    except ModuleNotFoundError:  # pragma: no cover - only hit when using PyPI build
        fallback_module = importlib.import_module("x_4357_make_common_x")
        get_logger = cast(
            "Callable[[str], object]",
            fallback_module.get_logger,
        )
        validate_payload = cast(
            "Callable[..., object]",
            fallback_module.validate_payload,
        )

JSONPrimitive = str | int | float | bool | None
JSONValue = JSONPrimitive | dict[str, "JSONValue"] | list["JSONValue"]

_LOGGER = get_logger("x_make_github_visitor")

VISITOR_CONTEXT_RELATIVE_PATH = (
    Path("artifacts") / "make_github_visitor" / "visitor_failures_context.json"
)
_REPO_TABLE_LIMIT = 5
_DEFAULT_NEXT_ACTIONS = (
    "1. Freeze unmanaged visitor artifacts in favor of DocumentFactory.\n"
    "2. Render `visitor_failure_digest_0_20_14` (or make_all digest) from the"
    " latest context.\n3. Run Doc Guard / Politia to confirm no unmanaged"
    " Markdown remains."
)


def _info(*args: object) -> None:
    msg = " ".join(str(a) for a in args)
    with suppress(Exception):
        _LOGGER.info("%s", msg)


def _string_field(value: object, fallback: str) -> str:
    if isinstance(value, str):
        stripped = value.strip()
        if stripped:
            return stripped
    if isinstance(value, Path):
        text = str(value).strip()
        if text:
            return text
    return fallback


def _summarize_failures_for_digest(
    failures: Sequence[Mapping[str, JSONValue]],
) -> tuple[dict[str, Counter[str]], Counter[str]]:
    repo_counters: dict[str, Counter[str]] = {}
    tool_counts: Counter[str] = Counter()
    for entry in failures:
        repo = _string_field(entry.get("repo"), "<unknown>")
        tool = _string_field(entry.get("tool"), "<unknown>")
        repo_counter = repo_counters.setdefault(repo, Counter())
        repo_counter[tool] += 1
        tool_counts[tool] += 1
    return repo_counters, tool_counts


def _format_repo_table(repo_counters: Mapping[str, Counter[str]]) -> str:
    if not repo_counters:
        return (
            "| Repo | Failures | Tool mix |\n"
            "| --- | --- | --- |\n"
            "| _None_ | 0 | — |"
        )
    sorted_entries = sorted(
        repo_counters.items(),
        key=lambda item: (-sum(item[1].values()), item[0].casefold()),
    )[:_REPO_TABLE_LIMIT]
    lines = ["| Repo | Failures | Tool mix |", "| --- | --- | --- |"]
    for repo, counter in sorted_entries:
        total = sum(counter.values())
        tool_mix = ", ".join(
            f"{tool} x{count}"
            for tool, count in sorted(
                counter.items(),
                key=lambda pair: (-pair[1], pair[0].casefold()),
            )
        )
        lines.append(f"| `{repo}` | {total} | {tool_mix or '—'} |")
    return "\n".join(lines)


def _format_tool_table(tool_counts: Counter[str]) -> str:
    if not tool_counts:
        return "| Tool | Failures |\n| --- | --- |\n| _None_ | 0 |"
    lines = ["| Tool | Failures |", "| --- | --- |"]
    for tool, count in sorted(
        tool_counts.items(),
        key=lambda item: (-item[1], item[0].casefold()),
    ):
        lines.append(f"| `{tool}` | {count} |")
    return "\n".join(lines)


def _relativize_path(path: Path | None, root: Path) -> str | None:
    if path is None:
        return None
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def _doc_guard_summary(
    straggler: Path | None,
    root: Path,
) -> tuple[str, str, int]:
    if straggler is None:
        return (
            "Doc Guard clear — Markdown report generation suppressed.",
            "(none detected)",
            0,
        )
    display = _relativize_path(straggler, root) or str(straggler)
    return (f"Doc Guard blocked by `{display}`.", display, 1)


def _build_summary_block(  # noqa: PLR0913 - summary metadata requires explicit fields
    *,
    generated_at: datetime,
    issue_count: int,
    repo_count: int,
    doc_guard_status: str,
    straggler_count: int,
    artifact_root: str,
) -> str:
    lines = [
        (
            "- Latest visitor run captured "
            f"**{issue_count}** issue(s) across **{repo_count}** repo(s) "
            f"({generated_at.isoformat()})."
        ),
        f"- Doc Guard status: **{doc_guard_status}**",
        (
            "- JSON dossiers retained: "
            f"**{issue_count}**; Markdown stragglers: **{straggler_count}**."
        ),
        f"- Artifact root: `{artifact_root}`.",
    ]
    return "\n".join(lines)


"""Visitor to run ruff/black/mypy/pyright on immediate child git clones.

Hidden and cache directories (for example: .mypy_cache, .ruff_cache,
__pycache__, .pyright) are ignored when discovering child repositories.
The visitor caches tool outputs for unchanged repositories and emits a
timestamped JSON report summarising any failures for downstream automation.
Failures are captured for reporting without raising so orchestrators can
continue processing while surfacing diagnostics.
"""


COMMON_CACHE_NAMES = {
    ".mypy_cache",
    ".ruff_cache",
    "__pycache__",
    ".pyright",
    ".tool_cache",
}

GENERATED_BUILD_DIR_PREFIXES: tuple[str, ...] = ("_build_temp",)
VENV_DIR_NAMES: frozenset[str] = frozenset({"venv", ".venv"})

TOOL_MODULE_MAP = {
    "ruff_fix": "ruff",
    "ruff_check": "ruff",
    "black": "black",
    "mypy": "mypy",
    "pyright": "pyright",
}

SCHEMA_VERSION = "x_make_github_visitor_x.run/1.0"

ToolResult = dict[str, object]
RepoReport = dict[str, object]
FAILURE_PREVIEW_LIMIT = 5
OUTPUT_PREVIEW_LIMIT = 5
VISIBLE_DIR_PREVIEW_LIMIT = 10
DEFAULT_TIMEOUT_SECONDS = 300
REQUIRED_PACKAGES: tuple[str, ...] = (
    "ruff",
    "black",
    "mypy",
    "pyright",
)
SUMMARY_MESSAGE_LIMIT = 240
REPORTS_DIR_NAME = "reports"
REPORT_ARTIFACTS_DIR_NAME = "artifacts"

_DIR_SCAN_YIELD_INTERVAL = 4
_FILE_SCAN_YIELD_INTERVAL = 8
_REPO_ITERATION_YIELD_INTERVAL = 1
_TOOL_ITERATION_YIELD_INTERVAL = 1


def _cooperative_yield() -> None:
    """Hint to the scheduler so GUI threads can process events."""

    time.sleep(0.001)


def _yield_periodically(counter: int, *, interval: int) -> None:
    if interval <= 0:
        return
    if counter % interval == 0:
        _cooperative_yield()


def _normalize_repo_name(value: str) -> str:
    stripped = value.strip()
    if not stripped:
        return ""
    candidate = Path(stripped)
    name = candidate.name or stripped
    return name.strip()


def _normalize_rel_path(value: str) -> str:
    normalized = value.replace("\\", "/").strip()
    while normalized.startswith("/"):
        normalized = normalized[1:]
    return normalized


def _is_virtual_env_part(name: str) -> bool:
    return name.lower() in VENV_DIR_NAMES


@dataclass(frozen=True)
class ToolConfig:
    name: str
    command: list[str]
    skip_if_no_python: bool


@dataclass
class ToolOutcome:
    result: ToolResult
    failure_message: str | None = None
    failure_detail: dict[str, object] | None = None


@dataclass
class RepoProcessingResult:
    relative_name: str
    report: RepoReport
    failure_messages: list[str]
    failure_details: list[dict[str, object]]


@dataclass(frozen=True)
class RepoContext:
    path: Path
    rel_path: str
    repo_hash: str
    has_python: bool
    files: tuple[str, ...]


@dataclass(frozen=True, slots=True)
class _ToolEventPayload:
    repo: RepoContext
    config: ToolConfig
    module_name: str
    status: str
    result: Mapping[str, object]
    summary: str | None = None
    failures: Sequence[Mapping[str, str]] | None = None


@dataclass(frozen=True)
class _ArtifactRequest:
    directory: Path
    index: int
    repo: str
    tool: str
    kind: str


def _coerce_exit_code(value: object) -> int | None:
    if value is None:
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, str):
        try:
            return int(value)
        except ValueError:
            return None
    return None


def _increment_counter(
    mapping: MutableMapping[str, object],
    key: str,
    delta: int = 1,
) -> None:
    current = mapping.get(key, 0)
    if isinstance(current, int):
        mapping[key] = current + delta
    else:
        mapping[key] = delta


def _preview_lines(lines: Sequence[str], limit: int) -> str:
    preview = "\n".join(lines[:limit])
    if len(lines) > limit:
        preview += "\n…"
    return preview


def _json_ready(value: object) -> JSONValue:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value
    if isinstance(value, Mapping):
        typed_mapping = cast("Mapping[object, object]", value)
        return {str(key): _json_ready(val) for key, val in typed_mapping.items()}
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        typed_sequence = cast("Sequence[object]", value)
        return [_json_ready(entry) for entry in typed_sequence]
    return str(value)


def _dedupe_preserving_order(values: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for value in values:
        if value not in seen:
            seen.add(value)
            unique.append(value)
    return unique


def _generate_run_id() -> str:
    """Return a short unique run identifier for streaming envelopes."""
    dt_part = datetime.now(UTC).strftime("%Y%m%d%H%M%S")
    rand_part = uuid.uuid4().hex[:8]
    return f"run_{dt_part}_{rand_part}"


def _is_generated_build_dir(name: str) -> bool:
    return any(name.startswith(prefix) for prefix in GENERATED_BUILD_DIR_PREFIXES)


def _iterable_to_str_list(value: object) -> list[str]:
    if isinstance(value, Iterable) and not isinstance(value, (str, bytes, bytearray)):
        return [str(entry) for entry in value]
    return []


def _validation_error_details(exc: Exception) -> dict[str, object]:
    message_obj: object = getattr(exc, "message", None)
    message = str(message_obj) if message_obj is not None else str(exc)
    path_attr: object = getattr(exc, "path", ())
    schema_path_attr: object = getattr(exc, "schema_path", ())
    return {
        "error": message,
        "path": _iterable_to_str_list(path_attr),
        "schema_path": _iterable_to_str_list(schema_path_attr),
    }


class x_cls_make_github_visitor_x:  # noqa: N801 - legacy naming retained for compatibility
    def __init__(  # noqa: PLR0913 - runtime configuration requires these parameters
        self,
        root_dir: str | Path,
        *,
        output_filename: str = "repos_index.json",
        ctx: object | None = None,
        enable_cache: bool = True,
        allowed_repositories: Sequence[str] | None = None,
        file_allowlist: Mapping[str, Sequence[str]] | None = None,
        progress_writer: RepoProgressReporter | None = None,
        stream_events: bool | None = None,
    ) -> None:
        """Initialize visitor.

        root_dir: path to a workspace that contains immediate child git clones.
        output_filename: unused for package-local index storage but kept for
        backwards compatibility.
        enable_cache: whether to reuse cached tool outputs when repositories are
        unchanged between runs.
        """
        self.root = Path(root_dir)
        if not self.root.exists() or not self.root.is_dir():
            msg = f"workspace root does not exist: {self.root}"
            raise AssertionError(msg)

        # Track whether the workspace root is itself a git repository. The
        # control center operates on immediate child clones, so we tolerate a
        # git root and simply avoid treating it as an inspected repository.
        self._root_is_git_repo = (self.root / ".git").is_dir()
        if self._root_is_git_repo:
            _info(
                (
                    "workspace root is a git repository; proceeding "
                    "with child clone discovery"
                ),
                str(self.root),
            )

        self.output_filename = output_filename
        self._tool_reports: dict[str, RepoReport] = {}
        self._ctx = ctx
        self.enable_cache = enable_cache
        self._last_run_failures: bool = False
        self._failure_messages: list[str] = []
        self._failure_details: list[dict[str, object]] = []
        self._tool_versions: dict[str, str] = {}
        self._runtime_snapshot: dict[str, object] = {
            "workspace_root": str(self.root),
        }
        self._last_report_path: Path | None = None
        self._last_markdown_report_path: Path | None = None
        self._last_context_path: Path | None = None
        self._last_run_result: VisitorRunResult | None = None
        self.progress_writer: RepoProgressReporter | None = progress_writer

        # package root (the folder containing this module). Reports live here so
        # they remain alongside the visitor package rather than the workspace
        # root.
        self.package_root = Path(__file__).resolve().parent
        self._reports_dir = self.package_root / REPORTS_DIR_NAME
        self._report_artifacts_dir = self._reports_dir / REPORT_ARTIFACTS_DIR_NAME

        self.cache_dir = self.package_root / ".tool_cache"
        if self.enable_cache:
            self.cache_dir.mkdir(exist_ok=True)

        normalized_allowed = {
            normalized
            for repo in (allowed_repositories or ())
            for normalized in (_normalize_repo_name(repo),)
            if normalized
        }
        self._allowed_repositories: frozenset[str] = frozenset(normalized_allowed)

        file_allowance: dict[str, frozenset[str]] = {}
        if file_allowlist:
            for repo_name, rel_paths in file_allowlist.items():
                normalized_repo = _normalize_repo_name(repo_name)
                if not normalized_repo:
                    continue
                normalized_files = {
                    normalized
                    for entry in rel_paths
                    for normalized in (_normalize_rel_path(entry),)
                    if normalized
                }
                if normalized_files:
                    file_allowance[normalized_repo] = frozenset(normalized_files)
        self._file_allowlist: dict[str, frozenset[str]] = file_allowance

        # ------------- Streaming event state (experimental) -------------
        if stream_events is None:
            env_value = os.environ.get("VISITOR_STREAMING", "").strip().lower()
            stream_events = env_value in {"1", "true", "yes", "on"}
        self._stream_events = bool(stream_events)
        self._event_run_id: str | None = (
            _generate_run_id() if self._stream_events else None
        )
        # Events live under reports/events/visitor_events.ndjson so they remain
        # co-located with the existing JSON reports.
        self._event_dir = self.package_root / REPORTS_DIR_NAME / "events"
        self._event_stream_path = self._event_dir / "visitor_events.ndjson"
        if self._stream_events:
            with suppress(OSError):
                self._event_dir.mkdir(parents=True, exist_ok=True)

    # ------------------------------------------------------------------
    # Streaming helpers
    # ------------------------------------------------------------------
    def _emit_stream_event(self, envelope: Mapping[str, object]) -> None:
        if not self._stream_events or self._event_run_id is None:
            return
        base: dict[str, object] = {
            "schema": "x_make_github_visitor_x.event/1.0",
            "emitted_at": datetime.now(UTC).isoformat(),
            "run_id": self._event_run_id,
        }
        base.update(dict(envelope))
        line = json.dumps(base, ensure_ascii=False)
        try:
            with self._event_stream_path.open("a", encoding="utf-8") as handle:
                handle.write(line + "\n")
                handle.flush()
                with suppress(OSError):
                    os.fsync(handle.fileno())
        except OSError:
            # Hard degrade: disable further streaming attempts this run
            self._stream_events = False

    def _emit_repo_event(
        self,
        *,
        repo: RepoContext,
        phase: str,
        status: str | None = None,
        summary: Mapping[str, object] | None = None,
        messages: Sequence[str] | None = None,
    ) -> None:
        if not self._stream_events:
            return
        payload: dict[str, object] = {
            "event": "repo",
            "phase": phase,
            "repo": repo.rel_path,
        }
        if status is not None:
            payload["status"] = status
        if summary is not None:
            payload["summary"] = dict(summary)
        if messages:
            payload["messages"] = list(messages)
        self._emit_stream_event(payload)

    def _emit_tool_stream_event(
        self,
        event: _ToolEventPayload,
        *,
        failures: Sequence[Mapping[str, object]] | None = None,
    ) -> None:
        if not self._stream_events:
            return
        payload: dict[str, object] = {
            "event": "tool",
            "repo": event.repo.rel_path,
            "tool": event.config.name,
            "status": event.status,
        }
        if event.summary:
            payload["summary"] = event.summary
        active_failures = failures or event.failures
        if active_failures:
            payload["failures"] = [dict(f) for f in active_failures]
        result = event.result
        if result is not None:
            # Include lightweight subset to limit file growth
            subset: dict[str, object] = {}
            for key in (
                "exit",
                "cached",
                "skipped",
                "timed_out",
                "duration_seconds",
                "repo_hash",
                "tool_version",
            ):
                val = result.get(key)
                if val is not None:
                    subset[key] = val
            payload["result"] = subset
        self._emit_stream_event(payload)

    def _emit_run_event(
        self,
        *,
        phase: str,
        repositories: Sequence[str] | None = None,
        summary: Mapping[str, object] | None = None,
    ) -> None:
        if not self._stream_events:
            return
        payload: dict[str, object] = {
            "event": "run",
            "phase": phase,
        }
        if repositories is not None:
            payload["repositories"] = list(repositories)
        if summary is not None:
            payload["summary"] = dict(summary)
        self._emit_stream_event(payload)

    @staticmethod
    def _detect_fast_paths() -> dict[str, bool]:
        def enabled(name: str) -> bool:
            val = os.environ.get(name, "").strip().lower()
            return val in {"1", "true", "yes", "on"}

        return {
            "skip_content_hash": enabled("VISITOR_SKIP_CONTENT_HASH"),
            "skip_tools": enabled("VISITOR_SKIP_TOOLS"),
            "quick_mode": enabled("VISITOR_QUICK_MODE"),
        }

    def _child_dirs(self) -> list[Path]:
        """Return immediate child directories excluding hidden and cache dirs.

        Exclude names starting with '.' or '__' and common cache names to avoid
        treating tool caches as repositories.
        """
        out: list[Path] = []
        for index, p in enumerate(self.root.iterdir(), 1):
            _yield_periodically(index, interval=_DIR_SCAN_YIELD_INTERVAL)
            if not p.is_dir():
                continue
            name = p.name
            if _is_virtual_env_part(name):
                continue
            if name.startswith((".", "__")):
                # hidden or dunder directories (including caches)
                continue
            if name in COMMON_CACHE_NAMES:
                continue
            normalized_name = _normalize_repo_name(name)
            if (
                self._allowed_repositories
                and normalized_name not in self._allowed_repositories
            ):
                continue
            # Only include directories that look like git clones (contain .git)
            if not (p / ".git").exists():
                # skip non-repo helper folders
                continue
            out.append(p)
        return sorted(out)

    def set_progress_writer(self, writer: RepoProgressReporter | None) -> None:
        self.progress_writer = writer

    def _atomic_write_json(self, path: Path, data: object) -> None:
        tmp = path.with_name(path.name + ".tmp")
        with tmp.open("w", encoding="utf-8") as fh:
            json.dump(data, fh, indent=4, sort_keys=True)
            fh.flush()
            with suppress(OSError):
                os.fsync(fh.fileno())
        tmp.replace(path)

    def _context_output_path(self) -> Path:
        return (self.root / VISITOR_CONTEXT_RELATIVE_PATH).resolve()

    def _artifact_run_dir(self, base_name: str) -> Path:
        artifact_dir = self._report_artifacts_dir / base_name
        artifact_dir.mkdir(parents=True, exist_ok=True)
        return artifact_dir

    def _find_markdown_straggler(self) -> Path | None:
        try:
            candidates = list(self._reports_dir.glob("visitor_failures_*.md"))
        except OSError:
            return None
        newest_path: Path | None = None
        newest_mtime = float("-inf")
        for candidate in candidates:
            try:
                stat = candidate.stat()
            except OSError:
                continue
            if stat.st_mtime >= newest_mtime:
                newest_mtime = stat.st_mtime
                newest_path = candidate
        return newest_path

    @staticmethod
    def _safe_slug(value: str, fallback: str) -> str:
        if not value:
            return fallback
        normalized = "".join(
            ch.lower() if ch.isalnum() else "-" for ch in value.strip()
        )
        parts = [part for part in normalized.split("-") if part]
        slug = "-".join(parts)
        return slug[:48] or fallback

    def _persist_failure_artifact(
        self,
        *,
        request: _ArtifactRequest,
        content: str,
    ) -> dict[str, JSONValue] | None:
        text = content if isinstance(content, str) else str(content)
        if not text:
            return None
        repo_slug = self._safe_slug(request.repo, "repo")
        tool_slug = self._safe_slug(request.tool, "tool")
        filename = f"{request.index:04d}_{repo_slug}_{tool_slug}_{request.kind}.log"
        artifact_path = request.directory / filename
        artifact_path.parent.mkdir(parents=True, exist_ok=True)
        encoded = text.encode("utf-8")
        with artifact_path.open("wb") as handle:
            handle.write(encoded)
            handle.flush()
            with suppress(OSError):
                os.fsync(handle.fileno())
        digest = hashlib.sha256(encoded).hexdigest()
        return {
            "path": str(artifact_path),
            "sha256": digest,
            "bytes": len(encoded),
        }

    def _sanitize_failure_detail(
        self,
        detail: Mapping[str, object],
    ) -> dict[str, JSONValue]:
        sanitized: dict[str, JSONValue] = {}
        for key, value in detail.items():
            if key in {"stdout", "stderr"}:
                continue
            sanitized[str(key)] = _json_ready(value)
        return sanitized

    @staticmethod
    def _hash_report_payload(payload: Mapping[str, object]) -> str:
        canonical = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
            "utf-8",
        )
        return hashlib.sha256(canonical).hexdigest()

    def _validate_report_payload(self, payload: Mapping[str, object]) -> None:
        try:
            validate_payload(payload, VISITOR_REPORT_SCHEMA)
        except JSONSchemaValidationError as exc:  # pragma: no cover - defensive
            details = _validation_error_details(exc)
            message = details.get("error", "report failed schema validation")
            raise AssertionError(message) from exc

    def _write_checksum_sidecar(self, report_path: Path) -> None:
        digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
        checksum_path = report_path.with_suffix(report_path.suffix + ".sha256")
        with checksum_path.open("w", encoding="utf-8") as handle:
            handle.write(f"{digest}  {report_path.name}\n")

    @staticmethod
    def _ensure_text(value: object) -> str:
        def decode_bytes(raw: bytes) -> str:
            try:
                return raw.decode("utf-8")
            except UnicodeDecodeError:  # pragma: no cover - diagnostic fallback
                return raw.decode("utf-8", "replace")

        if isinstance(value, str):
            return value

        if isinstance(value, (bytes, bytearray)):
            return decode_bytes(bytes(value))

        if isinstance(value, memoryview):
            return decode_bytes(value.tobytes())

        if value is None:
            return ""
        return str(value)

    def _cleanup_generated_build_dirs(self, repo_path: Path) -> None:
        with suppress(OSError):
            for index, child in enumerate(repo_path.iterdir(), 1):
                _yield_periodically(index, interval=_DIR_SCAN_YIELD_INTERVAL)
                if not child.is_dir():
                    continue
                if _is_virtual_env_part(child.name):
                    continue
                if not _is_generated_build_dir(child.name):
                    continue
                _info("Removing generated build directory:", str(child))
                shutil.rmtree(child, ignore_errors=True)

    def _repo_content_hash(self, repo_path: Path) -> str:
        """Return a deterministic hash of repository contents for caching."""
        # Fast-path: allow environment flag VISITOR_SKIP_CONTENT_HASH to bypass
        # expensive hashing for large iterative inspection runs. Returns a stable
        # placeholder derived from repo path for cache key segregation without
        # per-file IO.
        fast_flag = os.environ.get("VISITOR_SKIP_CONTENT_HASH", "").strip().lower()
        if fast_flag in {"1", "true", "yes", "on"}:
            placeholder = hashlib.sha256(str(repo_path).encode("utf-8")).hexdigest()
            _LOGGER.debug(
                "skip-content-hash fast path engaged for %s (placeholder=%s, flag=%s)",
                repo_path.name,
                placeholder[:12],
                fast_flag,
            )
            return placeholder

        hasher = hashlib.sha256()
        # Micro-optimisation: materialize directory listing once to avoid repeated
        # generator churn; still stable ordering.
        entries = list(repo_path.rglob("*"))
        for index, p in enumerate(sorted(entries), 1):
            # Reduced yield frequency for speed during hashing
            if index % 250 == 0:
                _cooperative_yield()
            if not p.is_file():
                continue
            if ".git" in p.parts or "__pycache__" in p.parts:
                continue
            if any(_is_virtual_env_part(part) for part in p.parts):
                continue
            if any(_is_generated_build_dir(part) for part in p.parts):
                continue
            if p.suffix in {".pyc", ".pyo"}:
                continue
            rel = p.relative_to(repo_path).as_posix().encode("utf-8")
            hasher.update(rel)
            try:
                hasher.update(p.read_bytes())
            except OSError:
                # Skip unreadable files without failing the whole hash
                continue
        return hasher.hexdigest()

    def _cache_path(self, repo_name: str, tool_name: str, repo_hash: str) -> Path:
        key = f"{repo_name}_{tool_name}_{repo_hash[:16]}"
        return self.cache_dir / f"{key}.json"

    def _prepare_environment(self, python: str, packages: Sequence[str]) -> None:
        proc = subprocess.run(  # noqa: S603
            [python, "-m", "pip", "install", "--upgrade", *packages],
            check=False,
            capture_output=True,
            text=True,
        )
        _cooperative_yield()
        if proc.returncode != 0:
            msg = f"failed to install required packages: {proc.stdout}\n{proc.stderr}"
            raise AssertionError(msg)

        self._tool_versions = self._collect_tool_versions(python)
        _cooperative_yield()
        self._runtime_snapshot = {
            "python_executable": python,
            "python_version": sys.version.replace("\n", " "),
            "platform": platform.platform(),
            "run_started_at": datetime.now(UTC).isoformat(),
            "workspace_root": str(self.root),
        }

        # Traceability: record which acceleration flags (fast paths) are active.
        fast_paths = self._detect_fast_paths()
        self._runtime_snapshot["fast_paths"] = dict(fast_paths)
        active_fast_paths = [name for name, enabled in fast_paths.items() if enabled]
        if active_fast_paths:
            self._runtime_snapshot["fast_paths_active"] = active_fast_paths

        env_snapshot = {
            key: os.environ.get(key)
            for key in ("PATH", "PYTHONPATH", "VIRTUAL_ENV")
            if os.environ.get(key)
        }
        if env_snapshot:
            self._runtime_snapshot["environment"] = env_snapshot

        self._prune_cache()
        _cooperative_yield()

    def _tool_configurations(self, python: str) -> list[ToolConfig]:
        # Fast-path skip: if VISITOR_SKIP_TOOLS is set truthy, return only a
        # lightweight pyright check to drastically reduce run time. This pairs
        # with VISITOR_SKIP_CONTENT_HASH for rapid inspection cycles.
        if os.environ.get("VISITOR_SKIP_TOOLS", "").strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }:
            return [
                ToolConfig(
                    name="pyright",
                    command=[
                        python,
                        "-m",
                        "pyright",
                        ".",
                        "--level",
                        "error",
                    ],
                    skip_if_no_python=True,
                ),
            ]
        return [
            ToolConfig(
                name="ruff_fix",
                command=[
                    python,
                    "-m",
                    "ruff",
                    "check",
                    ".",
                    "--fix",
                    "--select",
                    "ALL",
                    "--ignore",
                    "D,COM812,ISC001,T20",
                    "--line-length",
                    "88",
                    "--target-version",
                    "py311",
                ],
                skip_if_no_python=False,
            ),
            ToolConfig(
                name="black",
                command=[
                    python,
                    "-m",
                    "black",
                    ".",
                    "--line-length",
                    "88",
                    "--target-version",
                    "py311",
                    "--check",
                    "--diff",
                ],
                skip_if_no_python=True,
            ),
            ToolConfig(
                name="ruff_check",
                command=[
                    python,
                    "-m",
                    "ruff",
                    "check",
                    ".",
                    "--select",
                    "ALL",
                    "--ignore",
                    "D,COM812,ISC001,T20",
                    "--line-length",
                    "88",
                    "--target-version",
                    "py311",
                ],
                skip_if_no_python=False,
            ),
            ToolConfig(
                name="mypy",
                command=[
                    python,
                    "-m",
                    "mypy",
                    ".",
                    "--strict",
                    "--no-warn-unused-configs",
                    "--show-error-codes",
                    "--warn-return-any",
                    "--warn-unreachable",
                    "--disallow-any-unimported",
                    "--disallow-any-expr",
                    "--disallow-any-decorated",
                    "--disallow-any-explicit",
                ],
                skip_if_no_python=True,
            ),
            ToolConfig(
                name="pyright",
                command=[
                    python,
                    "-m",
                    "pyright",
                    ".",
                    "--level",
                    "error",
                ],
                skip_if_no_python=True,
            ),
        ]

    def _collect_repo_files(self, repo_path: Path) -> list[str]:
        files: list[str] = []
        normalized_repo = _normalize_repo_name(repo_path.name)
        allowlist = self._file_allowlist.get(normalized_repo)
        for index, pth in enumerate(repo_path.rglob("*"), 1):
            _yield_periodically(index, interval=_FILE_SCAN_YIELD_INTERVAL)
            if not pth.is_file():
                continue
            if ".git" in pth.parts or "__pycache__" in pth.parts:
                continue
            if any(_is_virtual_env_part(part) for part in pth.parts):
                continue
            if any(_is_generated_build_dir(part) for part in pth.parts):
                continue
            if pth.suffix.lower() not in {".py", ".pyi"}:
                continue
            rel_path = pth.relative_to(repo_path).as_posix()
            normalized_rel = _normalize_rel_path(rel_path)
            if allowlist and normalized_rel not in allowlist:
                continue
            files.append(normalized_rel)
        return sorted(files)

    def _extract_failure_entries(
        self,
        *,
        repo: RepoContext,
        result: Mapping[str, object],
    ) -> list[dict[str, str]]:
        stdout_text = self._ensure_text(result.get("stdout", ""))
        stderr_text = self._ensure_text(result.get("stderr", ""))
        if not repo.files:
            return []
        combined_lines = [line.strip() for line in stdout_text.splitlines()]
        combined_lines.extend(line.strip() for line in stderr_text.splitlines())
        entries: list[dict[str, str]] = []
        seen: set[str] = set()
        for rel_path in repo.files:
            variants = {rel_path, rel_path.replace("/", os.sep)}
            snippets = [
                line
                for line in combined_lines
                if any(variant in line for variant in variants)
            ]
            if not snippets:
                continue
            if rel_path in seen:
                continue
            seen.add(rel_path)
            entries.append(
                {
                    "file": rel_path,
                    "message": "\n".join(snippets[:OUTPUT_PREVIEW_LIMIT]),
                },
            )
        return entries

    def _event_duration_ms(self, result: Mapping[str, object]) -> int | None:
        value = result.get("duration_seconds")
        if isinstance(value, (int, float)):
            return int(max(float(value), 0.0) * 1000)
        return None

    def _collect_files_checked(self, payload: _ToolEventPayload) -> list[str]:
        files_checked_obj = payload.result.get("files_checked")
        if isinstance(files_checked_obj, (list, tuple)):
            candidate_entries = cast("Sequence[object]", files_checked_obj)
            collected = [
                candidate
                for candidate in candidate_entries
                if isinstance(candidate, str)
            ]
            if collected:
                return collected
        return list(payload.repo.files)

    def _collect_failure_entries(
        self,
        payload: _ToolEventPayload,
    ) -> tuple[list[dict[str, str]], list[str]]:
        failure_entries: list[dict[str, str]] = []
        failed_files: list[str] = []
        if payload.failures:
            for entry in payload.failures:
                file_name = entry.get("file")
                if file_name:
                    failed_files.append(file_name)
                    message = entry.get("message", "")
                    failure_entries.append({"file": file_name, "message": message})
        if failure_entries:
            return failure_entries, failed_files

        failed_files_obj = payload.result.get("failed_files")
        if isinstance(failed_files_obj, (list, tuple)):
            for entry_obj in cast("Sequence[object]", failed_files_obj):
                if not isinstance(entry_obj, Mapping):
                    continue
                typed_entry = cast("Mapping[str, object]", entry_obj)
                file_name_obj = typed_entry.get("file")
                if isinstance(file_name_obj, str) and file_name_obj:
                    failed_files.append(file_name_obj)
                    message_obj = typed_entry.get("message")
                    failure_entries.append(
                        {
                            "file": file_name_obj,
                            "message": (
                                message_obj if isinstance(message_obj, str) else ""
                            ),
                        },
                    )
        return failure_entries, failed_files

    def _resolve_files_for_event(
        self,
        *,
        status: str,
        files_checked: Sequence[str],
        failed_files: Sequence[str],
    ) -> list[str]:
        if status == "failed" and failed_files:
            return _dedupe_preserving_order(failed_files)
        return list(files_checked)

    def _build_event_details(
        self,
        *,
        payload: _ToolEventPayload,
        files_checked: Sequence[str],
        files_for_event: Sequence[str],
        failure_entries: Sequence[dict[str, str]],
    ) -> dict[str, object]:
        details: dict[str, object] = {
            "repo": payload.repo.rel_path,
            "repo_path": str(payload.repo.path),
            "tool": payload.config.name,
            "tool_family": payload.module_name,
            "files": list(files_for_event),
            "files_checked": list(files_checked),
            "cached": bool(payload.result.get("cached", False)),
            "skipped": bool(payload.result.get("skipped", False)),
            "timed_out": bool(payload.result.get("timed_out", False)),
        }
        if payload.summary:
            details["failure_summary"] = payload.summary
        if failure_entries:
            details["failures"] = list(failure_entries)
            details["failed_files"] = list(failure_entries)
        else:
            details["failed_files"] = []
        return details

    def _emit_tool_event(self, payload: _ToolEventPayload) -> None:
        duration_ms = self._event_duration_ms(payload.result)
        files_checked = self._collect_files_checked(payload)
        failure_entries, failed_files_for_event = self._collect_failure_entries(payload)
        files_for_event = self._resolve_files_for_event(
            status=payload.status,
            files_checked=files_checked,
            failed_files=failed_files_for_event,
        )
        details = self._build_event_details(
            payload=payload,
            files_checked=files_checked,
            files_for_event=files_for_event,
            failure_entries=failure_entries,
        )
        log_data = dict(details)
        log_data["status"] = payload.status
        log_data["duration_ms"] = duration_ms
        if payload.summary:
            log_data["summary"] = payload.summary
        if failure_entries:
            log_data["failure_count"] = len(failure_entries)

        message = f"{payload.config.name} {payload.status} for {payload.repo.rel_path}"
        if payload.summary:
            message = f"{message}: {payload.summary}"

        if payload.status == "failed":
            _LOGGER.warning("%s | details=%s", message, log_data)
        else:
            _LOGGER.debug("%s | details=%s", message, log_data)
        # Streaming mirror (tool-level)
        self._emit_tool_stream_event(
            payload,
            failures=failure_entries if failure_entries else None,
        )

    def _process_repository(
        self,
        repo_path: Path,
        python: str,
        timeout: int,
    ) -> RepoProcessingResult:
        _cooperative_yield()
        self._cleanup_generated_build_dirs(repo_path)
        rel = str(repo_path.relative_to(self.root))
        repo_hash = self._repo_content_hash(repo_path)
        repo_files = self._collect_repo_files(repo_path)
        # Quick mode: skip tool execution entirely for speed; emit a minimal report
        # capturing file discovery only. Intended for inspection-only fast passes.
        if os.environ.get("VISITOR_QUICK_MODE", "").strip().lower() in {
            "1",
            "true",
            "yes",
            "on",
        }:
            repo_context = RepoContext(
                path=repo_path,
                rel_path=rel,
                repo_hash=repo_hash,
                has_python=bool(repo_files),
                files=tuple(repo_files),
            )
            quick_repo_report: RepoReport = {
                "timestamp": datetime.now(UTC).isoformat(),
                "repo_hash": repo_context.repo_hash,
                "tool_reports": {},
                "files": repo_files,
            }
            return RepoProcessingResult(
                relative_name=repo_context.rel_path,
                report=quick_repo_report,
                failure_messages=[],
                failure_details=[],
            )
        repo_context = RepoContext(
            path=repo_path,
            rel_path=rel,
            repo_hash=repo_hash,
            has_python=bool(repo_files),
            files=tuple(repo_files),
        )

        tool_reports: dict[str, ToolResult] = {}
        failure_messages: list[str] = []
        failure_details: list[dict[str, object]] = []

        configs = self._tool_configurations(python)
        # Emit repo start streaming event
        self._emit_repo_event(repo=repo_context, phase="start")
        for index, config in enumerate(configs, 1):
            outcome = self._run_tool_for_repo(
                repo=repo_context,
                config=config,
                timeout=timeout,
            )
            tool_reports[config.name] = outcome.result
            if outcome.failure_message:
                failure_messages.append(outcome.failure_message)
            if outcome.failure_detail:
                failure_details.append(outcome.failure_detail)
            _yield_periodically(index, interval=_TOOL_ITERATION_YIELD_INTERVAL)

        repo_report: RepoReport = {
            "timestamp": datetime.now(UTC).isoformat(),
            "repo_hash": repo_context.repo_hash,
            "tool_reports": tool_reports,
            "files": repo_files,
        }

        result_obj = RepoProcessingResult(
            relative_name=repo_context.rel_path,
            report=repo_report,
            failure_messages=failure_messages,
            failure_details=failure_details,
        )
        # Emit repo completion streaming event
        status = "failed" if failure_messages else "succeeded"
        summary_payload = {
            "failed_tools": len(failure_messages),
            "tool_count": len(configs),
        }
        self._emit_repo_event(
            repo=repo_context,
            phase="complete",
            status=status,
            summary=summary_payload,
            messages=failure_messages if failure_messages else None,
        )
        return result_obj

    def _build_skip_outcome(
        self,
        *,
        repo: RepoContext,
        config: ToolConfig,
        tool_version: str,
        module_name: str,
    ) -> ToolOutcome:
        now_iso = datetime.now(UTC).isoformat()
        command = self._build_tool_command(repo=repo, config=config)
        skip_result: ToolResult = {
            "exit": 0,
            "stdout": "",
            "stderr": "skipped - no Python source (.py/.pyi) found",
            "cached": False,
            "skipped": True,
            "skip_reason": "no_python_files",
            "cmd": command,
            "cmd_display": " ".join(str(part) for part in command),
            "cwd": str(repo.path),
            "started_at": now_iso,
            "ended_at": now_iso,
            "duration_seconds": 0.0,
            "repo_hash": repo.repo_hash,
            "tool_version": tool_version,
            "tool_module": module_name,
        }
        return ToolOutcome(skip_result)

    def _load_cached_outcome(
        self,
        *,
        repo: RepoContext,
        config: ToolConfig,
        tool_version: str,
        module_name: str,
    ) -> ToolOutcome | None:
        cached = self._load_cache(repo.rel_path, config.name, repo.repo_hash)
        if cached is None:
            return None
        command = self._build_tool_command(repo=repo, config=config)
        cached_result: ToolResult = dict(cached)
        cached_result["cached"] = True
        cached_result.setdefault("cmd", command)
        cached_result.setdefault(
            "cmd_display",
            " ".join(str(part) for part in command),
        )
        cached_result.setdefault("cwd", str(repo.path))
        cached_result.setdefault("repo_hash", repo.repo_hash)
        cached_result.setdefault("tool_version", tool_version)
        cached_result.setdefault("tool_module", module_name)
        cached_result.setdefault("started_at", "")
        cached_result.setdefault("ended_at", "")
        cached_result.setdefault("duration_seconds", 0.0)
        _info(f"{config.name}: cache hit for {repo.rel_path}")
        return ToolOutcome(cached_result)

    def _build_tool_command(
        self,
        *,
        repo: RepoContext,
        config: ToolConfig,
    ) -> list[str]:
        command = list(config.command)
        if config.name == "mypy":
            try:
                target_index = command.index(".")
            except ValueError:
                target_index = -1
            if target_index >= 0:
                command[target_index : target_index + 1] = [
                    "--package",
                    repo.path.name,
                ]
        return command

    def _build_tool_environment(self, *, repo: RepoContext) -> dict[str, str]:
        env = os.environ.copy()
        pythonpath_entries: list[str] = [str(repo.path), str(self.root)]
        shared_typings_candidates = [
            self.root / "x_make_common_x" / "shared_typings",
            self.root / "typings",
        ]
        for shared_typings in shared_typings_candidates:
            if shared_typings.exists():
                pythonpath_entries.append(str(shared_typings))
                break
        repo_typings = repo.path / "typings"
        if repo_typings.exists():
            pythonpath_entries.append(str(repo_typings))
        existing = env.get("PYTHONPATH")
        if existing:
            pythonpath_entries.extend(
                part for part in existing.split(os.pathsep) if part
            )
        env["PYTHONPATH"] = os.pathsep.join(
            _dedupe_preserving_order(pythonpath_entries),
        )
        return env

    def _execute_tool_command(
        self,
        *,
        repo: RepoContext,
        command: Sequence[str],
        timeout: int,
        env: Mapping[str, str] | None = None,
    ) -> tuple[int | None, str, str, bool, datetime, datetime, float]:
        start_wall = datetime.now(UTC)
        start_perf = time.perf_counter()
        timed_out = False
        env_mapping = dict(env) if env is not None else os.environ.copy()
        try:
            _cooperative_yield()
            completed: CompletedProcess[str] = subprocess.run(  # noqa: S603
                list(command),
                check=False,
                cwd=str(repo.path),
                capture_output=True,
                text=True,
                timeout=timeout,
                env=env_mapping,
            )
        except subprocess.TimeoutExpired as exc:  # pragma: no cover - diag path
            timed_out = True
            exit_code = None
            stdout_timeout = cast(
                "str | bytes | bytearray | memoryview | None",
                exc.output,
            )
            stderr_timeout = cast(
                "str | bytes | bytearray | memoryview | None",
                exc.stderr,
            )
            stdout_text = self._ensure_text(stdout_timeout)
            stderr_text = self._ensure_text(stderr_timeout)
        else:
            exit_code = completed.returncode
            stdout_raw = cast(
                "str | bytes | bytearray | memoryview | None",
                completed.stdout,
            )
            stderr_raw = cast(
                "str | bytes | bytearray | memoryview | None",
                completed.stderr,
            )
            stdout_text = self._ensure_text(stdout_raw)
            stderr_text = self._ensure_text(stderr_raw)
        end_wall = datetime.now(UTC)
        duration = max(time.perf_counter() - start_perf, 0.0)
        return (
            exit_code,
            stdout_text,
            stderr_text,
            timed_out,
            start_wall,
            end_wall,
            duration,
        )

    def _run_tool_for_repo(
        self,
        *,
        repo: RepoContext,
        config: ToolConfig,
        timeout: int,
    ) -> ToolOutcome:
        module_name = TOOL_MODULE_MAP.get(config.name, config.name)
        tool_version = self._tool_versions.get(module_name, "<unknown>")

        self._emit_tool_event(
            _ToolEventPayload(
                repo=repo,
                config=config,
                module_name=module_name,
                status="started",
                result={
                    "duration_seconds": 0.0,
                    "cached": False,
                    "skipped": False,
                },
            ),
        )

        if config.skip_if_no_python and not repo.has_python:
            _info(f"{config.name}: skipped (no Python files) in {repo.rel_path}")
            outcome = self._build_skip_outcome(
                repo=repo,
                config=config,
                tool_version=tool_version,
                module_name=module_name,
            )
            self._emit_tool_event(
                _ToolEventPayload(
                    repo=repo,
                    config=config,
                    module_name=module_name,
                    status="skipped",
                    result=outcome.result,
                    summary="No Python files detected; skipping",
                ),
            )
            return outcome

        cached_outcome = self._load_cached_outcome(
            repo=repo,
            config=config,
            tool_version=tool_version,
            module_name=module_name,
        )
        if cached_outcome is not None:
            self._emit_tool_event(
                _ToolEventPayload(
                    repo=repo,
                    config=config,
                    module_name=module_name,
                    status="succeeded",
                    result=cached_outcome.result,
                    summary="Result loaded from cache",
                ),
            )
            return cached_outcome

        command = self._build_tool_command(repo=repo, config=config)
        env = self._build_tool_environment(repo=repo)
        (
            exit_code,
            proc_stdout,
            proc_stderr,
            timed_out,
            start_wall,
            end_wall,
            duration,
        ) = self._execute_tool_command(
            repo=repo,
            command=command,
            timeout=timeout,
            env=env,
        )

        result: ToolResult = {
            "exit": exit_code,
            "stdout": proc_stdout,
            "stderr": proc_stderr,
            "cached": False,
            "cmd": command,
            "cmd_display": " ".join(str(part) for part in command),
            "cwd": str(repo.path),
            "started_at": start_wall.isoformat(),
            "ended_at": end_wall.isoformat(),
            "duration_seconds": duration,
            "repo_hash": repo.repo_hash,
            "tool_version": tool_version,
            "tool_module": module_name,
        }
        result["files_checked"] = list(repo.files)
        result["failed_files"] = []
        if timed_out:
            result["timed_out"] = True
            result["timeout_seconds"] = timeout

        failure_condition = timed_out or exit_code is None or exit_code != 0
        if failure_condition:
            self._delete_cache(repo.rel_path, config.name, repo.repo_hash)
            message, detail = self._build_failure_payload(
                repo=repo,
                config=config,
                timed_out=timed_out,
                result=result,
            )
            _info(f"{config.name}: failure in {repo.rel_path}; details captured")
            failure_entries = self._extract_failure_entries(repo=repo, result=result)
            if failure_entries:
                result["failed_files"] = failure_entries
            self._emit_tool_event(
                _ToolEventPayload(
                    repo=repo,
                    config=config,
                    module_name=module_name,
                    status="failed",
                    result=result,
                    summary=message,
                    failures=tuple(failure_entries),
                ),
            )
            return ToolOutcome(result, message, detail)

        self._store_cache(repo.rel_path, config.name, repo.repo_hash, result)
        self._emit_tool_event(
            _ToolEventPayload(
                repo=repo,
                config=config,
                module_name=module_name,
                status="succeeded",
                result=result,
            ),
        )
        return ToolOutcome(result)

    def _build_failure_payload(
        self,
        *,
        repo: RepoContext,
        config: ToolConfig,
        timed_out: bool,
        result: ToolResult,
    ) -> tuple[str, dict[str, object]]:
        stdout_text = self._ensure_text(result.get("stdout", ""))
        stderr_text = self._ensure_text(result.get("stderr", ""))
        truncated_stdout = stdout_text.strip().splitlines()
        truncated_stderr = stderr_text.strip().splitlines()
        preview_stdout = _preview_lines(truncated_stdout, OUTPUT_PREVIEW_LIMIT)
        preview_stderr = _preview_lines(truncated_stderr, OUTPUT_PREVIEW_LIMIT)
        exit_code = _coerce_exit_code(result.get("exit"))
        exit_display = "timeout" if timed_out else f"exit {exit_code}"
        duration_value = result.get("duration_seconds", 0.0)
        if isinstance(duration_value, (int, float)):
            duration = float(duration_value)
        else:
            duration = 0.0
        tool_version = self._ensure_text(result.get("tool_version", "<unknown>"))
        cmd_display = self._ensure_text(result.get("cmd_display", ""))
        started_at = self._ensure_text(result.get("started_at", ""))
        failure_message_lines = [
            f"{config.name} failed for {repo.rel_path} ({exit_display})",
            f"cwd: {repo.path}",
            f"command: {cmd_display}",
            f"started_at: {started_at}",
            f"duration: {duration:.3f}s",
            f"tool_version: {tool_version}",
            f"stdout:\n{preview_stdout or '<empty>'}",
            f"stderr:\n{preview_stderr or '<empty>'}",
        ]
        failure_message = "\n".join(failure_message_lines)
        failure_detail: dict[str, object] = {
            "repo": repo.rel_path,
            "repo_path": str(repo.path),
            "tool": config.name,
            "tool_module": self._ensure_text(result.get("tool_module", config.name)),
        }
        failure_detail.update(result)
        return failure_message, failure_detail

    def _ensure_reports_dir(self) -> Path:
        reports_dir = self._reports_dir
        reports_dir.mkdir(parents=True, exist_ok=True)
        return reports_dir

    def _remove_legacy_json_reports(self) -> None:
        legacy_names = (
            "x_index_a_a_priori_x.json",
            "x_index_b_a_posteriori_x.json",
            "x_summary_report_x.json",
            "x_tool_failures_x.json",
        )
        for name in legacy_names:
            stale_path = self.package_root / name
            with suppress(OSError):
                if stale_path.exists():
                    stale_path.unlink()

    def _purge_markdown_stragglers(self) -> int:
        reports_dir = self._reports_dir
        try:
            candidates = list(reports_dir.glob("visitor_failures_*.md"))
        except OSError:
            return 0
        removed = 0
        for candidate in candidates:
            try:
                candidate.unlink()
            except OSError:
                continue
            removed += 1
        return removed

    def _summarize_failure_message(self, message: str) -> str:
        collapsed = " ".join(message.strip().split())
        if not collapsed:
            return "Tool failure recorded"
        if len(collapsed) <= SUMMARY_MESSAGE_LIMIT:
            return collapsed
        return collapsed[: SUMMARY_MESSAGE_LIMIT - 1] + "…"

    def _command_display(self, detail: Mapping[str, object]) -> str:
        cmd_display = detail.get("cmd_display")
        if isinstance(cmd_display, str) and cmd_display.strip():
            return cmd_display.strip()
        raw_cmd = detail.get("cmd")
        if isinstance(raw_cmd, Sequence) and not isinstance(
            raw_cmd,
            (str, bytes, bytearray),
        ):
            parts_seq = cast("Sequence[object]", raw_cmd)
            parts = [str(part) for part in parts_seq]
            if parts:
                return " ".join(parts)
        return "<command unavailable>"

    def _ensure_detail_text(self, detail: Mapping[str, object], key: str) -> str:
        value = detail.get(key)
        if value is None:
            return ""
        if isinstance(value, str):
            return value
        return str(value)

    def _detail_value(
        self,
        detail: Mapping[str, object],
        *keys: str,
        default: str = "",
    ) -> str:
        for key in keys:
            value = self._ensure_detail_text(detail, key)
            if value:
                return value
        return default

    def _stat_value(self, mapping: Mapping[str, object], key: str) -> int:
        value = mapping.get(key)
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, (int, float)):
            return int(value)
        if isinstance(value, str):
            with suppress(ValueError):
                return int(value)
        return 0

    def _exit_display(self, detail: Mapping[str, object]) -> str:
        if detail.get("timed_out"):
            timeout = self._detail_value(detail, "timeout_seconds")
            return f"timeout after {timeout}s" if timeout else "timeout"

        exit_code = _coerce_exit_code(detail.get("exit"))
        if exit_code is None:
            return "exit <unknown>"
        return f"exit {exit_code}"

    def _preview_output(self, detail: Mapping[str, object], key: str) -> str:
        text = self._ensure_text(detail.get(key, ""))
        return _preview_lines(text.splitlines(), OUTPUT_PREVIEW_LIMIT)

    def _serialize_failures(
        self,
        detail_pairs: Sequence[tuple[Mapping[str, object], str]],
        *,
        artifact_dir: Path | None = None,
    ) -> list[dict[str, JSONValue]]:
        entries: list[dict[str, JSONValue]] = []
        for index, (detail, message) in enumerate(detail_pairs, 1):
            repo = self._detail_value(detail, "repo", "repo_path", default="")
            tool = self._detail_value(detail, "tool", "tool_module", default="")
            preview = self._summarize_failure_message(message)
            command_display = self._command_display(detail)
            exit_display = self._exit_display(detail)
            repo_path = self._detail_value(detail, "repo_path", "cwd") or None
            suggestion = (
                self._detail_value(
                    detail,
                    "next_action",
                    default="Investigate",
                )
                or None
            )
            captured_at = self._detail_value(detail, "ended_at", "started_at") or None
            tool_version = self._detail_value(detail, "tool_version") or None
            stdout_preview = self._preview_output(detail, "stdout") or None
            stderr_preview = self._preview_output(detail, "stderr") or None
            stdout_artifact = None
            stderr_artifact = None
            if artifact_dir is not None:
                repo_label = repo or repo_path or "repo"
                tool_label = tool or "tool"
                stdout_artifact = self._persist_failure_artifact(
                    request=_ArtifactRequest(
                        directory=artifact_dir,
                        index=index,
                        repo=repo_label,
                        tool=tool_label,
                        kind="stdout",
                    ),
                    content=self._ensure_text(detail.get("stdout", "")),
                )
                stderr_artifact = self._persist_failure_artifact(
                    request=_ArtifactRequest(
                        directory=artifact_dir,
                        index=index,
                        repo=repo_label,
                        tool=tool_label,
                        kind="stderr",
                    ),
                    content=self._ensure_text(detail.get("stderr", "")),
                )
            entries.append(
                {
                    "repo": repo or None,
                    "tool": tool or None,
                    "summary": preview,
                    "message": message,
                    "command": command_display,
                    "exit": exit_display,
                    "repo_path": repo_path,
                    "tool_version": tool_version,
                    "captured_at": captured_at,
                    "suggested_action": suggestion,
                    "stdout_preview": stdout_preview,
                    "stderr_preview": stderr_preview,
                    "stdout_artifact": stdout_artifact,
                    "stderr_artifact": stderr_artifact,
                    "detail": self._sanitize_failure_detail(detail),
                },
            )
        entries.sort(
            key=lambda entry: (
                str(entry.get("repo") or "").casefold(),
                str(entry.get("tool") or "").casefold(),
                str(entry.get("summary") or ""),
            ),
        )
        return entries

    def failure_detail_pairs(self) -> list[tuple[dict[str, object], str]]:
        return list(zip(self._failure_details, self._failure_messages, strict=False))

    def sanitized_failure_details(self) -> list[dict[str, JSONValue]]:
        return [
            self._sanitize_failure_detail(detail) for detail in self._failure_details
        ]

    def _write_failure_context(
        self,
        *,
        generated_at: datetime,
        summary: Mapping[str, object],
        failures: Sequence[Mapping[str, JSONValue]],
        report_path: Path,
        artifact_dir: Path | None,
    ) -> Path:
        del summary  # retained for future templating expansion
        repo_counters, tool_counts = _summarize_failures_for_digest(failures)
        doc_guard_status, straggler_display, straggler_count = _doc_guard_summary(
            self._find_markdown_straggler(),
            self.root,
        )
        artifact_display = str(artifact_dir) if artifact_dir else "(not captured)"
        summary_block = _build_summary_block(
            generated_at=generated_at,
            issue_count=len(failures),
            repo_count=len(repo_counters),
            doc_guard_status=doc_guard_status,
            straggler_count=straggler_count,
            artifact_root=artifact_display,
        )
        context_payload: dict[str, JSONValue] = {
            "generated_at": generated_at.isoformat(),
            "schema_version": VISITOR_REPORT_SCHEMA_VERSION,
            "source_report": _relativize_path(report_path, self.root)
            or str(report_path),
            "artifact_root": artifact_display,
            "summary_block": summary_block,
            "repo_table": _format_repo_table(repo_counters),
            "tool_table": _format_tool_table(tool_counts),
            "doc_guard_status": doc_guard_status,
            "straggler_path": straggler_display,
            "next_actions": _DEFAULT_NEXT_ACTIONS,
        }
        context_path = self._context_output_path()
        context_path.parent.mkdir(parents=True, exist_ok=True)
        self._atomic_write_json(context_path, context_payload)
        return context_path

    def _write_failure_reports(self) -> tuple[Path, Path]:
        reports_dir = self._ensure_reports_dir()
        now = datetime.now(UTC)
        timestamp = now.strftime("%Y%m%d_%H%M%S")
        base_name = f"visitor_failures_{timestamp}"
        json_path = reports_dir / f"{base_name}.json"

        summary = self.generate_summary_report()
        detail_pairs = list(
            zip(self._failure_details, self._failure_messages, strict=False),
        )
        artifact_dir = self._artifact_run_dir(base_name) if detail_pairs else None
        failures = self._serialize_failures(detail_pairs, artifact_dir=artifact_dir)

        payload: dict[str, JSONValue] = {
            "schema_version": VISITOR_REPORT_SCHEMA_VERSION,
            "generated_at": now.isoformat(),
            "workspace_root": str(self.root),
            "runtime": _json_ready(dict(self._runtime_snapshot)),
            "tool_versions": _json_ready(dict(self._tool_versions)),
            "summary": _json_ready(summary),
            "failures": _json_ready(failures),
            "artifact_root": str(artifact_dir) if artifact_dir else None,
        }
        payload_checksum = self._hash_report_payload(payload)
        payload["payload_checksum"] = payload_checksum
        self._validate_report_payload(payload)

        self._atomic_write_json(json_path, payload)
        self._write_checksum_sidecar(json_path)
        context_path = self._write_failure_context(
            generated_at=now,
            summary=summary,
            failures=failures,
            report_path=json_path,
            artifact_dir=artifact_dir,
        )
        self._last_report_path = json_path
        self._last_markdown_report_path = None
        self._last_context_path = context_path
        return json_path, context_path

    def _finalize_run_result(
        self,
        report_path: Path | None,
        *,
        markdown_path: Path | None,
        context_path: Path | None,
    ) -> VisitorRunResult:
        had_failures = bool(self._last_run_failures)
        messages = tuple(self._failure_messages)
        details = tuple(
            {
                key: cast("object", value)
                for key, value in self._sanitize_failure_detail(detail).items()
            }
            for detail in self._failure_details
        )

        if had_failures:
            preview_chunks = list(messages[:FAILURE_PREVIEW_LIMIT])
            preview = "\n\n".join(preview_chunks)
            _info("toolchain failure preview:")
            if preview:
                for block in preview.split("\n\n"):
                    _info(block)
            if len(messages) > FAILURE_PREVIEW_LIMIT:
                _info("…additional failures omitted…")
            if report_path is not None:
                _info("toolchain JSON report:", str(report_path))
            if context_path is not None:
                _info("visitor failure context:", str(context_path))
            if report_path is None and context_path is None:
                _info("toolchain failures recorded; report paths unavailable")

        result = VisitorRunResult(
            report_path=report_path,
            markdown_report_path=markdown_path,
            context_path=context_path,
            had_failures=had_failures,
            failure_messages=messages,
            failure_details=details,
            skipped=False,
        )
        self._last_run_result = result
        return result

    def _load_cache(
        self,
        repo_name: str,
        tool_name: str,
        repo_hash: str,
    ) -> ToolResult | None:
        if not self.enable_cache:
            return None
        cache_file = self._cache_path(repo_name, tool_name, repo_hash)
        if not cache_file.exists():
            return None
        try:
            with cache_file.open("r", encoding="utf-8") as fh:
                cached = cast("ToolResult", json.load(fh))
        except (OSError, json.JSONDecodeError):
            with suppress(OSError):
                cache_file.unlink()
            return None
        exit_value = cached.get("exit", 0)
        exit_code: int | None
        if isinstance(exit_value, int):
            exit_code = exit_value
        elif isinstance(exit_value, str):
            try:
                exit_code = int(exit_value)
            except ValueError:
                exit_code = None
        else:
            exit_code = None
        if exit_code not in (None, 0):
            self._delete_cache(repo_name, tool_name, repo_hash)
            return None
        return cached

    def _store_cache(
        self,
        repo_name: str,
        tool_name: str,
        repo_hash: str,
        payload: ToolResult,
    ) -> None:
        if not self.enable_cache:
            return
        cache_file = self._cache_path(repo_name, tool_name, repo_hash)
        with suppress(OSError):
            self._atomic_write_json(cache_file, payload)

    def _delete_cache(
        self,
        repo_name: str,
        tool_name: str,
        repo_hash: str,
    ) -> None:
        if not self.enable_cache:
            return
        cache_file = self._cache_path(repo_name, tool_name, repo_hash)
        with suppress(OSError):
            cache_file.unlink()

    def _prune_cache(self, keep: int = 500) -> None:
        if not self.enable_cache or not self.cache_dir.exists():
            return
        try:
            candidate_files = list(self.cache_dir.glob("*.json"))
        except OSError:
            return

        def _file_mtime(path: Path) -> float:
            try:
                return path.stat().st_mtime
            except OSError:
                return 0.0

        cache_files = sorted(candidate_files, key=_file_mtime)
        overflow = len(cache_files) - keep
        if overflow <= 0:
            return
        for index, stale in enumerate(cache_files[:overflow], 1):
            _yield_periodically(index, interval=_FILE_SCAN_YIELD_INTERVAL)
            with suppress(OSError):
                stale.unlink()

    def _collect_tool_versions(self, python: str) -> dict[str, str]:
        versions: dict[str, str] = {}
        for module in sorted({*TOOL_MODULE_MAP.values()}):
            try:
                proc = subprocess.run(  # noqa: S603
                    [python, "-m", module, "--version"],
                    check=False,
                    capture_output=True,
                    text=True,
                    timeout=30,
                )
            except (
                OSError,
                subprocess.TimeoutExpired,
                subprocess.SubprocessError,
            ) as exc:  # pragma: no cover - diagnostics only
                versions[module] = f"<error invoking --version: {exc}>"
                continue
            output = (proc.stdout or proc.stderr).strip()
            if proc.returncode != 0:
                versions[module] = f"<exit {proc.returncode}> {output}"
            else:
                versions[module] = output or "<no output>"
            _cooperative_yield()
        return versions

    def body(self, *, children: Iterable[Path] | None = None) -> None:  # noqa: C901
        """Run ruff/black/mypy/pyright against each child repository."""

        python = sys.executable
        self._prepare_environment(python, REQUIRED_PACKAGES)

        # Traceability: record selected tools based on current acceleration flags.
        try:
            selected = [cfg.name for cfg in self._tool_configurations(python)]
        except (RuntimeError, ValueError, TypeError):
            selected = []
        if selected:
            self._runtime_snapshot["selected_tools"] = list(selected)

        reports: dict[str, RepoReport] = {}
        failure_messages: list[str] = []
        failure_details: list[dict[str, object]] = []

        repo_iterable = list(children) if children is not None else self._child_dirs()
        writer = self.progress_writer

        def _relative_name(path: Path) -> str:
            try:
                return str(path.relative_to(self.root))
            except ValueError:
                return path.name

        repo_names: dict[Path, str] = {
            child: _relative_name(child) for child in repo_iterable
        }

        if writer is not None:
            for child, rel_name in repo_names.items():
                writer.record_pending(
                    rel_name,
                    display_name=child.name,
                    metadata={
                        "absolute_path": str(child),
                        "relative_path": rel_name,
                    },
                )

        for index, child in enumerate(repo_iterable, 1):
            rel_name = repo_names.get(child) or _relative_name(child)
            display_name = Path(rel_name).name or child.name
            if writer is not None:
                writer.record_start(
                    rel_name,
                    display_name=display_name,
                    metadata={
                        "absolute_path": str(child),
                        "relative_path": rel_name,
                    },
                )

            result = self._process_repository(
                child,
                python,
                DEFAULT_TIMEOUT_SECONDS,
            )
            reports[result.relative_name] = result.report
            failure_messages.extend(result.failure_messages)
            failure_details.extend(result.failure_details)

            repo_metadata: dict[str, object] = {
                "absolute_path": str(child),
                "relative_path": result.relative_name,
                "repo_hash": result.report.get("repo_hash"),
                "tool_reports": result.report.get("tool_reports"),
            }

            if writer is not None:
                if result.failure_messages:
                    failure_meta = dict(repo_metadata)
                    if result.failure_details:
                        failure_meta["failure_details"] = result.failure_details
                    writer.record_failure(
                        result.relative_name,
                        display_name=display_name,
                        metadata=failure_meta,
                        messages=result.failure_messages,
                    )
                else:
                    tool_reports = result.report.get("tool_reports")
                    tool_count = (
                        len(tool_reports) if isinstance(tool_reports, dict) else 0
                    )
                    success_message = (
                        f"All {tool_count} tool(s) succeeded."
                        if tool_count
                        else "Inspection succeeded."
                    )
                    writer.record_success(
                        result.relative_name,
                        display_name=display_name,
                        metadata=repo_metadata,
                        messages=[success_message],
                    )

            _yield_periodically(index, interval=_REPO_ITERATION_YIELD_INTERVAL)

        self._tool_reports = reports
        self._last_run_failures = bool(failure_messages)
        self._failure_messages = failure_messages
        self._failure_details = failure_details
        self._runtime_snapshot["run_completed_at"] = datetime.now(UTC).isoformat()

    def cleanup(self) -> None:
        """Placeholder for cleanup. Override if needed."""
        return

    def generate_summary_report(self) -> dict[str, object]:
        """Produce an aggregate summary of the most recent tool run."""
        overall_stats: dict[str, object] = {
            "cache_hits": 0,
            "cache_misses": 0,
            "failed_tools": 0,
            "total_tools_run": 0,
            "had_failures": bool(self._last_run_failures),
        }
        repos_section: dict[str, dict[str, object]] = {}
        summary: dict[str, object] = {
            "timestamp": datetime.now(UTC).isoformat(),
            "total_repos": len(self._tool_reports),
            "overall_stats": overall_stats,
            "repos": repos_section,
        }
        # Surface acceleration flag usage in summary for downstream traceability.
        fast_paths = self._detect_fast_paths()
        summary["fast_paths"] = dict(fast_paths)
        summary["fast_paths_active"] = [
            name for name, enabled in fast_paths.items() if enabled
        ]
        for repo_name, report in self._tool_reports.items():
            tools_summary: dict[str, dict[str, object]] = {}
            repo_summary: dict[str, object] = {
                "repo_hash": report.get("repo_hash"),
                "tools": tools_summary,
                "cached": 0,
                "failed": 0,
            }
            raw_tools = report.get("tool_reports")
            tool_map: dict[str, ToolResult]
            if isinstance(raw_tools, dict):
                tool_map = cast("dict[str, ToolResult]", raw_tools)
            else:
                tool_map = {}
            for tool_name, tool_report in tool_map.items():
                exit_code = _coerce_exit_code(tool_report.get("exit"))
                cached_flag = bool(tool_report.get("cached", False))
                timed_out_flag = bool(tool_report.get("timed_out", False))
                tools_summary[tool_name] = {
                    "exit": exit_code,
                    "cached": cached_flag,
                    "timed_out": timed_out_flag,
                }
                _increment_counter(overall_stats, "total_tools_run")
                if cached_flag:
                    _increment_counter(repo_summary, "cached")
                    _increment_counter(overall_stats, "cache_hits")
                else:
                    _increment_counter(overall_stats, "cache_misses")
                if timed_out_flag or exit_code not in (None, 0):
                    _increment_counter(repo_summary, "failed")
                    _increment_counter(overall_stats, "failed_tools")
            repos_section[repo_name] = repo_summary
        return summary

    def runtime_snapshot(self) -> dict[str, object]:
        """Return a copy of the runtime snapshot for JSON serialization."""
        return dict(self._runtime_snapshot)

    def tool_versions(self) -> dict[str, str]:
        """Return a copy of the tool version map from the last run."""
        return dict(self._tool_versions)

    def serialize_failures(
        self,
        detail_pairs: Sequence[tuple[Mapping[str, object], str]],
    ) -> list[dict[str, JSONValue]]:
        """Serialize failure detail/message pairs for JSON output."""
        return self._serialize_failures(detail_pairs)

    def run_inspect_flow(self) -> None:
        """Run discovery, execute tools, and emit JSON + context artifacts."""

        children = self._child_dirs()
        if not children:
            try:
                entries = sorted(p.name for p in self.root.iterdir() if p.is_dir())
            except OSError:
                entries = []
            preview = ", ".join(entries[:VISIBLE_DIR_PREVIEW_LIMIT])
            suffix = "" if len(entries) <= VISIBLE_DIR_PREVIEW_LIMIT else " …"
            msg = (
                "no child git repositories found"
                f" under {self.root} (visible dirs: {preview}{suffix})"
            )
            raise AssertionError(msg)

        repo_names = [str(child.relative_to(self.root)) for child in children]
        self._runtime_snapshot["discovered_repositories"] = repo_names
        _info(
            "visitor discovery:",
            f"found {len(repo_names)} repositories under {self.root}",
        )
        # Streaming run start
        self._emit_run_event(phase="start", repositories=repo_names)

        self._remove_legacy_json_reports()
        purged = self._purge_markdown_stragglers()
        if purged:
            _info("removed", purged, "legacy visitor Markdown report(s)")
        self.body(children=children)
        report_path, context_path = self._write_failure_reports()
        self.cleanup()
        self._finalize_run_result(
            report_path,
            markdown_path=None,
            context_path=context_path,
        )
        # Streaming run complete with overall summary
        try:
            overall_summary = self.generate_summary_report()
        except (KeyError, TypeError, ValueError) as exc:  # pragma: no cover - defensive
            overall_summary = {
                "error": "summary_generation_failed",
                "detail": str(exc),
            }
        self._emit_run_event(phase="complete", summary=overall_summary)

    @property
    def last_report_path(self) -> Path | None:
        return self._last_report_path

    @property
    def last_markdown_report_path(self) -> Path | None:
        return self._last_markdown_report_path

    @property
    def last_context_path(self) -> Path | None:
        return self._last_context_path

    @property
    def last_run_result(self) -> VisitorRunResult | None:
        return self._last_run_result


def _coerce_bool_flag(value: object, *, default: bool) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"1", "true", "yes", "on"}:
            return True
        if lowered in {"0", "false", "no", "off"}:
            return False
    return default


def _maybe_string(value: object) -> str | None:
    if isinstance(value, str) and value:
        return value
    return None


def _coerce_allowed_repositories(value: object) -> tuple[str, ...] | None:
    if not value or isinstance(value, (str, bytes, bytearray)):
        return None
    if not isinstance(value, Sequence):
        return None
    names: list[str] = []
    for entry in value:
        if isinstance(entry, str) and entry:
            normalized = _normalize_repo_name(entry)
            if normalized:
                names.append(normalized)
    if not names:
        return None
    return tuple(_dedupe_preserving_order(names))


def _coerce_file_allowlist(
    value: object,
) -> dict[str, tuple[str, ...]] | None:
    if not isinstance(value, Mapping):
        return None
    mapping = cast("Mapping[object, object]", value)
    allowlist: dict[str, tuple[str, ...]] = {}
    for repo_name_obj, rel_paths_obj in mapping.items():
        if not isinstance(repo_name_obj, str) or not repo_name_obj:
            continue
        normalized_repo = _normalize_repo_name(repo_name_obj)
        if not normalized_repo:
            continue
        if isinstance(rel_paths_obj, (str, bytes, bytearray)):
            rel_entries = [rel_paths_obj]
        elif isinstance(rel_paths_obj, Sequence):
            rel_entries = [str(item) for item in rel_paths_obj]
        else:
            continue
        normalized_files = [
            normalized
            for item in rel_entries
            if isinstance(item, str) and (normalized := _normalize_rel_path(item))
        ]
        if normalized_files:
            allowlist[normalized_repo] = tuple(
                _dedupe_preserving_order(normalized_files),
            )
    return allowlist or None


def _failure_payload(
    message: str,
    *,
    details: Mapping[str, object] | None = None,
    failure_messages: Sequence[str] | None = None,
) -> dict[str, object]:
    payload: dict[str, object] = {
        "status": "failure",
        "message": message,
    }
    if details:
        payload["details"] = {
            str(key): _json_ready(value) for key, value in dict(details).items()
        }
    if failure_messages:
        payload["failure_messages"] = [
            str(message)
            for message in failure_messages
            if isinstance(message, str) and message
        ]
    return payload


class _VisitorError(Exception):
    def __init__(
        self,
        message: str,
        *,
        details: Mapping[str, object] | None = None,
        failure_messages: Sequence[str] | None = None,
    ) -> None:
        super().__init__(message)
        self.payload = _failure_payload(
            message,
            details=details,
            failure_messages=failure_messages,
        )


@dataclass(frozen=True)
class _VisitorParameters:
    root_dir: str
    output_filename: str | None
    enable_cache: bool
    allowed_repositories: tuple[str, ...] | None
    file_allowlist: dict[str, tuple[str, ...]] | None


def _ensure_input_schema(payload: Mapping[str, object]) -> None:
    try:
        validate_payload(payload, INPUT_SCHEMA)
    except JSONSchemaValidationError as exc:
        detail_payload = _validation_error_details(exc)
        failure_message = "input payload failed validation"
        raise _VisitorError(
            failure_message,
            details=detail_payload,
        ) from exc


def _extract_parameters(payload: Mapping[str, object]) -> _VisitorParameters:
    parameters_obj = payload.get("parameters", {})
    if not isinstance(parameters_obj, Mapping):
        failure_message = "input payload failed validation"
        raise _VisitorError(
            failure_message,
            details={"error": "parameters must be a mapping"},
        )
    parameters = cast("Mapping[str, object]", parameters_obj)

    root_dir_obj = parameters.get("root_dir")
    root_dir = _maybe_string(root_dir_obj)
    if root_dir is None:
        failure_message = "input payload failed validation"
        raise _VisitorError(
            failure_message,
            details={"error": "parameters.root_dir must be a non-empty string"},
        )

    output_filename = _maybe_string(parameters.get("output_filename"))
    enable_cache = _coerce_bool_flag(
        parameters.get("enable_cache"),
        default=True,
    )
    allowed_repos = _coerce_allowed_repositories(parameters.get("allowed_repositories"))
    file_allowlist = _coerce_file_allowlist(parameters.get("file_allowlist"))

    return _VisitorParameters(
        root_dir=root_dir,
        output_filename=output_filename,
        enable_cache=enable_cache,
        allowed_repositories=allowed_repos,
        file_allowlist=file_allowlist,
    )


def _initialize_visitor(
    params: _VisitorParameters,
    *,
    ctx: object | None,
) -> x_cls_make_github_visitor_x:
    try:
        if params.output_filename is None:
            return x_cls_make_github_visitor_x(
                params.root_dir,
                ctx=ctx,
                enable_cache=params.enable_cache,
                allowed_repositories=params.allowed_repositories,
                file_allowlist=params.file_allowlist,
            )
        return x_cls_make_github_visitor_x(
            params.root_dir,
            output_filename=params.output_filename,
            ctx=ctx,
            enable_cache=params.enable_cache,
            allowed_repositories=params.allowed_repositories,
            file_allowlist=params.file_allowlist,
        )
    except AssertionError as exc:
        failure_message = "visitor initialisation failed"
        raise _VisitorError(
            failure_message,
            details={"error": str(exc)},
        ) from exc
    except Exception as exc:
        failure_message = "unexpected error while initialising visitor"
        raise _VisitorError(
            failure_message,
            details={"error": str(exc)},
        ) from exc


def _validate_output_payload(
    payload: Mapping[str, object],
    *,
    failure_messages: Sequence[str],
) -> None:
    try:
        validate_payload(payload, OUTPUT_SCHEMA)
    except JSONSchemaValidationError as exc:
        detail_payload = _validation_error_details(exc)
        failure_message = "generated output failed schema validation"
        raise _VisitorError(
            failure_message,
            details=detail_payload,
            failure_messages=failure_messages,
        ) from exc


def _stringify_report_path(value: object) -> str | None:
    if isinstance(value, Path):
        return str(value)
    if isinstance(value, str) and value:
        return value
    return None


def _build_success_payload(
    visitor: x_cls_make_github_visitor_x,
    result: VisitorRunResult,
    *,
    generated_at: datetime,
) -> dict[str, object]:
    detail_pairs = visitor.failure_detail_pairs()
    failure_entries = visitor.serialize_failures(detail_pairs)
    summary = visitor.generate_summary_report()
    runtime_snapshot = _json_ready(visitor.runtime_snapshot())
    tool_versions = _json_ready(visitor.tool_versions())
    failure_details_json = _json_ready(list(result.failure_details))

    return {
        "status": "failure" if result.had_failures else "success",
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at.isoformat(),
        "workspace_root": str(visitor.root),
        "report_path": _stringify_report_path(result.report_path),
        "markdown_report_path": _stringify_report_path(result.markdown_report_path),
        "context_path": _stringify_report_path(result.context_path),
        "had_failures": bool(result.had_failures),
        "skipped": bool(result.skipped),
        "failures": _json_ready(failure_entries),
        "failure_messages": list(result.failure_messages),
        "failure_details": failure_details_json,
        "summary": _json_ready(summary),
        "runtime": runtime_snapshot,
        "tool_versions": tool_versions,
    }


def _build_skip_payload(
    visitor: x_cls_make_github_visitor_x,
    *,
    generated_at: datetime,
) -> dict[str, object]:
    summary = visitor.generate_summary_report()
    runtime_snapshot = _json_ready(visitor.runtime_snapshot())
    tool_versions = _json_ready(visitor.tool_versions())
    payload: dict[str, object] = {
        "status": "skipped",
        "schema_version": SCHEMA_VERSION,
        "generated_at": generated_at.isoformat(),
        "workspace_root": str(visitor.root),
        "report_path": None,
        "markdown_report_path": None,
        "context_path": None,
        "had_failures": False,
        "skipped": True,
        "failures": [],
        "failure_messages": [],
        "failure_details": [],
        "summary": _json_ready(summary),
        "runtime": runtime_snapshot,
        "tool_versions": tool_versions,
    }
    return payload


def main_json(
    payload: Mapping[str, object],
    *,
    ctx: object | None = None,
) -> dict[str, object]:
    try:
        _ensure_input_schema(payload)
        params = _extract_parameters(payload)
        visitor = _initialize_visitor(params, ctx=ctx)

        generated_at = datetime.now(UTC)
        try:
            visitor.run_inspect_flow()
        except AssertionError as exc:
            message = str(exc)
            if "no child git repositories found" in message.lower():
                skip_payload = _build_skip_payload(
                    visitor,
                    generated_at=generated_at,
                )
                _validate_output_payload(skip_payload, failure_messages=())
                return skip_payload
            failure_message = "visitor run failed"
            raise _VisitorError(
                failure_message,
                details={"error": message},
            ) from exc
        except Exception as exc:
            failure_message = "unexpected error during visitor run"
            raise _VisitorError(
                failure_message,
                details={"error": str(exc)},
            ) from exc

        result = visitor.last_run_result
        if not isinstance(result, VisitorRunResult):
            result = VisitorRunResult(
                report_path=visitor.last_report_path,
                markdown_report_path=visitor.last_markdown_report_path,
                context_path=visitor.last_context_path,
                had_failures=False,
            )

        payload_out = _build_success_payload(
            visitor,
            result,
            generated_at=generated_at,
        )
    except _VisitorError as exc:
        return exc.payload
    else:
        _validate_output_payload(
            payload_out,
            failure_messages=result.failure_messages,
        )
        return payload_out


def _load_json_payload(path: str | None) -> Mapping[str, object]:
    if path:
        with Path(path).open("r", encoding="utf-8") as handle:
            raw_payload: object = json.load(handle)
    else:
        raw_payload = json.load(sys.stdin)
    if not isinstance(raw_payload, Mapping):
        message = "JSON payload must be an object"
        raise TypeError(message)
    mapping_payload = cast("Mapping[str, object]", raw_payload)
    normalized: dict[str, object] = {}
    for key, value in mapping_payload.items():
        normalized[str(key)] = value
    return normalized


def _flag_enabled(namespace: argparse.Namespace, name: str) -> bool:
    """Return True when the argparse namespace defines a truthy flag."""

    return bool(cast("object", getattr(namespace, name, False)))


def _run_json_cli(args: Sequence[str]) -> None:
    parser = argparse.ArgumentParser(description="x_make_github_visitor_x JSON runner")
    parser.add_argument(
        "--json",
        action="store_true",
        help="Read JSON payload from stdin",
    )
    parser.add_argument(
        "--json-file",
        type=str,
        help="Path to JSON payload file",
    )
    parser.add_argument(
        "--quick",
        action="store_true",
        help="Engage quick mode (skip tool execution; repo/file discovery only).",
    )
    parser.add_argument(
        "--skip-content-hash",
        action="store_true",
        help="Skip computing repository content hashes (use path-derived placeholder).",
    )
    parser.add_argument(
        "--skip-tools",
        action="store_true",
        help="Run only lightweight pyright check instead of full toolchain.",
    )
    parsed = parser.parse_args(list(args))

    json_attr: object = getattr(parsed, "json", False)
    json_flag: bool = bool(json_attr)
    json_file_obj: object = getattr(parsed, "json_file", None)
    if isinstance(json_file_obj, str):
        json_file: str | None = json_file_obj
    else:
        json_file = None

    if not json_flag and json_file is None:
        parser.error("JSON input required. Use --json for stdin or --json-file <path>.")

    # Apply acceleration flags via environment before running
    quick_flag = _flag_enabled(parsed, "quick")
    if quick_flag:
        os.environ["VISITOR_QUICK_MODE"] = "1"
    skip_hash_flag = _flag_enabled(parsed, "skip_content_hash")
    if skip_hash_flag:
        os.environ["VISITOR_SKIP_CONTENT_HASH"] = "1"
    skip_tools_flag = _flag_enabled(parsed, "skip_tools")
    if skip_tools_flag:
        os.environ["VISITOR_SKIP_TOOLS"] = "1"

    payload = _load_json_payload(json_file)
    result = main_json(payload)
    json.dump(result, sys.stdout, indent=2)
    sys.stdout.write("\n")


def _workspace_root() -> str:
    here = Path(__file__).resolve()
    for anc in here.parents:
        if (anc / ".git").exists():  # repo root
            return str(anc.parent)
    # Fallback: three levels up
    return str(here.parent.parent.parent)


def init_name(
    root_dir: str | Path,
    *,
    output_filename: str | None = None,
    ctx: object | None = None,
    enable_cache: bool = True,
    progress_writer: RepoProgressReporter | None = None,
) -> x_cls_make_github_visitor_x:
    if output_filename is None:
        return x_cls_make_github_visitor_x(
            root_dir,
            ctx=ctx,
            enable_cache=enable_cache,
            progress_writer=progress_writer,
        )
    return x_cls_make_github_visitor_x(
        root_dir,
        output_filename=output_filename,
        ctx=ctx,
        enable_cache=enable_cache,
        progress_writer=progress_writer,
    )


def init_main(
    ctx: object | None = None,
    *,
    enable_cache: bool = True,
) -> x_cls_make_github_visitor_x:
    """Initialize the visitor using dynamic workspace root (parent of this repo)."""
    return init_name(_workspace_root(), ctx=ctx, enable_cache=enable_cache)


def run_workspace_inspection(
    root_dir: str | Path,
    *,
    ctx: object | None = None,
    enable_cache: bool = True,
    progress_writer: RepoProgressReporter | None = None,
) -> VisitorRunResult:
    """Run the full inspection pipeline for the provided workspace root.

    Returns a :class:`VisitorRunResult` describing the report path and any
    captured failures. When no child git repositories are discovered the
    function logs the outcome and marks the result as skipped.
    """

    try:
        visitor = init_name(
            root_dir,
            ctx=ctx,
            enable_cache=enable_cache,
            progress_writer=progress_writer,
        )
    except (RuntimeError, ValueError, TypeError) as err:  # pragma: no cover
        # init guard
        message = f"x_make_github_visitor instantiate failed: {err}"
        raise AssertionError(message) from err

    _info(
        "Running x_make_github_visitor against cloned repos",
        f"root={Path(root_dir)!s} ...",
    )

    try:
        visitor.run_inspect_flow()
    except AssertionError as err:
        lowered_error = str(err).lower()
        if "no child git repositories found" in lowered_error:
            _info(
                "Visitor skipped: no child git repositories present at root;",
                "continuing orchestrator flow",
            )
            return VisitorRunResult(
                report_path=None,
                had_failures=False,
                skipped=True,
            )
        raise
    except (RuntimeError, ValueError) as err:
        message = f"x_make_github_visitor run failed: {err}"
        raise AssertionError(message) from err

    result = visitor.last_run_result
    if isinstance(result, VisitorRunResult):
        return result

    report_path = visitor.last_report_path
    return VisitorRunResult(
        report_path=report_path,
        markdown_report_path=visitor.last_markdown_report_path,
        context_path=visitor.last_context_path,
        had_failures=False,
    )


__all__ = [
    "SCHEMA_VERSION",
    "init_main",
    "init_name",
    "main_json",
    "run_workspace_inspection",
    "x_cls_make_github_visitor_x",
]


if __name__ == "__main__":
    # Support both JSON payload mode and acceleration CLI flags.
    if any(arg in {"--json", "--json-file"} for arg in sys.argv[1:]):
        _run_json_cli(sys.argv[1:])
    else:
        parser = argparse.ArgumentParser(
            description=(
                "x_make_github_visitor_x workspace inspection runner "
                "with acceleration flags"
            ),
        )
        parser.add_argument(
            "--quick",
            action="store_true",
            help="Engage quick mode (skip tool execution; repo/file discovery only).",
        )
        parser.add_argument(
            "--skip-content-hash",
            action="store_true",
            help=(
                "Skip computing repository content hashes (use path-"
                "derived placeholder)."
            ),
        )
        parser.add_argument(
            "--skip-tools",
            action="store_true",
            help="Run only lightweight pyright check instead of full toolchain.",
        )
        parsed, _remaining = parser.parse_known_args(sys.argv[1:])

        if _flag_enabled(parsed, "quick"):
            os.environ["VISITOR_QUICK_MODE"] = "1"
        if _flag_enabled(parsed, "skip_content_hash"):
            os.environ["VISITOR_SKIP_CONTENT_HASH"] = "1"
        if _flag_enabled(parsed, "skip_tools"):
            os.environ["VISITOR_SKIP_TOOLS"] = "1"

        inst = init_main()
        inst.run_inspect_flow()
        summary = inst.generate_summary_report()
        overall_raw = summary.get("overall_stats", {})
        overall: Mapping[str, object]
        if isinstance(overall_raw, Mapping):
            overall = cast("Mapping[str, object]", overall_raw)
        else:
            overall = {}

        hits = _coerce_exit_code(overall.get("cache_hits", 0)) or 0
        total = _coerce_exit_code(overall.get("total_tools_run", 0)) or 0
        ratio = (hits / total * 100.0) if total else 0.0

        report_path = inst.last_report_path
        if report_path is not None:
            _info("visitor JSON report saved to:", report_path)
        else:
            _info("visitor JSON report path unavailable")

        summary_line = (
            f"processed {summary.get('total_repos', 0)} repositories "
            f"| cache hits: {hits}/{total} ({ratio:.1f}%)"
        )
        _info(summary_line)
