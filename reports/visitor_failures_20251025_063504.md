# Visitor TODO Report

- Generated: 2025-10-25T06:35:04.615421+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 23
- Recorded failures: 23

- [ ] x_0_make_ppnw_dot_ai_x — mypy
  - Summary: mypy failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:30:02.777326+00:00
  - Suggested action: Investigate
  - Stdout preview:
    app\template_utils.py:47: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    app\template_utils.py:47: error: Expression type contains "Any" (has type "set[Any]")  [misc]
    app\template_utils.py:53: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    app\template_utils.py:63: error: Expression type contains "Any" (has type "set[Any]")  [misc]
    app\template_utils.py:63: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_check
  - Summary: ruff_check failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:29:58.081216+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> app\generator_app.py:5:29
      |
    3 | # pyright: reportAttributeAccessIssue=false, reportArgumentType=false
    4 | import sys
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:29:56.407661+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> app\generator_app.py:5:29
      |
    3 | # pyright: reportAttributeAccessIssue=false, reportArgumentType=false
    4 | import sys
    …

- [ ] x_legatus_acta_schedae_x — black
  - Summary: black failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-25T06:30:4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-25T06:30:52.044693+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\cli\main.py	2025-10-25 06:30:49.698528+00:00
    +++ C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\cli\main.py	2025-10-25 06:30:51.711617+00:00
    @@ -79,15 +79,24 @@
         cast("Any", _typer_main).get_click_type = _patched_get_click_type
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_acta_schedae_x\x_legatus_acta_schedae_x\interface\cli\main.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 94 files would be left unchanged.

- [ ] x_legatus_acta_schedae_x — ruff_check
  - Summary: ruff_check failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:30:52.352721+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (101 > 88)
      --> x_legatus_acta_schedae_x\interface\cli\main.py:84:89
       |
    82 | _patch_typer_optional_handling()
    83 |
    …

- [ ] x_legatus_acta_schedae_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_runner_x\x_legatus_acta_schedae_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_acta_schedae_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:30:49.738546+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (101 > 88)
      --> x_legatus_acta_schedae_x\interface\cli\main.py:84:89
       |
    82 | _patch_typer_optional_handling()
    83 |
    …

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:31:44.402639+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:13: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:16: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "main_json"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:17: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "resolve_workspace_root"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:20: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "synchronize_workspace"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:23: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:31:43.625866+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0414 Import alias does not rename original package
      --> x_make_github_clones_x\x_cls_make_github_clones_x.py:14:9
       |
    12 | if TYPE_CHECKING:  # static type checkers see precise symbols
    13 |     from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:31:41.898006+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0414 Import alias does not rename original package
      --> x_make_github_clones_x\x_cls_make_github_clones_x.py:14:9
       |
    12 | if TYPE_CHECKING:  # static type checkers see precise symbols
    13 |     from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:32:14.307875+00:00
  - Suggested action: Investigate
  - Stdout preview:
    runner.py:944: error: Redundant cast to "CompletedProcess[str]"  [redundant-cast]
    runner.py:959: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 13 source files)

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:32:51.355000+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:26: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:27: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 12 source files)

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:33:11.811403+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:1550: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1553: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1553: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:28: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:29: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:33:32.895750+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:613: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:614: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:615: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:615: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:1177: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:33:31.851553+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
       --> tests\test_json_contracts.py:179:5
        |
    179 | def test_main_json_persist_current_handles_missing(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:33:30.373426+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
       --> tests\test_json_contracts.py:179:5
        |
    179 | def test_main_json_persist_current_handles_missing(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:34:10.245301+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_mod_sideload_x.py:44: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:285: error: Returning Any from function declared to return "str | None"  [no-any-return]
    x_cls_make_py_mod_sideload_x.py:285: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:453: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:456: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:34:19.302804+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:304: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:584: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:585: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:586: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:590: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:34:40.635572+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:31: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:32: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:76: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:77: error: Expression has type "Any"  [misc]
    publish_flow.py:68: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:34:39.452929+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_main_json.py:43:9
       |
    41 |         name: str,
    42 |         value: object,
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:34:37.820099+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_main_json.py:43:9
       |
    41 |         name: str,
    42 |         value: object,
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T06:35:01.307066+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_yahw_x.py:144: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:24: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:26: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:35:00.549779+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T06:34:59.074271+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …
