# Visitor TODO Report

- Generated: 2025-10-29T19:46:10.258678+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 19
- Failing tools: 6
- Recorded failures: 6

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T19:41:53.521750+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_progress_board_flags.py:20:12
       |
    20 | def expect(condition: bool, message: str) -> None:
       |            ^^^^^^^^^
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T19:41:50.725894+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> tests\test_progress_board_flags.py:20:12
       |
    20 | def expect(condition: bool, message: str) -> None:
       |            ^^^^^^^^^
    …

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --sho…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-29T19:46:02.825663+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:554: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:723: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:723: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:774: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:777: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-29T19:46:02.831973+00:00 duration: 2.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-29T19:46:05.233904+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py:3:6 - error: Import "x_make_slack_dump_and_reset_z.x_cls_make_slack_dump_and_reset_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:3:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:5:6 - error: Import "x_make_slack_dump_and_reset_z.json_contracts" could not be resolved (reportMissingImports)
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_check
  - Summary: ruff_check failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T19:46:01.916321+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `identifier`
      --> tests\test_slack_dump_and_reset.py:26:31
       |
    24 |         self.deleted_files: list[str] = []
    25 |
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T19:46:00.168629+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `identifier`
      --> tests\test_slack_dump_and_reset.py:26:31
       |
    24 |         self.deleted_files: list[str] = []
    25 |
    …
