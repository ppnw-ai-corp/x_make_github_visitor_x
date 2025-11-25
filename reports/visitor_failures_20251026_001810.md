# Visitor TODO Report

- Generated: 2025-10-26T00:18:10.058607+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 2
- Recorded failures: 2

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-26T00:15:46.505377+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-26 00:15:45.038610+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-26 00:15:46.228986+00:00
    @@ -34,10 +34,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-26T00:17:42.599340+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py	2025-10-26 00:11:46.278410+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py	2025-10-26 00:17:41.849389+00:00
    @@ -24,10 +24,12 @@
         if not isinstance(payload_obj, dict):
             message = f"Fixture payload must be an object: {name}"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_pypi_x\publish_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.
