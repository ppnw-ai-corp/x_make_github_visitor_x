# Visitor TODO Report

- Generated: 2025-10-23T15:57:26.283762+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 15
- Failing tools: 40
- Recorded failures: 40

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:52:45.808093+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_subprocess_utils_x.py:9: error: Cannot find implementation or library stub for module named ".x_logging_utils_x"  [import-not-found]
    __init__.py:5: error: Cannot find implementation or library stub for module named "__main__.exporters"  [import-not-found]
    __init__.py:5: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    __init__.py:12: error: Cannot find implementation or library stub for module named "__main__.json_board"  [import-not-found]
    __init__.py:28: error: Cannot find implementation or library stub for module named "__main__.json_contracts"  [import-not-found]
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:53:06.034357+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-23 15:50:26.475056+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-23 15:53:04.453598+00:00
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
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:53:06.991712+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    fastapi\cli.py:17: error: Explicit "Any" is not allowed  [explicit-any]
    fastapi\cli.py:17: error: Expression type contains "Any" (has type "Any | None")  [misc]
    fastapi\cli.py:18: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:53:06.171546+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:53:03.182113+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:53:40.827905+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-23 15:53:38.379938+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-23 15:53:40.018073+00:00
    @@ -49,10 +49,11 @@
             def _decorate(func: Callable[_P, _T]) -> Callable[_P, _T]:
                 decorated = pytest.fixture(*args, **kwargs)(func)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 9 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-re…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:53:42.086334+00:00
  - Suggested action: Investigate
  - Stdout preview:
    run_visitor_no_cache.py:1: error: Cannot find implementation or library stub for module named "x_make_github_visitor_x"  [import]
    run_visitor_no_cache.py:5: error: Expression has type "Any"  [misc]
    run_visitor_no_cache.py:7: error: Expression has type "Any"  [misc]
    run_visitor_no_cache.py:12: error: Expression has type "Any"  [misc]
    x_cls_make_github_visitor_x.py:7: error: Cannot find implementation or library stub for module named ".runner"  [import-not-found]
    …

- [ ] x_make_graphviz_x — black
  - Summary: black failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:54:00.586114+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py	2025-10-23 15:50:29.930669+00:00
    +++ C:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py	2025-10-23 15:53:59.766850+00:00
    @@ -42,10 +42,11 @@
             def _decorate(func: Callable[_P, _T]) -> Callable[_P, _T]:
                 decorated = pytest.fixture(*args, **kwargs)(func)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_graphviz_x\x_cls_make_graphviz_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 5 files would be left unchanged.

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:54:01.438092+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:5: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    __init__.py:5: note: You may be running mypy in a subpackage, mypy should be run on the package root
    tests\test_json_contracts.py:11: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    tests\test_json_contracts.py:13: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.json_contracts"  [import]
    tests\test_json_contracts.py:18: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    …

- [ ] x_make_graphviz_x — ruff_check
  - Summary: ruff_check failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --t…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:54:00.707347+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (91 > 88)
       --> x_cls_make_graphviz_x.py:613:89
        |
    611 |     json_flag = bool(args_map.get("json", False))
    612 |     json_file_obj = args_map.get("json_file")
    …

