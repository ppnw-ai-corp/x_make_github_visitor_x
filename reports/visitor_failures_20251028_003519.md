# Visitor TODO Report

- Generated: 2025-10-28T00:35:19.606781+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 17
- Failing tools: 15
- Recorded failures: 15

- [ ] x_legatus_acta_schedae_x — black
  - Summary: black failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-28T00:30:5…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-28T00:30:52.440986+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_plugin_calendar_sync.py	2025-10-28 00:28:46.851354+00:00
    +++ C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_plugin_calendar_sync.py	2025-10-28 00:30:51.699568+00:00
    @@ -27,10 +27,12 @@
         from collections.abc import Iterable
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_plugin_calendar_sync.py
    would reformat C:\x_runner_x\x_legatus_acta_schedae_x\tests\test_scheduler_service.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 93 files would be left unchanged.

- [ ] x_legatus_acta_schedae_x — ruff_check
  - Summary: ruff_check failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:30:52.714233+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SLF001 Private member accessed: `_synced_tasks`
      --> tests\test_plugin_calendar_sync.py:63:27
       |
    61 |         )
    62 |         self.dispatcher.publish(TaskCreated(task))
    …

- [ ] x_legatus_acta_schedae_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:30:50.113964+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SLF001 Private member accessed: `_synced_tasks`
      --> tests\test_plugin_calendar_sync.py:63:27
       |
    61 |         )
    62 |         self.dispatcher.publish(TaskCreated(task))
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:31:35.529046+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
     --> telemetry.py:5:7
      |
    3 |   from __future__ import annotations
    4 |
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:31:33.886778+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
     --> telemetry.py:5:7
      |
    3 |   from __future__ import annotations
    4 |
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-28T00:32:16.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-28T00:32:19.438993+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-28 00:28:08.989459+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-28 00:32:19.201433+00:00
    @@ -754,13 +754,11 @@
             if payload.summary:
                 log_data["summary"] = payload.summary
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 9 files would be left unchanged.

- [ ] x_make_persistent_env_var_x — black
  - Summary: black failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-28T0…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-28T00:33:27.107141+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_persistent_env_var_x\tests\test_persistent_env.py	2025-10-28 00:28:24.063220+00:00
    +++ C:\x_runner_x\x_make_persistent_env_var_x\tests\test_persistent_env.py	2025-10-28 00:33:26.314793+00:00
    @@ -167,11 +167,11 @@
                         {"name": "ALPHA", "label": "Alpha", "required": True},
                         {"name": "BETA", "label": "Beta", "required": False},
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\tests\test_persistent_env.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_gui_x.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-28T00:33:29.977387+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_gui_x.py:18: error: Incompatible types in assignment (expression has type "None", variable has type Module)  [assignment]
    x_cls_make_persistent_env_var_gui_x.py:19: error: Incompatible types in assignment (expression has type "None", variable has type Module)  [assignment]
    x_cls_make_persistent_env_var_gui_x.py:21: error: Incompatible types in assignment (expression has type "None", variable has type "ModuleNotFoundError")  [assignment]
    x_cls_make_persistent_env_var_gui_x.py:39: error: Explicit "Any" is not allowed  [explicit-any]
    x_cls_make_persistent_env_var_gui_x.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:33:27.276374+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0415 `import` should be at the top-level of a file
      --> tests\test_cli_dispatch.py:25:9
       |
    24 |       try:
    25 | /         from x_make_persistent_env_var_x import (
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:33:24.622295+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0415 `import` should be at the top-level of a file
      --> tests\test_cli_dispatch.py:25:9
       |
    24 |       try:
    25 | /         from x_make_persistent_env_var_x import (
    …

- [ ] x_make_slack_dump_and_reset_z — black
  - Summary: black failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-28T00:34:50.252864+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_slack_dump_and_reset.py	2025-10-28 00:34:47.922726+00:00
    +++ C:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_slack_dump_and_reset.py	2025-10-28 00:34:49.528408+00:00
    @@ -22,11 +22,13 @@
             self.downloaded: list[Path] = []
             self.deleted_messages: list[tuple[str, str]] = []
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_slack_dump_and_reset.py
    would reformat C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 5 files would be left unchanged.

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --sho…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-28T00:34:53.280536+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:17: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_slack_dump_and_reset_x.py:17: error: Library stubs not installed for "requests"  [import-untyped]
    x_cls_make_slack_dump_and_reset_x.py:17: note: Error code "import-untyped" not covered by "type: ignore" comment
    x_cls_make_slack_dump_and_reset_x.py:17: note: Hint: "python3 -m pip install types-requests"
    x_cls_make_slack_dump_and_reset_x.py:17: note: (or run "mypy --install-types" to install all missing stub packages)
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-28T00:34:53.283957+00:00 duration: 2.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-28T00:34:55.732799+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py:3:6 - error: Import "x_make_slack_dump_and_reset_z.x_cls_make_slack_dump_and_reset_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:3:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:5:6 - error: Import "x_make_slack_dump_and_reset_z.json_contracts" could not be resolved (reportMissingImports)
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_check
  - Summary: ruff_check failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:34:50.393346+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S108 Probable insecure usage of temporary file or directory: "/tmp"
      --> tests\test_json_contracts.py:17:29
       |
    15 |         "parameters": {
    16 |             "channels": ["C123"],
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-28T00:34:47.981027+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S108 Probable insecure usage of temporary file or directory: "/tmp"
      --> tests\test_json_contracts.py:17:29
       |
    15 |         "parameters": {
    16 |             "channels": ["C123"],
    …
