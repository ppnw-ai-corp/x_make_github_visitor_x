# Visitor TODO Report

- Generated: 2025-10-29T14:41:04.569868+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 18
- Failing tools: 7
- Recorded failures: 7

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-29T14:39:45.493642+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:66: error: Explicit "Any" is not allowed  [explicit-any]
    x_cls_make_persistent_env_var_x.py:302: error: Expression type contains "Any" (has type "tuple[Any, Any]")  [misc]
    x_cls_make_persistent_env_var_x.py:302: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:305: error: Expression has type "Any"  [misc]
    x_cls_make_persistent_env_var_x.py:306: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T14:39:39.546378+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> tests\test_cli_dispatch.py:4:29
      |
    3 | import sys
    4 | from collections.abc import Callable
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T14:39:37.305816+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> tests\test_cli_dispatch.py:4:29
      |
    3 | import sys
    4 | from collections.abc import Callable
    …

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --n…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-29T14:40:43.919244+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:17: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_slack_dump_and_reset_x.py:17: error: Library stubs not installed for "requests"  [import-untyped]
    x_cls_make_slack_dump_and_reset_x.py:17: note: Error code "import-untyped" not covered by "type: ignore" comment
    x_cls_make_slack_dump_and_reset_x.py:17: note: Hint: "python3 -m pip install types-requests"
    x_cls_make_slack_dump_and_reset_x.py:17: note: (or run "mypy --install-types" to install all missing stub packages)
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-29T14:40:4…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-10-29T14:40:46.820648+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py:3:6 - error: Import "x_make_slack_dump_and_reset_z.x_cls_make_slack_dump_and_reset_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:3:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:5:6 - error: Import "x_make_slack_dump_and_reset_z.json_contracts" could not be resolved (reportMissingImports)
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_check
  - Summary: ruff_check failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T14:40:42.115024+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S108 Probable insecure usage of temporary file or directory: "/tmp"
      --> tests\test_json_contracts.py:17:29
       |
    15 |         "parameters": {
    16 |             "channels": ["C123"],
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.2
  - Captured: 2025-10-29T14:40:40.195686+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S108 Probable insecure usage of temporary file or directory: "/tmp"
      --> tests\test_json_contracts.py:17:29
       |
    15 |         "parameters": {
    16 |             "channels": ["C123"],
    …
