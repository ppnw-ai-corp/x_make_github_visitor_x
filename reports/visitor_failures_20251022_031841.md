# Visitor TODO Report

- Generated: 2025-10-22T03:18:41.530272+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 15
- Failing tools: 34
- Recorded failures: 34

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:13:54.635810+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    tests\test_json_contracts.py:7: error: Library stubs not installed for "jsonschema.exceptions"  [import-untyped]
    tests\test_json_contracts.py:7: note: Hint: "python3 -m pip install types-jsonschema"
    tests\test_json_contracts.py:7: note: (or run "mypy --install-types" to install all missing stub packages)
    tests\test_json_contracts.py:7: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:14:19.175147+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_make_github_clones_x\__init__.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\__init__.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    __init__.py:6: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-22T03:14:18.113666+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
      --> tests\test_json_contracts.py:8:29
       |
     6 | import os
     7 | import sys
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-22T03:14:16.317435+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
      --> tests\test_json_contracts.py:8:29
       |
     6 | import os
     7 | import sys
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-22T03:14:51.729355+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-22 03:11:09.941226+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-22 03:14:50.978690+00:00
    @@ -29,10 +29,11 @@
     
     
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
  - Captured: 2025-10-22T03:14:53.791181+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    runner.py:19: error: Library stubs not installed for "jsonschema"  [import-untyped]
    runner.py:19: note: Hint: "python3 -m pip install types-jsonschema"
    runner.py:19: note: (or run "mypy --install-types" to install all missing stub packages)
    runner.py:19: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:15:13.590717+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:5: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    __init__.py:5: note: You may be running mypy in a subpackage, mypy should be run on the package root
    tests\test_json_contracts.py:11: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    tests\test_json_contracts.py:13: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.json_contracts"  [import]
    tests\test_json_contracts.py:18: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import]
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-22T03:15:38.342136+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-22 03:11:13.485389+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-22 03:15:37.968188+00:00
    @@ -21,10 +21,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:15:40.588508+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    x_cls_make_markdown_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_markdown_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_markdown_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_markdown_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-22T03:16:08.746344+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py	2025-10-22 03:11:15.626858+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py	2025-10-22 03:16:06.695899+00:00
    @@ -20,10 +20,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 4 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:16:13.147946+00:00
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
  - Captured: 2025-10-22T03:16:08.888722+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
      --> tests\test_json_contracts.py:92:15
       |
    90 |     parameters_obj = payload.get("parameters")
    91 |     if not isinstance(parameters_obj, dict):
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-22T03:16:04.150135+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
      --> tests\test_json_contracts.py:92:15
       |
    90 |     parameters_obj = payload.get("parameters")
    91 |     if not isinstance(parameters_obj, dict):
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:16:20.808915+00:00
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
  - Captured: 2025-10-22T03:16:26.627769+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-22 03:11:19.837350+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-22 03:16:26.144919+00:00
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
  - Captured: 2025-10-22T03:16:27.862291+00:00
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
  - Captured: 2025-10-22T03:16:26.782433+00:00
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
  - Captured: 2025-10-22T03:16:25.183033+00:00
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
  - Captured: 2025-10-22T03:16:55.341446+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-22 03:11:23.982187+00:00
    +++ C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-22 03:16:55.159962+00:00
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
  - Captured: 2025-10-22T03:17:06.737989+00:00
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
  - Captured: 2025-10-22T03:16:55.455509+00:00
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
  - Captured: 2025-10-22T03:16:52.964448+00:00
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
  - Captured: 2025-10-22T03:17:18.789524+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-22 03:17:17.631929+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-22 03:17:18.688076+00:00
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
  - Captured: 2025-10-22T03:17:19.859411+00:00
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
  - Captured: 2025-10-22T03:17:18.932466+00:00
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
  - Captured: 2025-10-22T03:17:17.659726+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG001 Unused function argument: `project_root`
       --> x_cls_make_py_venv_x.py:360:5
        |
    359 | def update_tox_ini(
    360 |     project_root: Path,
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-22T03…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-22T03:17:54.676157+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-22 03:17:51.523624+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-22 03:17:53.840697+00:00
    @@ -27,11 +27,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    would reformat C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-22T03:18:05.864182+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    publish_flow.py:66: error: Expression has type "Any"  [misc]
    publish_flow.py:67: error: Expression has type "Any"  [misc]
    publish_flow.py:71: error: Expression has type "Any"  [misc]
    publish_flow.py:72: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-22T03:18:05.867867+00:00 duration: 4.100s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-22T03:18:09.967651+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:90:17 - error: Cannot assign to attribute "FakePublisher" for class "ModuleType"
      Â Â Attribute "FakePublisher" is unknown (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py:199:13 - error: Cannot assign to attribute "run_report_path" for class "RuntimeError"
      Â Â Attribute "run_report_path" is unknown (reportAttributeAccessIssue)
    …

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-22T03:17:54.789913+00:00
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
  - Captured: 2025-10-22T03:17:51.545564+00:00
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
  - Captured: 2025-10-22T03:18:39.707818+00:00
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
  - Captured: 2025-10-22T03:18:37.881740+00:00
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
  - Captured: 2025-10-22T03:18:36.427381+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
