from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


@dataclass(slots=True)
class BackfillOutcome:
    created: list[Path]
    skipped: list[Path]
    errors: list[tuple[Path, str]]


def _default_reports_dir() -> Path:
    return Path(__file__).resolve().parent / "reports"


def backfill_markdown_reports(
    reports_dir: Path,
    *,
    force: bool = False,
    limit: int | None = None,
) -> BackfillOutcome:
    """Legacy helper retained for compatibility; Markdown generation is disabled."""

    del force  # Markdown artifacts are no longer produced

    reports_path = reports_dir.resolve()
    if not reports_path.exists():
        message = f"reports directory does not exist: {reports_path}"
        raise FileNotFoundError(message)

    json_files = sorted(reports_path.glob("visitor_failures_*.json"))
    if limit is not None and limit >= 0:
        json_files = json_files[:limit]

    skipped = [json_path.with_suffix(".md") for json_path in json_files]
    return BackfillOutcome(created=[], skipped=skipped, errors=[])


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="x_make_github_visitor_backfill",
        description=("Legacy compatibility shim for the retired Markdown backfill."),
    )
    parser.add_argument(
        "--reports-dir",
        type=Path,
        default=_default_reports_dir(),
        help=(
            "Path containing visitor_failures_*.json files"
            " (defaults to package reports dir)."
        ),
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Historical flag (no longer applicable).",
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
        f"errors={len(outcome.errors)} (markdown disabled)"
    )
    print(summary_line)
    if outcome.errors:
        for path, message in outcome.errors:
            print(f"ERROR {path}: {message}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    raise SystemExit(main())
