# Visitor TODO Report

- Generated: 2025-10-18T01:27:23.958025+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 4
- Recorded failures: 4

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T01:27:00.104999+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:369: error: "TkFrame" has no attribute "grid_columnconfigure"  [attr-defined]
    x_cls_make_persistent_env_var_x.py:397: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:398: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:399: error: Expression type contains "Any" (has type "Callable[[], Any]")  [misc]
    x_cls_make_persistent_env_var_x.py:399: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — pyright
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T01:27:00.108585+00:00 duration: 2.540s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T01:27:02.648313+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py
      c:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py:369:15 - error: Cannot access attribute "grid_columnconfigure" for class "TkFrame"
      Â Â Attribute "grid_columnconfigure" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T01:26:59.002735+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `run_gui` is too complex (11 > 10)
       --> x_cls_make_persistent_env_var_x.py:260:9
        |
    258 |         return summaries, ok_all
    259 |
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T01:26:57.501058+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `run_gui` is too complex (11 > 10)
       --> x_cls_make_persistent_env_var_x.py:260:9
        |
    258 |         return summaries, ok_all
    259 |
    …
