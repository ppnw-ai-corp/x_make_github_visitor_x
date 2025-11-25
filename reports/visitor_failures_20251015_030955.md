# Visitor TODO Report

- Generated: 2025-10-15T03:09:55.640491+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 21
- Recorded failures: 21

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T03:08:38.2650…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T03:08:41.406914+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 02:18:02.958933+00:00
    +++ C:\x_runner_x\x_0_make_all_x\interface\gui\app.py	2025-10-15 03:08:40.881734+00:00
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
  - Captured: 2025-10-15T03:08:43.812719+00:00
  - Suggested action: Investigate
  - Stdout preview:
    manifest.py:266: error: Incompatible types in assignment (expression has type "tuple[str, ...]", variable has type "tuple[str]")  [assignment]
    x_cls_make_all_x.py:550: error: Name "entry" already defined on line 522  [no-redef]
    x_cls_make_all_x.py:550: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    x_cls_make_all_x.py:557: error: Argument 1 to "append" of "list" has incompatible type "dict[str, Collection[str]]"; expected "dict[str, object]"  [arg-type]
    x_cls_make_all_x.py:557: note: "dict" is invariant -- see https://mypy.readthedocs.io/en/stable/common_issues.html#variance
    …

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:08:41.792922+00:00
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
  - Captured: 2025-10-15T03:08:38.256553+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `normalized` before `return` statement
       --> interface\gui\app.py:339:16
        |
    337 |             return ""
    338 |         normalized = _normalize_repo_name(value).lower()
    …

- [ ] x_make_common_x — black
  - Summary: black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T03:09:05.22…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T03:09:07.650710+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_common_x\run_reports.py	2025-10-15 03:09:05.151004+00:00
    +++ C:\x_runner_x\x_make_common_x\run_reports.py	2025-10-15 03:09:07.098971+00:00
    @@ -40,11 +40,13 @@
     def isoformat_timestamp(moment: datetime | None = None) -> str:
         current = (moment or datetime.now(UTC)).replace(microsecond=0)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_common_x\run_reports.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 12 files would be left unchanged.

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T03:09:09.154045+00:00
  - Suggested action: Investigate
  - Stdout preview:
    run_reports.py:45: error: Explicit "Any" is not allowed  [explicit-any]
    run_reports.py:46: error: Expression type contains "Any" (has type "Mapping[str, Any] | MutableMapping[str, Any]")  [misc]
    run_reports.py:47: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    run_reports.py:48: error: Expression type contains "Any" (has type "tuple[str, Any]")  [misc]
    run_reports.py:48: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:09:08.009878+00:00
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
  - Captured: 2025-10-15T03:09:05.218508+00:00
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
  - Captured: 2025-10-15T03:09:17.733714+00:00
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
  - Captured: 2025-10-15T03:09:16.649476+00:00
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
  - Captured: 2025-10-15T03:09:14.084869+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> runner.py:35:1
       |
    33 |         )
    34 |
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T0…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T03:09:31.799153+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-15 03:09:29.552218+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-15 03:09:31.416591+00:00
    @@ -55,13 +55,11 @@
         if isinstance(value, Path):
             return str(value)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 4 files would be left unchanged.

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T03:09:33.378530+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_pip_updates_x.py:310: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    update_flow.py:532: error: "Exception" has no attribute "run_report_path"  [attr-defined]
    Found 2 errors in 2 files (checked 5 source files)

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T03:09:33.381936+00:00 duration: 2.059s…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T03:09:35.440478+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\update_flow.py
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:532:24 - error: Cannot assign to attribute "run_report_path" for class "Exception"
      Â Â Attribute "run_report_path" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:09:32.150339+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (68 > 50)
       --> update_flow.py:348:5
        |
    348 | def run_updates_for_packages(  # noqa: PLR0913
        |     ^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:09:29.616137+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (68 > 50)
       --> update_flow.py:348:5
        |
    348 | def run_updates_for_packages(  # noqa: PLR0913
        |     ^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T03:09:38.032088…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T03:09:40.171938+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-15 03:09:37.965496+00:00
    +++ C:\x_runner_x\x_make_pypi_x\publish_flow.py	2025-10-15 03:09:39.841569+00:00
    @@ -31,17 +31,12 @@
             return value
         if isinstance(value, Path):
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\publish_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 1 file would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --dis…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T03:09:43.291758+00:00
  - Suggested action: Investigate
  - Stdout preview:
    publish_flow.py:583: error: Expression type contains "Any" (has type "tuple[str, dict[str, Any | str]]")  [misc]
    publish_flow.py:583: error: Expression type contains "Any" (has type "dict[str, Any | str]")  [misc]
    publish_flow.py:584: error: Expression type contains "Any" (has type "tuple[str, Any | str]")  [misc]
    publish_flow.py:584: error: Expression type contains "Any" (has type "Any | str")  [misc]
    publish_flow.py:685: error: "Exception" has no attribute "run_report_path"  [attr-defined]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T03:09:43.296934+00:00 duration: 2.275s tool_version:…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T03:09:45.571858+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\publish_flow.py
      c:\x_runner_x\x_make_pypi_x\publish_flow.py:685:24 - error: Cannot assign to attribute "run_report_path" for class "Exception"
      Â Â Attribute "run_report_path" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:09:40.506727+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use a list comprehension to create a transformed list
       --> publish_flow.py:565:9
        |
    563 |       manifest_inputs: list[dict[str, object]] = []
    564 |       for entry in entries:
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\x_make_yahw_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T03:09:38.028963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use a list comprehension to create a transformed list
       --> publish_flow.py:565:9
        |
    563 |       manifest_inputs: list[dict[str, object]] = []
    564 |       for entry in entries:
    …
