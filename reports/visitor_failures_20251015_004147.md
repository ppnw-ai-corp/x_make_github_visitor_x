# Visitor TODO Report

- Generated: 2025-10-15T00:41:47.491631+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 15
- Failing tools: 11
- Recorded failures: 11

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T00:40:20.8738…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T00:40:22.953982+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 00:18:43.605911+00:00
    +++ C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 00:40:22.378814+00:00
    @@ -122,11 +122,10 @@
     class GuiExit:
         """Outcome metadata after the Qt event loop terminates."""
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 13 files would be left unchanged.

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --d…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T00:40:24.521202+00:00
  - Suggested action: Investigate
  - Stdout preview:
    manifest.py:266: error: Incompatible types in assignment (expression has type "tuple[str, ...]", variable has type "tuple[str]")  [assignment]
    x_cls_make_all_x.py:540: error: Name "entry" already defined on line 512  [no-redef]
    x_cls_make_all_x.py:540: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    x_cls_make_all_x.py:547: error: Argument 1 to "append" of "list" has incompatible type "dict[str, Collection[str]]"; expected "dict[str, object]"  [arg-type]
    x_cls_make_all_x.py:547: note: "dict" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
    …

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:23.208494+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TID252 Prefer absolute imports over relative imports from parent modules
      --> interface\gui\app.py:18:1
       |
    16 |   from x_make_common_x import register_listener
    17 |
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:20.868922+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TID252 Prefer absolute imports over relative imports from parent modules
      --> interface\gui\app.py:18:1
       |
    16 |   from x_make_common_x import register_listener
    17 |
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T00:40:44.511571+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_board.py:111: error: Function "x_make_common_x.json_board.BoardState.list" is not valid as a type  [valid-type]
    json_board.py:111: note: Perhaps you need "Callable[...]" or a callback protocol?
    json_board.py:112: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    json_board.py:112: error: Expression has type "Any"  [misc]
    json_board.py:119: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:43.611523+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
      --> json_board.py:10:21
       |
     8 | from dataclasses import dataclass, field
     9 | from datetime import UTC, datetime
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:41.567586+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
      --> json_board.py:10:21
       |
     8 | from dataclasses import dataclass, field
     9 | from datetime import UTC, datetime
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-1…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T00:40:55.061800+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py	2025-10-15 00:35:11.860904+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py	2025-10-15 00:40:54.659132+00:00
    @@ -328,11 +328,14 @@
                     # hidden or dunder directories (including caches)
                     continue
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 2) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --wa…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T00:40:55.709066+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_visitor_x.py: error: Source file found twice under different module names: "x_cls_make_github_visitor_x" and "x_make_github_visitor_x.x_cls_make_github_visitor_x"
    Found 1 error in 1 file (errors prevented further checking)

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:55.342695+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> x_cls_make_github_visitor_x.py:35:1
       |
    33 |         )
    34 |
    …

- [ ] x_make_github_visitor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 …
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T00:40:52.799987+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> x_cls_make_github_visitor_x.py:35:1
       |
    33 |         )
    34 |
    …
