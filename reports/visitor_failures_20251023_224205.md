# Visitor TODO Report

- Generated: 2025-10-23T22:42:05.198614+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 27
- Recorded failures: 27

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:40:06.789428+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "main_json"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "resolve_workspace_root"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "synchronize_workspace"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:40:06.232236+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types` into a type-checking block
      --> tests\test_json_contracts.py:8:8
       |
     6 | import json
     7 | import os
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:40:04.404413+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types` into a type-checking block
      --> tests\test_json_contracts.py:8:8
       |
     6 | import json
     7 | import os
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T22:40:29.839080+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-23 22:38:54.968899+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-23 22:40:29.590271+00:00
    @@ -959,11 +959,19 @@
                 exit_code = None
                 stdout_obj = exc.output if exc.output is not None else ""
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 9 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-conf…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:40:30.979378+00:00
  - Suggested action: Investigate
  - Stdout preview:
    runner.py:960: error: Expression has type "Any"  [misc]
    runner.py:964: error: Expression type contains "Any" (has type "tuple[int | None, Any | str, bytes | str, bool, datetime, datetime, float]")  [misc]
    runner.py:964: error: Expression type contains "Any" (has type "Any | str")  [misc]
    Found 3 errors in 1 file (checked 13 source files)

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-l…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:40:29.995509+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (91 > 88)
       --> runner.py:964:89
        |
    962 |         end_wall = datetime.now(UTC)
    963 |         duration = max(time.perf_counter() - start_perf, 0.0)
    …

- [ ] x_make_github_visitor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:40:25.643676+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (91 > 88)
       --> runner.py:964:89
        |
    962 |         end_wall = datetime.now(UTC)
    963 |         duration = max(time.perf_counter() - start_perf, 0.0)
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:40:52.965921+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:22: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_graphviz_x.py:602: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:605: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:605: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_graphviz_x.py:624: error: Statement is unreachable  [unreachable]
    …

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:10.530115+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:55: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:56: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 12 source files)

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:18.034745+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:1532: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1535: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1535: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:54: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:55: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:25.738409+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:600: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:601: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:602: error: Expression type contains "Any" (has type "Callable[[], Any]")  [misc]
    x_cls_make_persistent_env_var_x.py:602: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:1142: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T22:41:34.065550+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-23 22:39:03.099084+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-23 22:41:33.851338+00:00
    @@ -729,11 +729,13 @@
             )
         typed_loaded = cast("Mapping[str, object]", loaded_obj)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pip_updates_x --strict --no-warn-unused-configs --sho…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:35.372963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    update_flow.py:16: error: Library stubs not installed for "jsonschema"  [import-untyped]
    update_flow.py:16: note: Hint: "python3 -m pip install types-jsonschema"
    update_flow.py:16: note: (or run "mypy --install-types" to install all missing stub packages)
    update_flow.py:16: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    update_flow.py:86: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:41:34.204671+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (7 > 5)
       --> update_flow.py:682:5
        |
    682 | def _run_updates_stage(
        |     ^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:41:32.000125+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (7 > 5)
       --> update_flow.py:682:5
        |
    682 | def _run_updates_stage(
        |     ^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:42.532712+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_mod_sideload_x.py:17: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_py_mod_sideload_x.py:17: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_py_mod_sideload_x.py:17: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_py_mod_sideload_x.py:17: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_py_mod_sideload_x.py:230: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:41:41.487666+00:00
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
  - Captured: 2025-10-23T22:41:40.010483+00:00
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
  - Captured: 2025-10-23T22:41:46.490030+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 22:39:08.649207+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 22:41:46.385441+00:00
    @@ -280,13 +280,11 @@
             LOGGER.debug("Command: %s", " ".join(command))
             if self.dry_run:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted.

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:47.272695+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:304: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:492: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:496: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:498: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:499: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — ruff_check
  - Summary: ruff_check failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:41:46.615884+00:00
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
  - Captured: 2025-10-23T22:41:45.513892+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_py_venv_x.py:285:13
        |
    283 |             return
    284 |         try:
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-23T22…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T22:41:54.329879+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 22:39:05.390532+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 22:41:54.106935+00:00
    @@ -22,12 +22,14 @@
     
         import pytest
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:41:55.734623+00:00
  - Suggested action: Investigate
  - Stdout preview:
    publish_flow.py:68: error: Expression has type "Any"  [misc]
    publish_flow.py:69: error: Expression has type "Any"  [misc]
    publish_flow.py:73: error: Expression has type "Any"  [misc]
    publish_flow.py:74: error: Expression has type "Any"  [misc]
    x_cls_make_pypi_x.py:28: error: Library stubs not installed for "jsonschema"  [import-untyped]
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:42:03.237400+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_yahw_x.py:12: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_yahw_x.py:12: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_yahw_x.py:12: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_yahw_x.py:12: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_yahw_x.py:63: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:42:02.214979+00:00
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
  - Captured: 2025-10-23T22:42:00.774481+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
