# Visitor TODO Report

- Generated: 2025-10-31T03:04:46.908890+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 22
- Failing tools: 19
- Recorded failures: 19

- [ ] x_legatus_tactica_impetus_x — black
  - Summary: black failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-31T0…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-31T02:53:43.722615+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_punch_classifier_x.py	2025-10-31 02:27:57.459385+00:00
    +++ C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_punch_classifier_x.py	2025-10-31 02:53:43.151630+00:00
    @@ -12,11 +12,13 @@
     
         def update_orientation(self, gravity, forward_axis):
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_punch_classifier_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_calibrate_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_sensor_bno055_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_punch_detector_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_display_tft_x.py
    …

- [ ] x_legatus_tactica_impetus_x — mypy
  - Summary: mypy failed for x_legatus_tactica_impetus_x (exit 2) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-31T02:53:44.844285+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_tactica_impetus_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_tactica_impetus_x — pyright
  - Summary: pyright failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-31T02:53:44.850595+00:00 duration: 4.362s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-31T02:53:49.209310+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py
      c:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py:35:21 - error: "ticks_add" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py:35:36 - error: "ticks_ms" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py:36:43 - error: "ticks_diff" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py:36:69 - error: "ticks_ms" is not a known attribute of "None" (reportOptionalMemberAccess)
    …

- [ ] x_legatus_tactica_impetus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:53:43.994607+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `firmware\boot.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> firmware\boot.py:1:1
    
    PGH003 Use specific rule codes when ignoring type issues
      --> firmware\boot.py:8:21
    …

- [ ] x_legatus_tactica_impetus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:53:40.873586+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `firmware\boot.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> firmware\boot.py:1:1
    
    PGH003 Use specific rule codes when ignoring type issues
      --> firmware\boot.py:8:21
    …

- [ ] x_make_cli_scaffolder_x — black
  - Summary: black failed for x_make_cli_scaffolder_x (exit 1) cwd: C:\x_runner_x\x_make_cli_scaffolder_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-31T02:53:55.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_cli_scaffolder_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-31T02:53:57.750267+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_cli_scaffolder_x\tests\test_scaffolder.py	2025-10-30 21:27:03.743331+00:00
    +++ C:\x_runner_x\x_make_cli_scaffolder_x\tests\test_scaffolder.py	2025-10-31 02:53:57.097203+00:00
    @@ -25,13 +25,15 @@
             if path.is_file()
         }
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_cli_scaffolder_x\tests\test_scaffolder.py
    would reformat C:\x_runner_x\x_make_cli_scaffolder_x\x_cls_make_cli_scaffolder_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 4 files would be left unchanged.

- [ ] x_make_cli_scaffolder_x — mypy
  - Summary: mypy failed for x_make_cli_scaffolder_x (exit 1) cwd: C:\x_runner_x\x_make_cli_scaffolder_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_cli_scaffolder_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_cli_scaffolder_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_cli_scaffolder_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-31T02:54:05.320500+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\conftest.py:9: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_cli_scaffolder_x.py:328: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    x_cls_make_cli_scaffolder_x.py:329: error: Expression type contains "Any" (has type "tuple[str, Any]")  [misc]
    x_cls_make_cli_scaffolder_x.py:329: error: Expression has type "Any"  [misc]
    x_cls_make_cli_scaffolder_x.py:330: error: Expression type contains "Any" (has type "tuple[str, Any]")  [misc]
    …

- [ ] x_make_cli_scaffolder_x — ruff_check
  - Summary: ruff_check failed for x_make_cli_scaffolder_x (exit 1) cwd: C:\x_runner_x\x_make_cli_scaffolder_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_cli_scaffolder_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:53:57.981295+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> tests\conftest.py:3:21
      |
    1 | from __future__ import annotations
    2 |
    …

- [ ] x_make_cli_scaffolder_x — ruff_fix
  - Summary: ruff_fix failed for x_make_cli_scaffolder_x (exit 1) cwd: C:\x_runner_x\x_make_cli_scaffolder_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_cli_scaffolder_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:53:55.424336+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> tests\conftest.py:3:21
      |
    1 | from __future__ import annotations
    2 |
    …

