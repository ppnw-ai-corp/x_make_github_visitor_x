# Visitor TODO Report

- Generated: 2025-11-13T02:50:50.992769+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 1
- Recorded failures: 1

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-13T02:50:11.446489+00:00 duration: 3.203s tool_vers…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-13T02:50:14.648772+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\tests\test_telemetry_vector.py
      c:\x_runner_x\x_make_github_clones_x\tests\test_telemetry_vector.py:8:14 - error: Cannot access attribute "skip" for class "_MarkModule"
      Â Â Attribute "skip" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations
