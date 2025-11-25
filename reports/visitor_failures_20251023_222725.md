# Visitor TODO Report

- Generated: 2025-10-23T22:27:25.655333+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 29
- Recorded failures: 29

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:21:16.685920+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_gui_columns.py:12: error: Skipping analyzing "PySide6.QtCore": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    tests\test_gui_columns.py:12: error: Skipping analyzing "PySide6.QtWidgets": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    tests\test_gui_columns.py:12: error: Skipping analyzing "PySide6": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    tests\test_gui_columns.py:21: error: Type of variable becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_gui_columns.py:111: error: Expression has type "Any"  [misc]
    …

- [ ] x_0_make_ppnw_dot_ai_x — mypy
  - Summary: mypy failed for x_0_make_ppnw_dot_ai_x (exit 2) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:21:22.807782+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_0_make_ppnw_dot_ai_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_common_x --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:23:07.412679+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_contracts.py:8: error: Library stubs not installed for "jsonschema.validators"  [import-untyped]
    json_contracts.py:8: note: Hint: "python3 -m pip install types-jsonschema"
    json_contracts.py:8: note: (or run "mypy --install-types" to install all missing stub packages)
    json_contracts.py:8: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:7: error: Library stubs not installed for "jsonschema.exceptions"  [import-untyped]
    …

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:23:31.595066+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    Found 1 error in 1 file (checked 2 source files)

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:23:31.033462+00:00
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
  - Captured: 2025-10-23T22:23:29.175229+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
      --> tests\test_json_contracts.py:10:19
       |
     8 | import typing
     9 | from pathlib import Path
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-conf…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:24:21.051976+00:00
  - Suggested action: Investigate
  - Stdout preview:
    runner.py:19: error: Library stubs not installed for "jsonschema"  [import-untyped]
    runner.py:19: note: Hint: "python3 -m pip install types-jsonschema"
    runner.py:19: note: (or run "mypy --install-types" to install all missing stub packages)
    runner.py:19: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    Found 1 error in 1 file (checked 13 source files)

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-l…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:24:15.080927+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (52 > 50)
       --> runner.py:929:9
        |
    927 |         return env
    928 |
    …

- [ ] x_make_github_visitor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-23T22:24:12.927890+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (52 > 50)
       --> runner.py:929:9
        |
    927 |         return env
    928 |
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:24:43.853782+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:511: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:515: error: Expression type contains "Any" (has type "tuple[str, Any]")  [misc]
    x_cls_make_graphviz_x.py:515: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:516: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:517: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:25:12.657938+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_markdown_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_markdown_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_markdown_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_markdown_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_markdown_x.py:369: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:25:42.950275+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_mermaid_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_mermaid_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_mermaid_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_mermaid_x.py:787: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-23T22:26:11.354346+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:20: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_persistent_env_var_x.py:20: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_persistent_env_var_x.py:20: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_persistent_env_var_x.py:20: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_persistent_env_var_x.py:600: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-23T22:26:30.480511+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-23 22:19:09.595145+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\update_flow.py	2025-10-23 22:26:30.249700+00:00
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
  - Captured: 2025-10-23T22:26:32.796094+00:00
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
  - Captured: 2025-10-23T22:26:30.621668+00:00
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
  - Captured: 2025-10-23T22:26:28.247832+00:00
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
  - Captured: 2025-10-23T22:27:03.247772+00:00
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
  - Captured: 2025-10-23T22:27:02.029139+00:00
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
  - Captured: 2025-10-23T22:27:00.506522+00:00
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
  - Captured: 2025-10-23T22:27:06.795984+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 21:15:07.772954+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-23 22:27:06.731596+00:00
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
  - Captured: 2025-10-23T22:27:07.637047+00:00
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
  - Captured: 2025-10-23T22:27:06.945527+00:00
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
  - Captured: 2025-10-23T22:27:05.867669+00:00
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
  - Captured: 2025-10-23T22:27:14.222863+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 21:15:04.193574+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-23 22:27:13.994682+00:00
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
  - Captured: 2025-10-23T22:27:15.668487+00:00
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
  - Captured: 2025-10-23T22:27:23.542849+00:00
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
  - Captured: 2025-10-23T22:27:22.370986+00:00
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
  - Captured: 2025-10-23T22:27:20.915538+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_main_json.py:45:5
       |
    43 |     validate_payload(result, OUTPUT_SCHEMA)
    44 |
    …
