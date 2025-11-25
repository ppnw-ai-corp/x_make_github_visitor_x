# Visitor TODO Report

- Generated: 2025-10-20T16:56:04.108204+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 15
- Failing tools: 56
- Recorded failures: 56

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:53:39.258815+00:00 durat…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:53:42.438660+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py	2025-10-20 16:53:13.837675+00:00
    +++ C:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py	2025-10-20 16:53:40.721240+00:00
    @@ -34,11 +34,13 @@
             worker_done_event: threading.Event,
             parent: QtWidgets.QWidget | None = None,
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py
    would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 27 files would be left unchanged.

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:53:43.487417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    interface\gui\prototypes\shared.py:319: error: Explicit "Any" is not allowed  [explicit-any]
    interface\gui\prototypes\shared.py:320: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    interface\gui\prototypes\shared.py:320: error: Expression type contains "Any" (has type "Any | None")  [misc]
    interface\gui\prototypes\shared.py:322: error: Expression type contains "Any" (has type "Any | None")  [misc]
    interface\gui\prototypes\shared.py:348: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-20T16:53:43.500732+00:00 duration: 3.872s tool_version: pyright 1.1…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-20T16:53:47.372430+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py
      c:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py:11:29 - error: "load_progress_snapshot" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py:35:17 - error: Variable not allowed in type expression (reportInvalidTypeForm)
      c:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py:41:32 - error: Variable not allowed in type expression (reportInvalidTypeForm)
      c:\x_runner_x\x_0_make_all_x\interface\gui\progress_board.py:171:15 - error: Variable not allowed in type expression (reportInvalidTypeForm)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:53:42.574160+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> interface\gui\commit.py:7:29
      |
    5 | import json
    6 | import subprocess
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:53:39.238887+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> interface\gui\commit.py:7:29
      |
    5 | import json
    6 | import subprocess
    …

- [ ] x_legatus_acta_schedae_x — mypy
  - Summary: mypy failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:53:59.625608+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    Found 4 errors in 1 file (checked 95 source files)

- [ ] x_legatus_acta_schedae_x — ruff_check
  - Summary: ruff_check failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:53:57.788751+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> tests\test_automation_service.py:4:29
      |
    3 | import json
    4 | from collections.abc import Callable
    …

- [ ] x_legatus_acta_schedae_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:53:55.760788+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> tests\test_automation_service.py:4:29
      |
    3 | import json
    4 | from collections.abc import Callable
    …

- [ ] x_make_common_x — black
  - Summary: black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:54:06.325565+00:00 dur…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:54:07.827829+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-20 03:45:12.624232+00:00
    +++ C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-20 16:54:07.476635+00:00
    @@ -11,11 +11,13 @@
     
     JSONPrimitive = str | int | float | bool | None
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_common_x\telemetry.py
    would reformat C:\x_runner_x\x_make_common_x\progress_snapshot.py
    would reformat C:\x_runner_x\x_make_common_x\stage_progress.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:54:08.925594+00:00
  - Suggested action: Investigate
  - Stdout preview:
    progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    stage_progress.py:380: error: Expression has type "Any"  [misc]
    Found 4 errors in 2 files (checked 18 source files)

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:07.985838+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `_resolve_binary` is too complex (11 > 10)
      --> exporters.py:65:5
       |
    65 | def _resolve_binary(
       |     ^^^^^^^^^^^^^^^
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:06.314905+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `_resolve_binary` is too complex (11 > 10)
      --> exporters.py:65:5
       |
    65 | def _resolve_binary(
       |     ^^^^^^^^^^^^^^^
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:54:22.88…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:54:24.895245+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\__init__.py	2025-10-20 03:42:36.181660+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\__init__.py	2025-10-20 16:54:23.786867+00:00
    @@ -1,19 +1,19 @@
     """x_make_github_clones_x package."""
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_clones_x\__init__.py
    would reformat C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 11 files would be left unchanged.

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:54:25.733341+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\__init__.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    __init__.py:5: error: Cannot find implementation or library stub for module named "__main__.x_cls_make_github_clones_x"  [import-not-found]
    __init__.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_github_clones_x.py:35: error: Cannot find implementation or library stub for module named "x_make_common_x.stage_progress"  [import]
    x_cls_make_github_clones_x.py:38: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:25.031238+00:00
  - Suggested action: Investigate
  - Stdout preview:
    W191 Indentation contains tabs
     --> __init__.py:6:1
      |
    5 | from .x_cls_make_github_clones_x import (  # re-export public surface
    6 |     RepoRecord,
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:22.864428+00:00
  - Suggested action: Investigate
  - Stdout preview:
    W191 Indentation contains tabs
     --> __init__.py:6:1
      |
    5 | from .x_cls_make_github_clones_x import (  # re-export public surface
    6 |     RepoRecord,
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:54:45.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:54:48.597965+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-20 16:52:59.758569+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-20 16:54:48.412430+00:00
    @@ -45,10 +45,11 @@
                 emit_event,
                 get_logger,
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 9 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:54:49.909621+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    inspection_flow.py:501: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:48.728491+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC002 Move third-party import `x_make_common_x.stage_progress.RepoProgressReporter` into a type-checking block
      --> inspection_flow.py:16:44
       |
    15 | from x_make_common_x import ensure_workspace_on_syspath, get_logger
    16 | from x_make_common_x.stage_progress import RepoProgressReporter
    …

- [ ] x_make_github_visitor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:54:45.953350+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC002 Move third-party import `x_make_common_x.stage_progress.RepoProgressReporter` into a type-checking block
      --> inspection_flow.py:16:44
       |
    15 | from x_make_common_x import ensure_workspace_on_syspath, get_logger
    16 | from x_make_common_x.stage_progress import RepoProgressReporter
    …

- [ ] x_make_graphviz_x — black
  - Summary: black failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:01.029130+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:02.560032+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_graphviz_x\json_contracts.py	2025-10-20 03:42:41.118634+00:00
    +++ C:\x_runner_x\x_make_graphviz_x\json_contracts.py	2025-10-20 16:55:01.985518+00:00
    @@ -5,25 +5,25 @@
     _NODE_SCHEMA: dict[str, object] = {
         "type": "object",
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_graphviz_x\json_contracts.py
    would reformat C:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_graphviz_x\x_cls_make_graphviz_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:03.279013+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:5: error: Cannot find implementation or library stub for module named "__main__.x_cls_make_graphviz_x"  [import-not-found]
    __init__.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:8: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    tests\test_json_contracts.py:10: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.json_contracts"  [import]
    tests\test_json_contracts.py:15: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    …

- [ ] x_make_graphviz_x — ruff_check
  - Summary: ruff_check failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:02.678836+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:70:5
       |
    68 |     validate_payload(result, OUTPUT_SCHEMA)
    69 |     status_value = result.get("status")
    …

- [ ] x_make_graphviz_x — ruff_fix
  - Summary: ruff_fix failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:01.012301+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:70:5
       |
    68 |     validate_payload(result, OUTPUT_SCHEMA)
    69 |     status_value = result.get("status")
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:13.615325+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:15.006619+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-20 04:07:46.869483+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-20 16:55:14.565735+00:00
    @@ -78,11 +78,13 @@
         status_value = result.get("status")
         assert isinstance(status_value, str)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 4 files would be left unchanged.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:16.448073+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    x_cls_make_markdown_x.py:22: error: Unused "type: ignore" comment  [unused-ignore]
    …

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:15.145815+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:79:5
       |
    77 |     validate_payload(result, OUTPUT_SCHEMA)
    78 |     status_value = result.get("status")
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:13.609518+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:79:5
       |
    77 |     validate_payload(result, OUTPUT_SCHEMA)
    78 |     status_value = result.get("status")
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:20.799067+00:00 d…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:22.925415+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-20 03:42:46.161963+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-20 16:55:22.755106+00:00
    @@ -90,16 +90,11 @@
     
     SCHEMA_VERSION = "x_make_mermaid_x.run/1.0"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-an…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:24.173809+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:22: error: Unused "type: ignore" comment  [unused-ignore]
    …

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:23.058386+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
      --> tests\test_json_contracts.py:89:9
       |
    87 |     payload["parameters"]["mermaid_cli_path"] = str(fake_cli)
    88 |
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 start…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:20.790699+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
      --> tests\test_json_contracts.py:89:9
       |
    87 |     payload["parameters"]["mermaid_cli_path"] = str(fake_cli)
    88 |
    …

- [ ] x_make_persistent_env_var_x — black
  - Summary: black failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T1…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:30.222725+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py	2025-10-20 04:07:47.910098+00:00
    +++ C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py	2025-10-20 16:55:29.538132+00:00
    @@ -147,11 +147,13 @@
         assert isinstance(user_obj, dict)
         assert provided_obj.get("API_TOKEN") == "<hidden>"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\tests\test_persistent_env.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:31.436194+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:268: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:30.352888+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
      --> tests\test_json_contracts.py:69:5
       |
    69 | def test_main_json_persist_values_success(
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:28.483386+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
      --> tests\test_json_contracts.py:69:5
       |
    69 | def test_main_json_persist_values_success(
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:35.402423…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:36.978019+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-20 03:42:51.701996+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-20 16:55:36.380872+00:00
    @@ -64,11 +64,13 @@
         result = main_json(sample_input)
         validate_payload(result, OUTPUT_SCHEMA)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_pip_updates_x\x_cls_make_pip_updates_x.py
    would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --dis…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:37.720657+00:00
  - Suggested action: Investigate
  - Stdout preview:
    update_flow.py:16: error: Unused "type: ignore" comment  [unused-ignore]
    update_flow.py:654: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    x_cls_make_pip_updates_x.py:305: error: Expression has type "Any"  [misc]
    x_cls_make_pip_updates_x.py:308: error: Expression has type "Any"  [misc]
    x_cls_make_pip_updates_x.py:308: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:37.094333+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:56:5
       |
    54 | def test_existing_reports_align_with_schema() -> None:
    55 |     report_files = sorted(REPORTS_DIR.glob("x_make_pip_updates_x_run_*.json"))
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:35.394364+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:56:5
       |
    54 | def test_existing_reports_align_with_schema() -> None:
    55 |     report_files = sorted(REPORTS_DIR.glob("x_make_pip_updates_x_run_*.json"))
    …

- [ ] x_make_py_mod_sideload_x — black
  - Summary: black failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:43.144447+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-20 03:42:57.115646+00:00
    +++ C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-20 16:55:43.001073+00:00
    @@ -154,11 +154,13 @@
             obj: optional attribute name to return from the module
             """
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:44.231379+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:165: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    …

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:43.271785+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:95:5
       |
    94 |     parameters_obj = payload.get("parameters")
    95 |     assert isinstance(parameters_obj, dict)
    …

- [ ] x_make_py_mod_sideload_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:41.872494+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:95:5
       |
    94 |     parameters_obj = payload.get("parameters")
    95 |     assert isinstance(parameters_obj, dict)
    …

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-an…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:48.230237+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:267: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:396: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_py_venv_x.py:402: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_py_venv_x.py:409: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_py_venv_x.py:460: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:47.668546+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
      --> x_cls_make_py_venv_x.py:12:29
       |
    10 | import subprocess
    11 | import sys
    …

- [ ] x_make_py_venv_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 start…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:47.131586+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
      --> x_cls_make_py_venv_x.py:12:29
       |
    10 | import subprocess
    11 | import sys
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:52.449428+00:00 duratio…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:55:54.176527+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-20 04:07:48.963368+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-20 16:55:53.578246+00:00
    @@ -163,12 +163,16 @@
         status_value = result.get("status")
         assert isinstance(status_value, str)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    would reformat C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unim…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:55:55.376435+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    C:\x_runner_x\x_make_common_x\stage_progress.py:380: error: Expression has type "Any"  [misc]
    x_cls_make_pypi_x.py:27: error: Unused "type: ignore" comment  [unused-ignore]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-20T16:55:55.379278+00:00 duration: 2.629s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-20T16:55:58.007756+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:86:17 - error: Cannot assign to attribute "FakePublisher" for class "ModuleType"
      Â Â Attribute "FakePublisher" is unknown (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:172:13 - error: Cannot assign to attribute "run_report_path" for class "RuntimeError"
      Â Â Attribute "run_report_path" is unknown (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:54.302480+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:6:29
      |
    4 | import json
    5 | import sys
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:52.444552+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:6:29
      |
    4 | import json
    5 | import sys
    …

- [ ] x_make_yahw_x — black
  - Summary: black failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-20T16:55:59.835929+00:00 duratio…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-20T16:56:01.048267+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py	2025-10-20 03:42:59.635792+00:00
    +++ C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py	2025-10-20 16:56:00.905313+00:00
    @@ -28,31 +28,37 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unim…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-20T16:56:02.167946+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:7: error: Expression has type "Any"  [misc]
    __init__.py:8: error: Expression has type "Any"  [misc]
    __init__.py:9: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:201: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\progress_snapshot.py:202: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:56:01.183633+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-20T16:55:59.829348+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …
