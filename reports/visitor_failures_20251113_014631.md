# Visitor TODO Report

- Generated: 2025-11-13T01:46:31.980786+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 13
- Recorded failures: 13

- [ ] x_make_contract_validators_x — ruff_check
  - Summary: ruff_check failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:38.334523+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0415 `import` should be at the top-level of a file
      --> x_cls_make_contract_validators_x.py:47:9
       |
    45 | def _load_validator() -> type[_DraftValidatorProtocol]:
    46 |     try:
    …

- [ ] x_make_contract_validators_x — ruff_fix
  - Summary: ruff_fix failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:38.189338+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLC0415 `import` should be at the top-level of a file
      --> x_cls_make_contract_validators_x.py:47:9
       |
    45 | def _load_validator() -> type[_DraftValidatorProtocol]:
    46 |     try:
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-13T01:45:38.79…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-13T01:45:40.790383+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\scripts\package_telemetry_vector.py	2025-11-13 01:16:51.901830+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\scripts\package_telemetry_vector.py	2025-11-13 01:45:40.185963+00:00
    @@ -14,11 +14,13 @@
     
     def run(cmd: list[str]) -> None:
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_clones_x\scripts\package_telemetry_vector.py
    would reformat C:\x_runner_x\x_make_github_clones_x\tests\test_telemetry_vector.py
    would reformat C:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-13T01:45:40.954963+00:00 duration: 3.029s tool_vers…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-13T01:45:43.980535+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py
      c:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py:14:33 - error: "ConfigDict" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py:14:52 - error: "ValidationError" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py:14:69 - error: "field_validator" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\src\x_make_telemetry_vector_x\__init__.py:24:21 - error: Type "object" is not assignable to declared type "str"
    …

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:40.943172+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `scripts\package_telemetry_vector.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> scripts\package_telemetry_vector.py:1:1
    
    S603 `subprocess` call: check for execution of untrusted input
      --> scripts\package_telemetry_vector.py:17:17
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:38.792054+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `scripts\package_telemetry_vector.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> scripts\package_telemetry_vector.py:1:1
    
    S603 `subprocess` call: check for execution of untrusted input
      --> scripts\package_telemetry_vector.py:17:17
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:54.050241+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ICN001 `tkinter` should be imported as `tk`
      --> x_cls_make_persistent_env_var_x.py:32:27
       |
    30 | else:  # pragma: no cover - import guard to support headless environments
    31 |     try:
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:53.896064+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ICN001 `tkinter` should be imported as `tk`
      --> x_cls_make_persistent_env_var_x.py:32:27
       |
    30 | else:  # pragma: no cover - import guard to support headless environments
    31 |     try:
    …

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-13T01:45:59.100419+00:00
  - Suggested action: Investigate
  - Stdout preview:
    cli.py:38: error: Expression has type "Any"  [misc]
    Found 1 error in 1 file (checked 10 source files)

- [ ] x_make_progress_board_x — ruff_check
  - Summary: ruff_check failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:58.322720+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> controller.py:7:21
      |
    5 | import threading
    6 | from dataclasses import dataclass
    …

- [ ] x_make_progress_board_x — ruff_fix
  - Summary: ruff_fix failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:45:58.165822+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> controller.py:7:21
      |
    5 | import threading
    6 | from dataclasses import dataclass
    …

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:46:28.994523+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0911 Too many return statements (7 > 6)
      --> x_cls_make_yahw_x.py:90:5
       |
    90 | def _maybe_generate_projection(
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.4
  - Captured: 2025-11-13T01:46:27.214388+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0911 Too many return statements (7 > 6)
      --> x_cls_make_yahw_x.py:90:5
       |
    90 | def _maybe_generate_projection(
       |     ^^^^^^^^^^^^^^^^^^^^^^^^^^
    …
