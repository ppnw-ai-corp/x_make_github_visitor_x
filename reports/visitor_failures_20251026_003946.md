# Visitor TODO Report

- Generated: 2025-10-26T00:39:46.801980+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 3
- Recorded failures: 3

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-26T00:39:41.549960+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-26 00:39:39.336264+00:00
    +++ C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-26 00:39:41.351007+00:00
    @@ -25,17 +25,13 @@
     
     class _WinRegModule(Protocol):
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\publish_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-26T00:39:41.700748+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N802 Function name `OpenKey` should be lowercase
      --> publish_flow.py:30:9
       |
    28 |     REG_EXPAND_SZ: int
    29 |
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-26T00:39:39.352079+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N802 Function name `OpenKey` should be lowercase
      --> publish_flow.py:30:9
       |
    28 |     REG_EXPAND_SZ: int
    29 |
    …