- [ ] x_make_graphviz_x — ruff_fix
  - Summary: ruff_fix failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:53:58.237920+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (91 > 88)
       --> x_cls_make_graphviz_x.py:613:89
        |
    611 |     json_flag = bool(args_map.get("json", False))
    612 |     json_file_obj = args_map.get("json_file")
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:54:24.538593+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-23 15:50:31.690790+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-23 15:54:23.730585+00:00
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
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:54:38.053053+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_markdown_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_markdown_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_markdown_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_markdown_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --t…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:54:24.720585+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:54:22.549152+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:55:02.570040+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-22 23:27:19.466485+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-23 15:55:02.305203+00:00
    @@ -818,11 +818,13 @@
     
     def _extract_export_options(
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:55:04.004944+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_mermaid_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_mermaid_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_mermaid_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_mermaid_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:55:02.725734+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:54:59.420409+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:55:29.335627+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_persistent_env_var_x.py:20: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_persistent_env_var_x.py:20: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_persistent_env_var_x.py:20: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_persistent_env_var_x.py:20: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:55:51.811932+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-22 23:27:23.569468+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-23 15:55:51.457678+00:00
    @@ -21,10 +21,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-a…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:55:56.013501+00:00
  - Suggested action: Investigate
  - Stdout preview:
    update_flow.py:86: error: Expression has type "Any"  [misc]
    update_flow.py:558: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    update_flow.py:581: error: Expression type contains "Any" (has type "Any | None")  [misc]
    update_flow.py:582: error: Expression type contains "Any" (has type "Any | None")  [misc]
    update_flow.py:645: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:55:51.929177+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `main_json` is too complex (16 > 10)
       --> update_flow.py:655:5
        |
    655 | def main_json(
        |     ^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:55:49.404189+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `main_json` is too complex (16 > 10)
       --> update_flow.py:655:5
        |
    655 | def main_json(
        |     ^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — black
  - Summary: black failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff sta…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:56:21.172766+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-22 23:27:27.459838+00:00
    +++ C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-23 15:56:20.964054+00:00
    @@ -249,11 +249,13 @@
         missing = _validate_required_inputs(base_path, module_name)
         if missing is not None:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:56:22.521615+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_py_mod_sideload_x.py:17: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_py_mod_sideload_x.py:17: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_py_mod_sideload_x.py:17: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_py_mod_sideload_x.py:17: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:21.287587+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (90 > 88)
       --> x_cls_make_py_mod_sideload_x.py:254:89
        |
    252 |         return _failure_payload(message, details={"field": field})
    253 |
    …

- [ ] x_make_py_mod_sideload_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:19.394300+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (90 > 88)
       --> x_cls_make_py_mod_sideload_x.py:254:89
        |
    252 |         return _failure_payload(message, details={"field": field})
    253 |
    …

- [ ] x_make_py_venv_x — black
  - Summary: black failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:56:31.172245+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-22 13:20:22.362540+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 15:56:31.094327+00:00
    @@ -280,11 +280,13 @@
             LOGGER.debug("Command: %s", " ".join(command))
             if self.dry_run:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted.

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:56:32.126640+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:302: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:490: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:494: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:496: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:497: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:31.304355+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG001 Unused function argument: `project_root`
       --> x_cls_make_py_venv_x.py:360:5
        |
    359 | def update_tox_ini(
    360 |     project_root: Path,
    …

- [ ] x_make_py_venv_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:30.214772+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG001 Unused function argument: `project_root`
       --> x_cls_make_py_venv_x.py:360:5
        |
    359 | def update_tox_ini(
    360 |     project_root: Path,
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T15…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T15:56:58.144536+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py	2025-10-22 23:27:25.416216+00:00
    +++ C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py	2025-10-23 15:56:57.863086+00:00
    @@ -670,11 +670,13 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:56:59.617340+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    publish_flow.py:66: error: Expression has type "Any"  [misc]
    publish_flow.py:67: error: Expression has type "Any"  [misc]
    publish_flow.py:71: error: Expression has type "Any"  [misc]
    publish_flow.py:72: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-23T15:56:59.621023+00:00 duration: 3.168s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-23T15:57:02.788747+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:90:17 - error: Cannot assign to attribute "FakePublisher" for class "ModuleType"
      Â Â Attribute "FakePublisher" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:58.268322+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> publish_flow.py:14:19
       |
    12 | from os import PathLike
    13 | from pathlib import Path
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targe…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:56:55.451507+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> publish_flow.py:14:19
       |
    12 | from os import PathLike
    13 | from pathlib import Path
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T15:57:24.096181+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_yahw_x.py:12: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_yahw_x.py:12: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_yahw_x.py:12: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_yahw_x.py:12: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:57:22.744238+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targe…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-23T15:57:21.159011+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
