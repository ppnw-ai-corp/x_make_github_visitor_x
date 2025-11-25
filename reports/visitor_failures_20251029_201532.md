# Visitor TODO Report

- Generated: 2025-10-29T20:15:32.224251+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 19
- Failing tools: 7
- Recorded failures: 7

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-29T20:14:13.349621+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_cli_dispatch.py:22: error: Expression type contains "Any" (has type "Any | bool")  [misc]
    tests\test_cli_dispatch.py:23: error: Expression type contains "Any" (has type "Any | bool")  [misc]
    tests\test_cli_dispatch.py:26: error: Expression has type "Any"  [misc]
    Found 3 errors in 1 file (checked 10 source files)

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T20:14:12.249755+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SIM108 Use ternary operator `quiet_attr = raw_quiet if isinstance(raw_quiet, bool) else bool(raw_quiet)` instead of `if`-`else`-block
      --> tests\test_cli_dispatch.py:23:9
       |
    21 |       def fake_run(self: module.x_cls_make_persistent_env_var_x) -> int:
    22 |           raw_quiet = getattr(self, "quiet", False)
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T20:14:10.438018+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SIM108 Use ternary operator `quiet_attr = raw_quiet if isinstance(raw_quiet, bool) else bool(raw_quiet)` instead of `if`-`else`-block
      --> tests\test_cli_dispatch.py:23:9
       |
    21 |       def fake_run(self: module.x_cls_make_persistent_env_var_x) -> int:
    22 |           raw_quiet = getattr(self, "quiet", False)
    …

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --sho…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-29T20:15:21.371471+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:558: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:727: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:727: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:778: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:781: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-29T20:15:21.378316+00:00 duration: 2.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-29T20:15:23.898031+00:00
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
  - Captured: 2025-10-29T20:15:20.312113+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `channel_id`
      --> tests\test_slack_dump_and_reset.py:34:9
       |
    32 |     def fetch_messages(
    33 |         self,
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T20:15:18.616341+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `channel_id`
      --> tests\test_slack_dump_and_reset.py:34:9
       |
    32 |     def fetch_messages(
    33 |         self,
    …
