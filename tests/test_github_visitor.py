from __future__ import annotations

# ruff: noqa: S101
import hashlib
import json
import pathlib
from collections.abc import Mapping
from typing import cast

from x_make_github_visitor_x import x_cls_make_github_visitor_x


def _create_repo(root: pathlib.Path, name: str) -> pathlib.Path:
    repo = root / name
    repo.mkdir(parents=True)
    (repo / ".git").mkdir()
    return repo


class DummyVisitor(x_cls_make_github_visitor_x):
    """Test double that injects predetermined visitor results."""

    def __init__(  # noqa: PLR0913
        self,
        root_dir: pathlib.Path,
        *,
        reports_dir: pathlib.Path,
        tool_reports: dict[str, dict[str, object]],
        failure_messages: list[str],
        failure_details: list[dict[str, object]],
        had_failures: bool,
        run_started: str,
        run_completed: str,
    ) -> None:
        super().__init__(root_dir, enable_cache=False)
        self._preset_reports = tool_reports
        self._preset_failure_messages = failure_messages
        self._preset_failure_details = failure_details
        self._preset_had_failures = had_failures
        self._preset_run_started = run_started
        self._preset_run_completed = run_completed
        self._reports_dir = reports_dir

    def body(self, *, children: object | None = None) -> None:
        _ = children
        self._tool_reports = self._preset_reports
        self._failure_messages = self._preset_failure_messages
        self._failure_details = self._preset_failure_details
        self._last_run_failures = self._preset_had_failures
        self._runtime_snapshot["run_started_at"] = self._preset_run_started
        self._runtime_snapshot["run_completed_at"] = self._preset_run_completed


