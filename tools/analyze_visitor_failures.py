from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from collections.abc import Sequence


WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = WORKSPACE_ROOT / "artifacts" / "lint_runs" / "visitor_run_latest.log"


def _parse_failure_header(
    lines: Sequence[str],
    idx: int,
) -> tuple[str, str, int]:
    line = lines[idx]
    before, _, after = line.partition(":")
    tool = before.strip()
    remainder = after.split("failure in", 1)[-1].strip()
    repo_parts = [remainder]
    lookahead = idx + 1
    while ";" not in "".join(repo_parts) and lookahead < len(lines):
        repo_parts.append(lines[lookahead].strip())
        lookahead += 1
    repo_full = "".join(repo_parts)
    repo = repo_full.split(";", 1)[0].strip()
    return tool, repo, lookahead


def _extract_reason(lines: Sequence[str], start: int) -> tuple[str, int]:
    probe = start
    while probe < len(lines) and not lines[probe].startswith("stdout:"):
        probe += 1
    if probe >= len(lines):
        return "", probe
    detail = probe + 1
    while detail < len(lines) and not lines[detail].strip():
        detail += 1
    reason = lines[detail].strip() if detail < len(lines) else ""
    return reason, probe + 1


def _gather_failures(lines: Sequence[str]) -> list[tuple[str, str, str]]:
    failures: list[tuple[str, str, str]] = []
    idx = 0
    while idx < len(lines):
        if "failure in" not in lines[idx]:
            idx += 1
            continue
        tool, repo, header_end = _parse_failure_header(lines, idx)
        reason, next_idx = _extract_reason(lines, header_end)
        failures.append((tool, repo, reason))
        idx = max(next_idx, header_end + 1)
    return failures


def main() -> None:
    lines = LOG_PATH.read_text(encoding="utf-16", errors="ignore").splitlines()
    failures = _gather_failures(lines)

    sys.stdout.write(f"Total failures: {len(failures)}\n")
    per_repo: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for tool, repo, reason in failures:
        per_repo[repo].append((tool, reason))

    for repo in sorted(per_repo):
        sys.stdout.write(f"--- {repo}\n")
        for tool, reason in per_repo[repo]:
            sys.stdout.write(f"   {tool}: {reason}\n")


if __name__ == "__main__":
    main()
