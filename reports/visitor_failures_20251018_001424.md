# Visitor TODO Report

- Generated: 2025-10-18T00:14:24.463182+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 4
- Recorded failures: 4

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T00:13:47.847839+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "CommandError"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "log_error"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "log_info"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:14: error: Module "x_make_common_x" has no attribute "run_command"  [attr-defined]
    C:\x_runner_x\x_make_pip_updates_x\update_flow.py:238: error: Expression has type "Any"  [misc]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-18T00:13:47.853472+00:00 duration: 3.709…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T00:13:51.562417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\interface\gui\app.py
      c:\x_runner_x\x_0_make_all_x\interface\gui\app.py:16:29 - error: "register_listener" is unknown import symbol (reportAttributeAccessIssue)
    c:\x_runner_x\x_0_make_all_x\interface\gui\commit.py
      c:\x_runner_x\x_0_make_all_x\interface\gui\commit.py:9:29 - error: "run_command" is unknown import symbol (reportAttributeAccessIssue)
    c:\x_runner_x\x_0_make_all_x\manifest.py
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_github_visitor_x — pyright
  - Summary: pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-18T00:14:02.982735+00:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T00:14:06.063649+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py
      c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:16:5 - error: "configure_event_sink" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:17:5 - error: "emit_event" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:18:5 - error: "ensure_workspace_on_syspath" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_visitor_x\inspection_flow.py:19:5 - error: "get_logger" is unknown import symbol (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-18T00:14:16.214424+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T00:14:18.500116+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\update_flow.py
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:15:5 - error: "CommandError" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:17:5 - error: "log_error" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:18:5 - error: "log_info" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\update_flow.py:19:5 - error: "run_command" is unknown import symbol (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