def test_run_inspect_flow_writes_json_report_and_preserves_order(  # noqa: PLR0915
    tmp_path: pathlib.Path,
) -> None:
    workspace = pathlib.Path(tmp_path) / "workspace"
    workspace.mkdir()
    repo_a = _create_repo(workspace, "repo_a")
    repo_b = _create_repo(workspace, "repo_b")

    reports_dir = pathlib.Path(tmp_path) / "reports"

    tool_reports: dict[str, dict[str, object]] = {
        "repo_a": {
            "repo_hash": "hash-a",
            "timestamp": "2025-10-12T12:15:00+00:00",
            "files": ["a.py"],
            "tool_reports": {
                "ruff_check": {
                    "exit": 1,
                    "cached": False,
                    "stdout": "lint error",
                    "stderr": "E999 broken",
                }
            },
        },
        "repo_b": {
            "repo_hash": "hash-b",
            "timestamp": "2025-10-12T12:16:00+00:00",
            "files": ["b.py"],
            "tool_reports": {
                "mypy": {
                    "exit": 2,
                    "cached": False,
                    "stdout": "",
                    "stderr": "error: incompatible types",
                }
            },
        },
    }
    failure_messages = [
        "ruff_check failed for repo_a (exit 1)",
        "mypy failed for repo_b (exit 2)",
    ]
    failure_details: list[dict[str, object]] = [
        {
            "repo": "repo_a",
            "repo_path": str(repo_a),
            "tool": "ruff_check",
            "cmd_display": "python -m ruff check .",
            "exit": 1,
            "stdout": "lint error",
            "stderr": "E999 broken",
            "ended_at": "2025-10-12T12:15:00+00:00",
            "tool_version": "ruff 0.5.0",
        },
        {
            "repo": "repo_b",
            "repo_path": str(repo_b),
            "tool": "mypy",
            "cmd_display": "python -m mypy . --strict",
            "exit": 2,
            "stdout": "",
            "stderr": "error: incompatible types",
            "ended_at": "2025-10-12T12:16:00+00:00",
            "tool_version": "mypy 1.10.0",
        },
    ]

    visitor = DummyVisitor(
        workspace,
        reports_dir=reports_dir,
        tool_reports=tool_reports,
        failure_messages=failure_messages,
        failure_details=failure_details,
        had_failures=True,
        run_started="2025-10-12T12:00:00+00:00",
        run_completed="2025-10-12T12:20:00+00:00",
    )

    visitor.run_inspect_flow()

    result = visitor.last_run_result
    assert result is not None
    assert result.had_failures is True
    assert list(result.failure_messages) == failure_messages
    result_details = [dict(detail) for detail in result.failure_details]
    for detail in result_details:
        assert "stdout" not in detail
        assert "stderr" not in detail
    assert [detail.get("repo") for detail in result_details] == [
        entry["repo"] for entry in failure_details
    ]
    markdown_path = visitor.last_markdown_report_path
    assert markdown_path is not None
    assert markdown_path.suffix == ".md"
    assert result.markdown_report_path == markdown_path

    report_path = visitor.last_report_path
    assert report_path is not None
    assert report_path.suffix == ".json"
    assert result.report_path == report_path
    payload_text = report_path.read_text(encoding="utf-8")
    report_data_raw = cast("object", json.loads(payload_text))
    assert isinstance(report_data_raw, dict)
    report_data = cast("dict[str, object]", report_data_raw)
    payload_checksum = report_data.get("payload_checksum")
    assert isinstance(payload_checksum, str)
    payload_copy = dict(report_data)
    payload_copy.pop("payload_checksum", None)
    canonical = json.dumps(payload_copy, sort_keys=True, separators=(",", ":")).encode(
        "utf-8"
    )
    assert payload_checksum == hashlib.sha256(canonical).hexdigest()

    artifact_root_value = report_data.get("artifact_root")
    assert isinstance(artifact_root_value, str)
    artifact_root = pathlib.Path(artifact_root_value)
    assert artifact_root.exists()

    failures_value = report_data.get("failures")
    assert isinstance(failures_value, list)
    failure_entries = cast("list[object]", failures_value)
    failures: list[dict[str, object]] = []
    for entry in failure_entries:
        assert isinstance(entry, dict)
        typed_entry = cast("dict[str, object]", entry)
        failures.append(typed_entry)

    repo_tool_pairs: list[tuple[str, str]] = []
    for entry in failures:
        repo = entry.get("repo")
        tool = entry.get("tool")
        assert isinstance(repo, str)
        assert isinstance(tool, str)
        repo_tool_pairs.append((repo, tool))
    assert repo_tool_pairs == [("repo_a", "ruff_check"), ("repo_b", "mypy")]

    command_a = failures[0].get("command")
    command_b = failures[1].get("command")
    assert isinstance(command_a, str)
    assert isinstance(command_b, str)
    assert command_a == "python -m ruff check ."
    assert command_b == "python -m mypy . --strict"

    suggested = failures[0].get("suggested_action")
    assert suggested == "Investigate"

    stdout_preview = failures[0].get("stdout_preview")
    assert stdout_preview == "lint error"

    stderr_preview = failures[1].get("stderr_preview")
    assert isinstance(stderr_preview, str)
    assert "incompatible types" in stderr_preview

    stdout_artifact_entry = failures[0].get("stdout_artifact")
    assert isinstance(stdout_artifact_entry, dict)
    stdout_artifact_path = pathlib.Path(stdout_artifact_entry.get("path", ""))
    assert stdout_artifact_path.exists()
    stdout_bytes = stdout_artifact_path.read_bytes()
    assert stdout_artifact_entry.get("bytes") == len(stdout_bytes)
    assert stdout_artifact_entry.get("sha256") == hashlib.sha256(stdout_bytes).hexdigest()

    checksum_path = report_path.with_suffix(".json.sha256")
    assert checksum_path.exists()
    recorded_digest = checksum_path.read_text(encoding="utf-8").split()[0]
    actual_digest = hashlib.sha256(report_path.read_bytes()).hexdigest()
    assert recorded_digest == actual_digest


