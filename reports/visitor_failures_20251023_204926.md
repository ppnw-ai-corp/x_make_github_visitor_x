# Visitor TODO Report

- Generated: 2025-10-23T20:49:26.509402+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 32
- Recorded failures: 32

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 2) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:42:41.289144+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_0_make_all_x': No such file or directory

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 2) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:44:25.960675+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_common_x': No such file or directory

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_clones_x --strict --no-warn-unused-configs --show-er…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:44:48.656571+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "main_json"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "resolve_workspace_root"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "synchronize_workspace"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-23T20:44:48.666395+00:00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-23T20:44:51.934963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:114:12 - error: Module is not callable (reportCallIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:127:15 - error: Module cannot be used as a type (reportInvalidTypeForm)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:152:14 - error: Module is not callable (reportCallIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:198:12 - error: Module is not callable (reportCallIssue)
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:44:47.965749+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:44:45.961185+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 2) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_visitor_x --strict --no-warn-unused-configs --show…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:45:30.692826+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_github_visitor_x': No such file or directory

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 2) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:45:52.937052+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_graphviz_x': No such file or directory

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 2) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:46:23.199972+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_markdown_x': No such file or directory

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --t…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:46:22.804666+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:106:13
        |
    104 |         else:
    105 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:46:20.712623+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:106:13
        |
    104 |         else:
    105 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 2) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-r…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:46:51.297264+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_mermaid_x': No such file or directory

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:46:50.901068+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:46:49.005298+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
       --> tests\test_json_contracts.py:105:13
        |
    103 |         else:
    104 |             message = f"Report {report_file.name} must contain a JSON object"
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 2) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_persistent_env_var_x --strict --no-warn-unused-co…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:47:21.930146+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_persistent_env_var_x': No such file or directory

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 2) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-co…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:47:44.583964+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_pip_updates_x': No such file or directory

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:47:44.273396+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:47:42.714140+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `main_json` is too complex (16 > 10)
       --> update_flow.py:655:5
        |
    655 | def main_json(
        |     ^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 2) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_py_mod_sideload_x --strict --no-warn-unused-configs --s…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:48:13.215134+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_py_mod_sideload_x': No such file or directory

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:12.900184+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
       --> x_cls_make_py_mod_sideload_x.py:290:5
        |
    290 | def _resolve_attribute_if_requested(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:11.463413+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
       --> x_cls_make_py_mod_sideload_x.py:290:5
        |
    290 | def _resolve_attribute_if_requested(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_py_venv_x — black
  - Summary: black failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T20:48:22.955485+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 20:48:22.038625+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 20:48:22.872132+00:00
    @@ -280,13 +280,11 @@
             LOGGER.debug("Command: %s", " ".join(command))
             if self.dry_run:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted.

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 2) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-r…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:48:23.422403+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_py_venv_x': No such file or directory

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:23.063602+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_py_venv_x.py:285:13
        |
    283 |             return
    284 |         try:
    …

- [ ] x_make_py_venv_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:22.059096+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_py_venv_x.py:285:13
        |
    283 |             return
    284 |         try:
    …

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 2) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:48:55.243005+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_pypi_x': No such file or directory

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-23T20:48:55.245640+00:00 duration: 2.688s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-23T20:48:57.933940+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:54.920043+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:48:53.009234+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> publish_flow.py:14:19
       |
    12 | from os import PathLike
    13 | from pathlib import Path
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 2) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T20:49:23.769648+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_yahw_x': No such file or directory

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:49:23.417729+00:00
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
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T20:49:21.827603+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
