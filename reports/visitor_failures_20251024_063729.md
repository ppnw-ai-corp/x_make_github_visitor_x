# Visitor TODO Report

- Generated: 2025-10-24T06:37:29.269680+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 16
- Failing tools: 24
- Recorded failures: 24

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-c…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_clones_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:32:31.738492+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: error: Cannot find implementation or library stub for module named ".x_cls_make_github_clones_x"  [import-not-found]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:3: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_make_github_clones_x\x_cls_make_github_clones_x.py:19: error: Expression has type "Any"  [misc]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:20: error: Expression has type "Any"  [misc]
    x_make_github_clones_x\x_cls_make_github_clones_x.py:21: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:32:31.159093+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N812 Lowercase `x_cls_make_github_clones_x` imported as non-lowercase `GithubClonesRunner`
      --> tests\test_make_github_clones.py:12:5
       |
    10 | )
    11 | from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:32:29.456365+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N812 Lowercase `x_cls_make_github_clones_x` imported as non-lowercase `GithubClonesRunner`
      --> tests\test_make_github_clones.py:12:5
       |
    10 | )
    11 | from x_make_github_clones_x.x_cls_make_github_clones_x import (
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unuse…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:33:17.652343+00:00
  - Suggested action: Investigate
  - Stdout preview:
    runner.py:955: error: Redundant cast to "str"  [redundant-cast]
    runner.py:955: error: Expression has type "Any"  [misc]
    runner.py:956: error: Redundant cast to "str"  [redundant-cast]
    runner.py:959: error: Redundant cast to "str"  [redundant-cast]
    runner.py:960: error: Redundant cast to "str"  [redundant-cast]
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-e…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:33:42.610032+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:39: error: Argument 1 has incompatible type "Callable[[], dict[str, object]]"; expected "Callable[[VarArg(Never), KwArg(Never)], Never]"  [arg-type]
    tests\test_json_contracts.py:44: error: Argument 1 has incompatible type "Callable[[], dict[str, object]]"; expected "Callable[[VarArg(Never), KwArg(Never)], Never]"  [arg-type]
    tests\test_json_contracts.py:49: error: Argument 1 has incompatible type "Callable[[], dict[str, object]]"; expected "Callable[[VarArg(Never), KwArg(Never)], Never]"  [arg-type]
    Found 3 errors in 1 file (checked 9 source files)

- [ ] x_make_graphviz_x — ruff_check
  - Summary: ruff_check failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:33:41.984940+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
      --> tests\test_json_contracts.py:27:9
       |
    25 |         raw: object = json.load(handle)
    26 |     if not isinstance(raw, dict):
    …

- [ ] x_make_graphviz_x — ruff_fix
  - Summary: ruff_fix failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:33:40.532646+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY004 Prefer `TypeError` exception for invalid type
      --> tests\test_json_contracts.py:27:9
       |
    25 |         raw: object = json.load(handle)
    26 |     if not isinstance(raw, dict):
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at:…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-24T06:34:12.035459+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py	2025-10-24 06:28:52.026939+00:00
    +++ C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py	2025-10-24 06:34:11.874189+00:00
    @@ -31,14 +31,16 @@
     
     from x_make_markdown_x.json_contracts import ERROR_SCHEMA, INPUT_SCHEMA, OUTPUT_SCHEMA
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
  - Captured: 2025-10-24T06:34:12.854831+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_markdown_x.py:45: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:26: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:27: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:33: error: Argument 1 has incompatible type "Callable[[], dict[str, object]]"; expected "Callable[[VarArg(Never), KwArg(Never)], Never]"  [arg-type]
    tests\test_json_contracts.py:38: error: Argument 1 has incompatible type "Callable[[], dict[str, object]]"; expected "Callable[[VarArg(Never), KwArg(Never)], Never]"  [arg-type]
    …

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:34:42.814776+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_mermaid_x.py:87: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1547: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1550: error: Expression has type "Any"  [misc]
    x_cls_make_mermaid_x.py:1550: error: Expression type contains "Any" (has type "Any | None")  [misc]
    tests\test_json_contracts.py:27: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — black
  - Summary: black failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --chec…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-24T06:35:14.112293+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py	2025-10-24 06:28:56.000209+00:00
    +++ C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py	2025-10-24 06:35:13.953236+00:00
    @@ -25,10 +25,11 @@
         INPUT_SCHEMA,
         OUTPUT_SCHEMA,
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --n…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:35:15.075458+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:39: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:612: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:613: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:614: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:614: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC00…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:35:14.268828+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC004 Move import `typing.Protocol` out of type-checking block. Import is used for more than type hinting.
      --> x_cls_make_persistent_env_var_x.py:46:24
       |
    45 | if TYPE_CHECKING:
    46 |     from typing import Protocol
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,I…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-24T06:35:11.984667+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC004 Move import `typing.Protocol` out of type-checking block. Import is used for more than type hinting.
      --> x_cls_make_persistent_env_var_x.py:46:24
       |
    45 | if TYPE_CHECKING:
    46 |     from typing import Protocol
    …

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_pip_updates_x --strict --no-warn-unused-configs…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:35:40.629793+00:00
  - Suggested action: Investigate
  - Stdout preview:
    update_flow.py:43: error: Expression has type "Any"  [misc]
    update_flow.py:118: error: Expression has type "Any"  [misc]
    update_flow.py:590: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    update_flow.py:613: error: Expression type contains "Any" (has type "Any | None")  [misc]
    update_flow.py:614: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-un…
  - Command: C:\x_runner_x\artifacts\venvs\orchestrator_gui_py312\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-24T06:36:11.056610+00:00
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
  - Captured: 2025-10-24T06:36:22.699014+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-24 06:29:04.767468+00:00
    +++ C:\x_runner_x\x_make_py_venv_x\x_cls_make_py_venv_x.py	2025-10-24 06:36:22.547083+00:00
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
  - Captured: 2025-10-24T06:36:23.651743+00:00
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
  - Captured: 2025-10-24T06:36:57.888489+00:00
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
  - Captured: 2025-10-24T06:36:56.992518+00:00
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
  - Captured: 2025-10-24T06:36:55.210564+00:00
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
  - Captured: 2025-10-24T06:37:27.154666+00:00
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
  - Captured: 2025-10-24T06:37:26.346423+00:00
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
  - Captured: 2025-10-24T06:37:24.819954+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …
