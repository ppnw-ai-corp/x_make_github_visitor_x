"""Utility to summarize repos with failures from visitor_run_latest.log."""

from __future__ import annotations

import re
from collections import OrderedDict
from pathlib import Path

WORKSPACE_ROOT = Path(__file__).resolve().parents[2]
LOG_PATH = WORKSPACE_ROOT / "artifacts" / "lint_runs" / "visitor_run_latest.log"


def main() -> None:
    text = LOG_PATH.read_text(encoding="utf-16-le")
    pattern = re.compile(r"'repo': '([^']+)'")
    order: OrderedDict[str, int] = OrderedDict()
    for match in pattern.finditer(text):
        repo = match.group(1).replace("\r", "").replace("\n", "")
        order.setdefault(repo, 0)
        order[repo] += 1
    print(f"unique repos with failures: {len(order)}")
    for idx, (repo, count) in enumerate(order.items(), start=1):
        print(f"{idx:2d}. {repo} ({count} hits)")


if __name__ == "__main__":
    main()
