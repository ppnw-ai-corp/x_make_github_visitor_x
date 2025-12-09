from __future__ import annotations

# ruff: noqa: S101
import hashlib
import json
from typing import TYPE_CHECKING

from x_make_github_visitor_x.json_contracts import VISITOR_REPORT_SCHEMA_VERSION
from x_make_github_visitor_x.report_validator import (
    compute_payload_checksum,
    validate_report_path,
    validate_reports_dir,
)

if TYPE_CHECKING:
    from pathlib import Path


def _write_sample_report(tmp_path: Path) -> Path:
    reports_dir = tmp_path / "reports"
    artifacts_dir = reports_dir / "artifacts" / "visitor_failures_20250101_000000"
    workspace_root = tmp_path / "workspace"
    repo_path = workspace_root / "demo"
    artifacts_dir.mkdir(parents=True)
    workspace_root.mkdir()
    repo_path.mkdir()

    stdout_path = artifacts_dir / "0001_demo_ruff_stdout.log"
    stderr_path = artifacts_dir / "0001_demo_ruff_stderr.log"
    stdout_text = "stdout line\n"
    stderr_text = "stderr line\n"
    stdout_path.write_text(stdout_text, encoding="utf-8")
    stderr_path.write_text(stderr_text, encoding="utf-8")

    stdout_bytes = stdout_path.read_bytes()
    stderr_bytes = stderr_path.read_bytes()
    stdout_digest = hashlib.sha256(stdout_bytes).hexdigest()
    stderr_digest = hashlib.sha256(stderr_bytes).hexdigest()

    summary = {
        "timestamp": "2025-11-24T00:00:00Z",
        "total_repos": 1,
        "overall_stats": {
            "cache_hits": 0,
            "cache_misses": 1,
            "failed_tools": 1,
            "total_tools_run": 1,
            "had_failures": True,
        },
        "repos": {
            "demo": {
                "repo_hash": "abc",
                "tools": {
                    "ruff": {
                        "exit": 1,
                        "cached": False,
                        "timed_out": False,
                    },
                },
                "cached": 0,
                "failed": 1,
            },
        },
        "fast_paths": {},
        "fast_paths_active": [],
    }

    payload = {
        "schema_version": VISITOR_REPORT_SCHEMA_VERSION,
        "generated_at": "2025-11-24T00:00:00Z",
        "workspace_root": str(workspace_root),
        "runtime": {"workspace_root": str(workspace_root)},
        "tool_versions": {"ruff": "0.6.0"},
        "summary": summary,
        "failures": [
            {
                "repo": "demo",
                "tool": "ruff",
                "summary": "ruff failed",
                "message": "ruff failed",
                "command": "ruff .",
                "exit": "exit 1",
                "repo_path": str(repo_path),
                "tool_version": "0.6.0",
                "captured_at": "2025-11-24T00:00:00Z",
                "suggested_action": "Investigate",
                "stdout_preview": stdout_text.strip(),
                "stderr_preview": stderr_text.strip(),
                "stdout_artifact": {
                    "path": str(stdout_path),
                    "sha256": stdout_digest,
                    "bytes": len(stdout_bytes),
                },
                "stderr_artifact": {
                    "path": str(stderr_path),
                    "sha256": stderr_digest,
                    "bytes": len(stderr_bytes),
                },
                "detail": {"repo": "demo"},
            },
        ],
        "artifact_root": str(artifacts_dir),
    }
    payload["payload_checksum"] = compute_payload_checksum(payload)

    reports_dir.mkdir(exist_ok=True)
    report_path = reports_dir / "visitor_failures_20250101_000000.json"
    with report_path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, indent=2)
    digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
    sidecar = report_path.with_suffix(".json.sha256")
    sidecar.write_text(f"{digest}  {report_path.name}\n", encoding="utf-8")
    return report_path


def test_validate_reports_dir_passes(tmp_path: Path) -> None:
    report_path = _write_sample_report(tmp_path)
    outcome = validate_reports_dir(report_path.parent)
    assert outcome.errors == []
    assert outcome.checked == [report_path]


def test_validate_report_path_detects_sidecar_regressions(tmp_path: Path) -> None:
    report_path = _write_sample_report(tmp_path)
    assert validate_report_path(report_path) == []

    checksum_path = report_path.with_suffix(".json.sha256")
    checksum_path.write_text("deadbeef invalid\n", encoding="utf-8")

    errors = validate_report_path(report_path)
    assert errors
    assert any("checksum sidecar" in message for message in errors)


def test_validate_reports_dir_detects_missing_artifact(tmp_path: Path) -> None:
    report_path = _write_sample_report(tmp_path)
    artifact_dir = report_path.parent / "artifacts" / "visitor_failures_20250101_000000"
    missing = next(artifact_dir.glob("*_stdout.log"))
    missing.unlink()

    outcome = validate_reports_dir(report_path.parent)
    assert outcome.errors
    assert any("stdout_artifact" in message for _, message in outcome.errors)
