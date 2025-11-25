# Visitor TODO Report

- Generated: 2025-11-18T22:40:15.431521+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 3
- Recorded failures: 3

- [ ] x_make_common_x — black
  - Summary: black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-18T22:38:27.823685+00:00 dur…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-18T22:38:29.515241+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_common_x\ledger.py	2025-11-18 22:35:28.102558+00:00
    +++ C:\x_runner_x\x_make_common_x\ledger.py	2025-11-18 22:38:29.172753+00:00
    @@ -15,13 +15,11 @@
     class LedgerEvent:
         """Structured event suitable for immutable ledgers."""
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_common_x\ledger.py
    would reformat C:\x_runner_x\x_make_common_x\detect\entrypoints.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 18 files would be left unchanged.

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.5
  - Captured: 2025-11-18T22:38:29.754686+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.5
  - Captured: 2025-11-18T22:38:27.819288+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …
