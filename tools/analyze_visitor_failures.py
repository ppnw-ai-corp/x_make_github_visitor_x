from __future__ import annotations

from collections import defaultdict
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = WORKSPACE_ROOT / "artifacts" / "lint_runs" / "visitor_run_latest.log"


def main() -> None:
    lines = LOG_PATH.read_text(encoding="utf-16", errors="ignore").splitlines()
    failures: list[tuple[str, str, str]] = []
    idx = 0
    while idx < len(lines):
        line = lines[idx]
        if "failure in" not in line:
            idx += 1
            continue
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
        idx = lookahead - 1
        reason = ""
        probe = idx + 1
        while probe < len(lines) and not lines[probe].startswith("stdout:"):
            probe += 1
        if probe < len(lines):
            detail = probe + 1
            while detail < len(lines) and not lines[detail].strip():
                detail += 1
            if detail < len(lines):
                reason = lines[detail].strip()
        failures.append((tool, repo, reason))
        idx = probe + 1

    print(f"Total failures: {len(failures)}")
    per_repo: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for tool, repo, reason in failures:
        per_repo[repo].append((tool, reason))

    for repo in sorted(per_repo):
        print(f"--- {repo}")
        for tool, reason in per_repo[repo]:
            print(f"   {tool}: {reason}")


if __name__ == "__main__":
    main()
