# Visitor TODO Report

- Generated: 2025-10-18T00:23:35.848565+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 3
- Recorded failures: 3

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T00:23:10.839507+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "CommandError"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "run_command"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:238: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:239: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:240: error: Expression has type "Any"  [misc]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-18T00:23:10.843333+00:00 duration: 4.251…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T00:23:15.094423+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\interface\gui\commit.py
      c:\x_runner_x\x_0_make_all_x\interface\gui\commit.py:9:29 - error: "run_command" is unknown import symbol (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-18T00:23:28.042800+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T00:23:30.290792+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\update_flow.py
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:15:5 - error: "CommandError" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:19:5 - error: "run_command" is unknown import symbol (reportAttributeAccessIssue)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
