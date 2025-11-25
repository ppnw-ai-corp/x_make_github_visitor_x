# Visitor TODO Report

- Generated: 2025-10-16T00:26:06.842693+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 1
- Recorded failures: 1

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-16T00:25:55.236080+00:00 duration: 1.462s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-16T00:25:56.698445+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\publish_flow.py
      c:\x_runner_x\x_make_pypi_x\publish_flow.py:700:53 - error: Type "tuple[dict[str, str | None], dict[str, dict[str, object]], Unknown | Path | None]" is not assignable to return type "tuple[dict[str, str | None], dict[str, dict[str, object]], Path]"
      Â Â Type "Unknown | Path | None" is not assignable to type "Path"
      Â Â Â Â "None" is not assignable to "Path" (reportReturnType)
    1 error, 0 warnings, 0 informations
