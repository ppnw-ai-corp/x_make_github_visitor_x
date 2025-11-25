# Visitor TODO Report

- Generated: 2025-10-25T04:01:48.193378+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 25
- Recorded failures: 25

- [ ] x_0_make_ppnw_dot_ai_x — black
  - Summary: black failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff s…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-25T03:56:54.027201+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\template_utils.py	2025-10-25 03:56:52.782465+00:00
    +++ C:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\template_utils.py	2025-10-25 03:56:53.868557+00:00
    @@ -25,11 +25,13 @@
             if not RE_MARKDOWN.match(str(p)):
                 continue
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\template_utils.py
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 2 files would be left unchanged.

- [ ] x_0_make_ppnw_dot_ai_x — mypy
  - Summary: mypy failed for x_0_make_ppnw_dot_ai_x (exit 2) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-c…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T03:56:54.505027+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_0_make_ppnw_dot_ai_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_0_make_ppnw_dot_ai_x — pyright
  - Summary: pyright failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m pyright . --level error started_at: 2025-10-25T03:56:54.511485…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-25T03:56:56.663959+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py
      c:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py:9:5 - error: "QDialog" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py:10:5 - error: "QFormLayout" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py:11:5 - error: "QGridLayout" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_0_make_ppnw_dot_ai_x\app\generator_app.py:12:5 - error: "QGroupBox" is unknown import symbol (reportAttributeAccessIssue)
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_check
  - Summary: ruff_check failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T03:56:54.167573+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PGH003 Use specific rule codes when ignoring type issues
      --> app\generator_app.py:40:39
       |
    39 |     _sys.path.append(str(Path(__file__).resolve().parents[1]))
    40 |     from app.template_utils import (  # type: ignore
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T03:56:52.825842+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PGH003 Use specific rule codes when ignoring type issues
      --> app\generator_app.py:40:39
       |
    39 |     _sys.path.append(str(Path(__file__).resolve().parents[1]))
    40 |     from app.template_utils import (  # type: ignore
    …

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-c…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T03:58:20.391967+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:13: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "RepoRecord"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:16: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "main_json"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:17: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "resolve_workspace_root"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:20: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "synchronize_workspace"  [attr-defined]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:23: error: Module "x_make_github_clones_x.x_cls_make_github_clones_x" has no attribute "x_cls_make_github_clones_x"  [attr-defined]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T03:58:19.737893+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0414 Import alias does not rename original package
      --> x_make_github_clones_x\x_cls_make_github_clones_x.py:14:9
       |
    12 | if TYPE_CHECKING:  # static type checkers see precise symbols
    13 |     from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T03:58:17.985751+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0414 Import alias does not rename original package
      --> x_make_github_clones_x\x_cls_make_github_clones_x.py:14:9
       |
    12 | if TYPE_CHECKING:  # static type checkers see precise symbols
    13 |     from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unuse…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T03:58:49.762790+00:00
  - Suggested action: Investigate
  - Stdout preview:
    runner.py:944: error: Redundant cast to "CompletedProcess[str]"  [redundant-cast]
    runner.py:959: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 13 source files)

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-25T03:59:25.723311+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py	2025-10-25 03:55:46.502804+00:00
    +++ C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py	2025-10-25 03:59:25.580928+00:00
    @@ -447,10 +447,11 @@
             blocks_obj, (str, bytes, bytearray)
         ):
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-e…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T03:59:26.757925+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:26: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:27: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 12 source files)

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-25T03:59:48.697923+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-25 03:55:48.499348+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-25 03:59:48.538318+00:00
    @@ -87,10 +87,11 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T03:59:49.649991+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:1549: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1552: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1552: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:28: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:29: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --n…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T04:00:11.197652+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:613: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:614: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:615: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:615: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:1177: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC00…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:00:10.356448+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
       --> tests\test_json_contracts.py:179:5
        |
    179 | def test_main_json_persist_current_handles_missing(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,I…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:00:08.578849+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (51 > 50)
       --> tests\test_json_contracts.py:179:5
        |
    179 | def test_main_json_persist_current_handles_missing(
        |     ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-un…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T04:00:51.017509+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_mod_sideload_x.py:44: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:285: error: Returning Any from function declared to return "str | None"  [no-any-return]
    x_cls_make_py_mod_sideload_x.py:285: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:453: error: Expression has type "Any"  [misc]
    x_cls_make_py_mod_sideload_x.py:456: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_py_venv_x — black
  - Summary: black failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-25T04:01:00.459772+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-25 03:55:58.510059+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-25 04:01:00.365926+00:00
    @@ -567,13 +567,11 @@
             "Sequence[str] | None", getattr(namespace, "requirements", None)
         )
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 1 file would be left unchanged.

- [ ] x_make_py_venv_x — mypy
  - Summary: mypy failed for x_make_py_venv_x (exit 1) cwd: C:\x_runner_x\x_make_py_venv_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_venv_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_venv_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T04:01:01.353413+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_py_venv_x.py:304: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:586: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:587: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:588: error: Expression has type "Any"  [misc]
    x_cls_make_py_venv_x.py:592: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T04:01:24.345104+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:31: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:32: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:76: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:77: error: Expression has type "Any"  [misc]
    publish_flow.py:68: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:01:23.405203+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_main_json.py:43:9
       |
    41 |         name: str,
    42 |         value: object,
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:01:21.630963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_main_json.py:43:9
       |
    41 |         name: str,
    42 |         value: object,
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-25T04:01:45.688812+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_yahw_x.py:144: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression has type "Any"  [misc]
    x_cls_make_yahw_x.py:147: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:24: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:26: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --tar…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:01:44.965619+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 -…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-25T04:01:43.314432+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …
