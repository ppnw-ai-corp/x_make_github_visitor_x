# Visitor TODO Report

- Generated: 2025-10-23T21:21:22.672700+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 27
- Recorded failures: 27

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 2) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:16:01.564238+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_0_make_all_x': No such file or directory

- [ ] x_0_make_ppnw_dot_ai_x — mypy
  - Summary: mypy failed for x_0_make_ppnw_dot_ai_x (exit 2) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-er…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:16:07.365182+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_0_make_ppnw_dot_ai_x': No such file or directory

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 2) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:17:48.772932+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_common_x': No such file or directory

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_clones_x --strict --no-warn-unused-configs --show-er…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:18:13.878318+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "main_json"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "resolve_workspace_root"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "synchronize_workspace"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-23T21:18:13.883019+00:00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-23T21:18:16.462432+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:114:12 - error: Module is not callable (reportCallIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:127:15 - error: Module cannot be used as a type (reportInvalidTypeForm)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:152:14 - error: Module is not callable (reportCallIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:198:12 - error: Module is not callable (reportCallIssue)
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 2) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_visitor_x --strict --no-warn-unused-configs --show…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:18:55.888669+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_github_visitor_x': No such file or directory

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 2) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:19:17.069698+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_graphviz_x': No such file or directory

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 2) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:19:45.180742+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_markdown_x': No such file or directory

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 2) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-r…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:20:12.831813+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_mermaid_x': No such file or directory

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T21:20:12.526667+00:00
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
  - Captured: 2025-10-23T21:20:10.725288+00:00
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
  - Captured: 2025-10-23T21:20:41.263072+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_persistent_env_var_x': No such file or directory

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 2) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-co…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:20:56.249947+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_pip_updates_x': No such file or directory

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T21:20:55.936296+00:00
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
  - Captured: 2025-10-23T21:20:54.385132+00:00
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
  - Captured: 2025-10-23T21:21:02.707287+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_py_mod_sideload_x': No such file or directory

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T21:21:02.401675+00:00
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
  - Captured: 2025-10-23T21:21:00.868197+00:00
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
  - Captured: 2025-10-23T21:21:06.639823+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 21:15:07.772954+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 21:21:06.563179+00:00
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
  - Captured: 2025-10-23T21:21:07.106803+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_py_venv_x': No such file or directory

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T21:21:06.753078+00:00
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
  - Captured: 2025-10-23T21:21:05.727758+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_py_venv_x.py:285:13
        |
    283 |             return
    284 |         try:
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T21…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T21:21:13.392283+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 21:15:04.193574+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 21:21:13.154944+00:00
    @@ -22,12 +22,14 @@
     
         import pytest
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 2) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:21:13.863419+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_pypi_x': No such file or directory

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 2) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T21:21:20.616959+00:00
  - Suggested action: Investigate
  - Stderr preview:
    mypy: can't read file 'x_make_yahw_x': No such file or directory

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T21:21:20.296517+00:00
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
  - Captured: 2025-10-23T21:21:18.899336+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