- [ ] x_make_contract_validators_x — black
  - Summary: black failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-31…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-31T02:54:21.949069+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_contract_validators_x\tests\test_contract_validators.py	2025-10-30 21:27:14.068087+00:00
    +++ C:\x_runner_x\x_make_contract_validators_x\tests\test_contract_validators.py	2025-10-31 02:54:21.502365+00:00
    @@ -74,11 +74,13 @@
         result = run(payload)
         assert result["status"] == "success"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_contract_validators_x\tests\test_contract_validators.py
    would reformat C:\x_runner_x\x_make_contract_validators_x\x_cls_make_contract_validators_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 2 files would be left unchanged.

- [ ] x_make_contract_validators_x — mypy
  - Summary: mypy failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_contract_validators_x --strict --no-warn-unused-configs --show-e…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_contract_validators_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-31T02:54:23.625505+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_contract_validators_x.py:30: error: Returning Any from function declared to return "type[_DraftValidatorProtocol]"  [no-any-return]
    x_cls_make_contract_validators_x.py:30: error: Expression has type "Any"  [misc]
    x_cls_make_contract_validators_x.py:91: error: Expression type contains "Any" (has type "Any | str")  [misc]
    x_cls_make_contract_validators_x.py:92: error: Expression type contains "Any" (has type "tuple[Any, ...]")  [misc]
    x_cls_make_contract_validators_x.py:92: error: Expression type contains "Any" (has type "Any | Iterable[Any]")  [misc]
    …

- [ ] x_make_contract_validators_x — ruff_check
  - Summary: ruff_check failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:54:22.187022+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> tests\test_contract_validators.py:4:21
      |
    3 | import json
    4 | from pathlib import Path
    …

- [ ] x_make_contract_validators_x — ruff_fix
  - Summary: ruff_fix failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T02:54:19.463622+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib.Path` into a type-checking block
     --> tests\test_contract_validators.py:4:21
      |
    3 | import json
    4 | from pathlib import Path
    …

- [ ] x_make_progress_board_x — black
  - Summary: black failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-31T03:02:57.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-31T03:02:59.145210+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_progress_board_x\cli.py	2025-10-30 21:29:12.888265+00:00
    +++ C:\x_runner_x\x_make_progress_board_x\cli.py	2025-10-31 03:02:58.762503+00:00
    @@ -25,11 +25,13 @@
         return stages
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_progress_board_x\cli.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 4 files would be left unchanged.

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-31T03:03:01.171417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    progress_board_widget.py:21: error: Explicit "Any" is not allowed  [explicit-any]
    progress_board_widget.py:21: error: Expression has type "Any"  [misc]
    progress_board_widget.py:22: error: Explicit "Any" is not allowed  [explicit-any]
    progress_board_widget.py:22: error: Expression has type "Any"  [misc]
    progress_board_widget.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_make_progress_board_x — ruff_check
  - Summary: ruff_check failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T03:02:59.562081+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
     --> cli.py:7:29
      |
    5 | import argparse
    6 | import threading
    …

- [ ] x_make_progress_board_x — ruff_fix
  - Summary: ruff_fix failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-10-31T03:02:57.105110+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
     --> cli.py:7:29
      |
    5 | import argparse
    6 | import threading
    …

- [ ] x_make_slack_dump_and_reset_z — black
  - Summary: black failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-10-31T03:04:39.009269+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-10-30 18:16:19.336325+00:00
    +++ C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-10-31 03:04:38.696267+00:00
    @@ -886,11 +886,11 @@
                 raise RuntimeError(message)
             return Path(archive_root_raw).expanduser().resolve()
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --sho…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-31T03:04:40.574254+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:120: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_slack_dump_and_reset_x.py:676: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1074: error: Expression has type "Any"  [misc]
    …
