# Visitor TODO Report

- Generated: 2025-10-23T19:55:42.661055+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 37
- Recorded failures: 37

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:50:26.856959+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_subprocess_utils_x.py:9: error: Cannot find implementation or library stub for module named ".x_logging_utils_x"  [import-not-found]
    __init__.py:5: error: Cannot find implementation or library stub for module named "__main__.exporters"  [import-not-found]
    __init__.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    __init__.py:12: error: Cannot find implementation or library stub for module named "__main__.json_board"  [import-not-found]
    __init__.py:28: error: Cannot find implementation or library stub for module named "__main__.json_contracts"  [import-not-found]
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:50:51.975371+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-23 19:47:35.508937+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-23 19:50:50.803744+00:00
    @@ -1,17 +1,17 @@
     """Expose the CLI implementation from the script module."""
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_clones_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    would reformat C:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-a…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:50:53.071457+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    fastapi\cli.py:17: error: Explicit "Any" is not allowed  [explicit-any]
    fastapi\cli.py:17: error: Expression type contains "Any" (has type "Any | None")  [misc]
    fastapi\cli.py:18: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:50:52.128169+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:50:49.791040+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_a…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:51:33.672511+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-23 19:47:37.726955+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-23 19:51:33.043943+00:00
    @@ -49,10 +49,11 @@
             def _decorate(func: Callable[_P, _T]) -> Callable[_P, _T]:
                 decorated = pytest.fixture(*args, **kwargs)(func)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 9 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:51:35.151325+00:00
  - Suggested action: Investigate
  - Stdout preview:
    run_visitor_no_cache.py:1: error: Cannot find implementation or library stub for module named "x_make_github_visitor_x"  [import]
    run_visitor_no_cache.py:5: error: Expression has type "Any"  [misc]
    run_visitor_no_cache.py:7: error: Expression has type "Any"  [misc]
    run_visitor_no_cache.py:12: error: Expression has type "Any"  [misc]
    x_cls_make_github_visitor_x.py:7: error: Cannot find implementation or library stub for module named ".runner"  [import-not-found]
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:51:59.465963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:5: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    __init__.py:5: note: You may be running mypy in a subpackage, mypy should be run on the package root
    tests\test_json_contracts.py:11: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    tests\test_json_contracts.py:13: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.json_contracts"  [import]
    tests\test_json_contracts.py:18: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-2…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:52:29.984375+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-23 19:47:40.694841+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-23 19:52:29.359870+00:00
    @@ -42,10 +42,11 @@
             def _decorate(func: Callable[_P, _T]) -> Callable[_P, _T]:
                 decorated = pytest.fixture(*args, **kwargs)(func)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 4 files would be left unchanged.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:52:31.078758+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_markdown_x.py:369: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_markdown_x.py:503: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    tests\test_markdown_builder.py:12: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_markdown_builder.py:20: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_markdown_builder.py:48: error: Argument 1 to "test_to_html_fallback_when_markdown_missing" becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targe…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:52:30.126895+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --t…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:52:28.368221+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:53:01.476228+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-22 23:27:19.466485+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-23 19:53:01.290016+00:00
    @@ -818,11 +818,13 @@
     
     def _extract_export_options(
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:53:02.797019+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:787: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_mermaid_x.py:902: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_mermaid_x.py:1530: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1533: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1533: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:53:01.651160+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:52:58.883479+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --war…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:53:35.274207+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:600: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:601: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:602: error: Expression type contains "Any" (has type "Callable[[], Any]")  [misc]
    x_cls_make_persistent_env_var_x.py:602: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:1018: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 202…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:53:57.267227+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-22 23:27:23.569468+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-23 19:53:56.952596+00:00
    @@ -21,10 +21,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any -…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:53:58.286204+00:00
  - Suggested action: Investigate
  - Stdout preview:
    update_flow.py:86: error: Expression has type "Any"  [misc]
    update_flow.py:558: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    update_flow.py:581: error: Expression type contains "Any" (has type "Any | None")  [misc]
    update_flow.py:582: error: Expression type contains "Any" (has type "Any | None")  [misc]
    update_flow.py:645: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:53:57.400608+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `main_json` is too complex (16 > 10)
       --> update_flow.py:655:5
        |
    655 | def main_json(
        |     ^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:53:55.915246+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `main_json` is too complex (16 > 10)
       --> update_flow.py:655:5
        |
    655 | def main_json(
        |     ^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — black
  - Summary: black failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:54:27.139098+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-22 23:27:27.459838+00:00
    +++ C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-23 19:54:26.988576+00:00
    @@ -249,11 +249,13 @@
         missing = _validate_required_inputs(base_path, module_name)
         if missing is not None:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:54:28.355633+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_mod_sideload_x.py:230: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_py_mod_sideload_x.py:262: error: Returning Any from function declared to return "str | None"  [no-any-return]
    x_cls_make_py_mod_sideload_x.py:262: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:340: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_py_mod_sideload_x.py:426: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:54:27.326196+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (90 > 88)
       --> x_cls_make_py_mod_sideload_x.py:254:89
        |
    252 |         return _failure_payload(message, details={"field": field})
    253 |
    …

- [ ] x_make_py_mod_sideload_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:54:25.644716+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (90 > 88)
       --> x_cls_make_py_mod_sideload_x.py:254:89
        |
    252 |         return _failure_payload(message, details={"field": field})
    253 |
    …

- [ ] x_make_py_venv_x — black
  - Summary: black failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:54:37.836575+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-22 13:20:22.362540+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 19:54:37.795376+00:00
    @@ -280,11 +280,13 @@
             LOGGER.debug("Command: %s", " ".join(command))
             if self.dry_run:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted.

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:54:38.770215+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:302: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:490: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:494: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:496: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:497: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:54:37.977135+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG001 Unused function argument: `project_root`
       --> x_cls_make_py_venv_x.py:360:5
        |
    359 | def update_tox_ini(
    360 |     project_root: Path,
    …

- [ ] x_make_py_venv_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:54:37.113652+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG001 Unused function argument: `project_root`
       --> x_cls_make_py_venv_x.py:360:5
        |
    359 | def update_tox_ini(
    360 |     project_root: Path,
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T19:55:…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-23T19:55:08.912394+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py	2025-10-22 23:27:25.416216+00:00
    +++ C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py	2025-10-23 19:55:08.737331+00:00
    @@ -670,11 +670,13 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreacha…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:55:10.158351+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:8: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_json_contracts.py:8: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:24: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:31: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:32: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m pyright . --level error started_at: 2025-10-23T19:55:10.183504+00:00 duration: 3.025s tool…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-23T19:55:13.203896+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:90:17 - error: Cannot assign to attribute "FakePublisher" for class "ModuleType"
      Â Â Attribute "FakePublisher" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versio…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:55:09.047641+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> publish_flow.py:14:19
       |
    12 | from os import PathLike
    13 | from pathlib import Path
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:55:07.147252+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> publish_flow.py:14:19
       |
    12 | from os import PathLike
    13 | from pathlib import Path
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreacha…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T19:55:40.497308+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_yahw_x.py:63: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_yahw_x.py:116: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_yahw_x.py:144: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versio…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:55:39.616514+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\x_runner_x\artifacts\venvs\.venv-3.12.6\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T19:55:38.282636+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
