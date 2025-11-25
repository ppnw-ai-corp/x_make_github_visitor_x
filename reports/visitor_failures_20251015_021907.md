# Visitor TODO Report

- Generated: 2025-10-15T02:19:07.978004+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 10
- Recorded failures: 10

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T02:18:03.0359…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T02:18:05.640272+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 02:18:02.958933+00:00
    +++ C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 02:18:05.240868+00:00
    @@ -528,13 +528,11 @@
                 self.enqueue_log(
                     f"[summary] Applied cached statuses from {report_path.name} for "
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\app.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 14 files would be left unchanged.

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --d…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T02:18:07.799673+00:00
  - Suggested action: Investigate
  - Stdout preview:
    manifest.py:266: error: Incompatible types in assignment (expression has type "tuple[str, ...]", variable has type "tuple[str]")  [assignment]
    x_cls_make_all_x.py:538: error: Name "entry" already defined on line 510  [no-redef]
    x_cls_make_all_x.py:538: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    x_cls_make_all_x.py:545: error: Argument 1 to "append" of "list" has incompatible type "dict[str, Collection[str]]"; expected "dict[str, object]"  [arg-type]
    x_cls_make_all_x.py:545: note: "dict" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
    …

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T02:18:05.961385+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `normalized` before `return` statement
       --> interface\gui\app.py:339:16
        |
    337 |             return ""
    338 |         normalized = _normalize_repo_name(value).lower()
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T02:18:03.031554+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `normalized` before `return` statement
       --> interface\gui\app.py:339:16
        |
    337 |             return ""
    338 |         normalized = _normalize_repo_name(value).lower()
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T02:18:33.076538+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_board.py:113: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    json_board.py:113: error: Expression has type "Any"  [misc]
    json_board.py:121: error: Expression has type "Any"  [misc]
    json_board.py:122: error: Expression has type "Any"  [misc]
    Found 4 errors in 1 file (checked 11 source files)

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T02:18:27.585696+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `builtins` into a type-checking block
     --> json_board.py:5:8
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T02:18:25.441727+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `builtins` into a type-checking block
     --> json_board.py:5:8
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --wa…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T02:18:41.204811+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_visitor_x.py:643: error: Incompatible types in assignment (expression has type "Mapping[str, object]", variable has type "Mapping[str, str]")  [assignment]
    x_cls_make_github_visitor_x.py:659: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    runner.py:643: error: Incompatible types in assignment (expression has type "Mapping[str, object]", variable has type "Mapping[str, str]")  [assignment]
    runner.py:659: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    Found 4 errors in 2 files (checked 8 source files)

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T02:18:40.240177+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> runner.py:35:1
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
  - Captured: 2025-10-15T02:18:37.742032+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> runner.py:35:1
       |
    33 |         )
    34 |
    …
