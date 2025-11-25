# Visitor TODO Report

- Generated: 2025-11-05T00:26:34.043133+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 24
- Failing tools: 20
- Recorded failures: 20

- [ ] x_legatus_celer_notitia_x — mypy
  - Summary: mypy failed for x_legatus_celer_notitia_x (exit 2) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_celer_notitia_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_celer_notitia_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-05T00:22:22.886580+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_celer_notitia_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_celer_notitia_x — ruff_check
  - Summary: ruff_check failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:22.196251+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> firmware\boot.py:19:20
       |
    17 |         Pin = _PinStub
    18 |
    …

- [ ] x_legatus_celer_notitia_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:19.900873+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> firmware\boot.py:19:20
       |
    17 |         Pin = _PinStub
    18 |
    …

- [ ] x_legatus_tactica_impetus_x — black
  - Summary: black failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-05T0…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-05T00:22:29.302392+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\mp_time.py	2025-11-03 17:04:44.736073+00:00
    +++ C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\mp_time.py	2025-11-05 00:22:28.865076+00:00
    @@ -17,10 +17,11 @@
         def sleep_ms(ms: int) -> None:
             _stdlib_time.sleep(ms / 1000.0)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\mp_time.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_calibrate_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_features_imu_x.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\boot.py
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\firmware\lib\x_cls_punch_classifier_x.py
    …

- [ ] x_legatus_tactica_impetus_x — mypy
  - Summary: mypy failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-05T00:22:30.895541+00:00
  - Suggested action: Investigate
  - Stdout preview:
    firmware\main.py:8: error: Skipping analyzing "machine": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    firmware\main.py:12: error: Cannot find implementation or library stub for module named "lib"  [import-not-found]
    firmware\main.py:14: error: Cannot find implementation or library stub for module named "lib.mp_time"  [import-not-found]
    firmware\main.py:15: error: Cannot find implementation or library stub for module named "lib.types"  [import-not-found]
    firmware\main.py:16: error: Cannot find implementation or library stub for module named "lib.x_cls_calibrate_x"  [import-not-found]
    …

- [ ] x_legatus_tactica_impetus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:29.610513+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:32:22
       |
    31 | class _WLAN(Protocol):
    32 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_tactica_impetus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:27.113027+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:32:22
       |
    31 | class _WLAN(Protocol):
    32 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_vigil_nexus_x — mypy
  - Summary: mypy failed for x_legatus_vigil_nexus_x (exit 2) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-05T00:22:37.428294+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_vigil_nexus_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_vigil_nexus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:36.699298+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `data` before `return` statement
      --> clients\session_client.py:71:16
       |
    69 |         response = await self._authorized_post(f"/v1/device/{device_id}/session", None)
    70 |         data = response.json()
    …

- [ ] x_legatus_vigil_nexus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:34.561560+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `data` before `return` statement
      --> clients\session_client.py:71:16
       |
    69 |         response = await self._authorized_post(f"/v1/device/{device_id}/session", None)
    70 |         data = response.json()
    …

- [ ] x_make_contract_validators_x — ruff_check
  - Summary: ruff_check failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:46.617889+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib` into a type-checking block
     --> tests\test_contract_validators.py:5:8
      |
    3 | # ruff: noqa: S101
    4 | import json
    …

- [ ] x_make_contract_validators_x — ruff_fix
  - Summary: ruff_fix failed for x_make_contract_validators_x (exit 1) cwd: C:\x_runner_x\x_make_contract_validators_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_contract_validators_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:22:44.721193+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `pathlib` into a type-checking block
     --> tests\test_contract_validators.py:5:8
      |
    3 | # ruff: noqa: S101
    4 | import json
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:24:59.526292+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_pip_updates_x.py:173:21
        |
    171 |     @staticmethod
    172 |     def _run(cmd: Sequence[str]) -> RunResult:
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-05T00:24:57.275765+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S603 `subprocess` call: check for execution of untrusted input
       --> x_cls_make_pip_updates_x.py:173:21
        |
    171 |     @staticmethod
    172 |     def _run(cmd: Sequence[str]) -> RunResult:
    …

- [ ] x_make_progress_board_x — black
  - Summary: black failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-05T00:25:12.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-05T00:25:14.638598+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_progress_board_x\cli.py	2025-10-30 21:29:12.888265+00:00
    +++ C:\x_runner_x\x_make_progress_board_x\cli.py	2025-11-05 00:25:13.987019+00:00
    @@ -25,11 +25,13 @@
         return stages
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_progress_board_x\cli.py
    would reformat C:\x_runner_x\x_make_progress_board_x\tests\test_entry_module.py
    would reformat C:\x_runner_x\x_make_progress_board_x\x_cls_make_progress_board_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-05T00:25:16.403232+00:00
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
  - Captured: 2025-11-05T00:25:15.065806+00:00
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
  - Captured: 2025-11-05T00:25:12.493651+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
     --> cli.py:7:29
      |
    5 | import argparse
    6 | import threading
    …

- [ ] x_make_slack_dump_and_reset_z — black
  - Summary: black failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-05T00:26:24.635808+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-11-04 23:56:34.972762+00:00
    +++ C:\x_runner_x\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-11-05 00:26:24.304738+00:00
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
  - Captured: 2025-11-05T00:26:26.994414+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:676: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1074: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1087: error: Expression has type "Any"  [misc]
    …