def test_run_inspect_flow_creates_empty_failure_report(
    tmp_path: pathlib.Path,
) -> None:
    workspace = pathlib.Path(tmp_path) / "workspace"
    workspace.mkdir()
    _create_repo(workspace, "repo_clean")

    reports_dir = pathlib.Path(tmp_path) / "reports"

    tool_reports: dict[str, dict[str, object]] = {
        "repo_clean": {
            "repo_hash": "hash-clean",
            "timestamp": "2025-10-12T10:01:00+00:00",
            "files": ["ok.py"],
            "tool_reports": {
                "ruff_check": {
                    "exit": 0,
                    "cached": False,
                    "stdout": "",
                    "stderr": "",
                }
            },
        }
    }

    visitor = DummyVisitor(
        workspace,
        reports_dir=reports_dir,
        tool_reports=tool_reports,
        failure_messages=[],
        failure_details=[],
        had_failures=False,
        run_started="2025-10-12T10:00:00+00:00",
        run_completed="2025-10-12T10:01:00+00:00",
    )

    visitor.run_inspect_flow()

    report_path = visitor.last_report_path
    assert report_path is not None
    payload_text = report_path.read_text(encoding="utf-8")
    report_data_raw = cast("object", json.loads(payload_text))
    assert isinstance(report_data_raw, dict)
    report_data = cast("dict[str, object]", report_data_raw)
    failures_value = report_data.get("failures")
    assert isinstance(failures_value, list)
    failures = cast("list[object]", failures_value)
    assert failures == []

    assert report_data.get("artifact_root") is None
    assert isinstance(report_data.get("payload_checksum"), str)

    summary = report_data.get("summary")
    assert isinstance(summary, Mapping)
    summary_map = cast("Mapping[str, object]", summary)
    assert summary_map.get("total_repos") == 1

    markdown_path = visitor.last_markdown_report_path
    assert markdown_path is not None
    text = markdown_path.read_text(encoding="utf-8")
    assert "All tools succeeded" in text


def test_workspace_root_can_be_git_repo(tmp_path: pathlib.Path) -> None:
    workspace = pathlib.Path(tmp_path)
    (workspace / ".git").mkdir()
    _create_repo(workspace, "child_repo")

    visitor = x_cls_make_github_visitor_x(workspace)
    assert visitor.root == workspace


def test_markdown_todo_emission(tmp_path: pathlib.Path) -> None:
    workspace = pathlib.Path(tmp_path) / "workspace"
    workspace.mkdir()
    repo = _create_repo(workspace, "repo_markdown")

    reports_dir = pathlib.Path(tmp_path) / "reports"

    tool_reports: dict[str, dict[str, object]] = {
        "repo_markdown": {
            "repo_hash": "hash-md",
            "timestamp": "2025-10-12T12:17:00+00:00",
            "files": ["m.py"],
            "tool_reports": {
                "pyright": {
                    "exit": 3,
                    "cached": False,
                    "stdout": "",
                    "stderr": "Type error!",
                }
            },
        }
    }
    failure_messages = ["pyright failed for repo_markdown (exit 3)"]
    failure_details = [
        {
            "repo": "repo_markdown",
            "repo_path": str(repo),
            "tool": "pyright",
            "cmd_display": "python -m pyright .",
            "exit": 3,
            "stdout": "",
            "stderr": "Type error!",
            "ended_at": "2025-10-12T12:17:00+00:00",
            "tool_version": "pyright 1.2.3",
        }
    ]

    visitor = DummyVisitor(
        workspace,
        reports_dir=reports_dir,
        tool_reports=tool_reports,
        failure_messages=failure_messages,
        failure_details=failure_details,
        had_failures=True,
        run_started="2025-10-12T12:15:00+00:00",
        run_completed="2025-10-12T12:18:00+00:00",
    )

    visitor.run_inspect_flow()

    markdown_path = visitor.last_markdown_report_path
    assert markdown_path is not None
    text = markdown_path.read_text(encoding="utf-8")
    assert "Visitor TODO Report" in text
    assert "repo_markdown" in text
    assert "pyright" in text
    assert "Suggested action" in text
