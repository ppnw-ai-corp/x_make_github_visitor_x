from __future__ import annotations

import json
from pathlib import Path

from x_make_github_visitor_x.backfill_markdown_reports import backfill_markdown_reports


def _write_report(path: Path, payload: dict[str, object]) -> None:
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def test_backfill_generates_markdown(tmp_path: Path) -> None:
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
            }
        ],
    }
    _write_report(json_path, payload)

    outcome = backfill_markdown_reports(reports_dir)
    markdown_path = json_path.with_suffix(".md")
    assert markdown_path.exists()
    text = markdown_path.read_text(encoding="utf-8")
    assert "Visitor TODO Report" in text
    assert "repo_a" in text
    assert "ruff" in text
    assert len(outcome.created) == 1
    assert not outcome.errors

    second = backfill_markdown_reports(reports_dir)
    assert len(second.created) == 0
    assert len(second.skipped) == 1

    payload["failures"][0]["summary"] = "updated lint failure"  # type: ignore[index]
    _write_report(json_path, payload)
    forced = backfill_markdown_reports(reports_dir, force=True)
    assert len(forced.created) == 1
    updated_text = markdown_path.read_text(encoding="utf-8")
    assert "updated lint failure" in updated_text
