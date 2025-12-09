from __future__ import annotations

# ruff: noqa: S101
import json
from typing import TYPE_CHECKING

from x_make_github_visitor_x.backfill_markdown_reports import backfill_markdown_reports

if TYPE_CHECKING:
    from pathlib import Path


def _write_report(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def test_backfill_is_noop(tmp_path: Path) -> None:
    reports_dir = tmp_path / "reports"
    reports_dir.mkdir()

    json_path = reports_dir / "visitor_failures_20250101_010203.json"
    payload: dict[str, object] = {
        "workspace_root": "C:/workspace",
        "generated_at": "2025-01-01T01:02:03+00:00",
        "summary": {
            "total_repos": 1,
            "overall_stats": {"failed_tools": 1},
        },
        "failures": [
            {
                "repo": "repo_a",
                "tool": "ruff",
                "summary": "lint failure",
                "message": "ruff failed",
                "command": "python -m ruff check .",
                "exit": "exit 1",
                "repo_path": "C:/workspace/repo_a",
                "tool_version": "ruff 0.5.0",
                "captured_at": "2025-01-01T01:00:00+00:00",
                "suggested_action": "Fix lint",
                "stdout_preview": "stdout",
                "stderr_preview": "stderr",
            },
        ],
    }
    _write_report(json_path, payload)

    outcome = backfill_markdown_reports(reports_dir)
    markdown_path = json_path.with_suffix(".md")
    assert not markdown_path.exists()
    assert len(outcome.created) == 0
    assert len(outcome.skipped) == 1
    assert outcome.skipped[0] == markdown_path
    assert not outcome.errors

    second = backfill_markdown_reports(reports_dir)
    assert len(second.created) == 0
    assert len(second.skipped) == 1

    payload["failures"][0]["summary"] = "updated lint failure"  # type: ignore[index]
    _write_report(json_path, payload)
    forced = backfill_markdown_reports(reports_dir, force=True)
    assert len(forced.created) == 0
    assert len(forced.skipped) == 1
