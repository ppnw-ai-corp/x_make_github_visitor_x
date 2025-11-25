# Visitor TODO Report

- Generated: 2025-11-19T00:06:16.358574+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 3
- Recorded failures: 3

- [ ] x_make_common_x — black
  - Summary: black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: c:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-19T00:05:48.803766+00:00 dur…
  - Command: c:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-19T00:05:50.974604+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_common_x\detect\entrypoints.py	2025-11-18 23:58:48.168517+00:00
    +++ C:\x_runner_x\x_make_common_x\detect\entrypoints.py	2025-11-19 00:05:50.579601+00:00
    @@ -121,11 +121,13 @@
         if "fire" in text:
             hints.append("fire")
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_common_x\detect\entrypoints.py
    would reformat C:\x_runner_x\x_make_common_x\ledger.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 18 files would be left unchanged.

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: c:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: c:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.5
  - Captured: 2025-11-19T00:05:51.190475+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: c:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: c:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.5
  - Captured: 2025-11-19T00:05:48.795339+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …
