# Visitor TODO Report

- Generated: 2025-10-18T02:11:49.263451+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 9
- Recorded failures: 9

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T02:11:21.843725+00:00 durat…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T02:11:25.296586+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py	2025-10-18 02:04:30.533306+00:00
    +++ C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py	2025-10-18 02:11:23.310223+00:00
    @@ -72,11 +72,13 @@
         make_all.main(["--no-gui"])
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py
    would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 17 files would be left unchanged.

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T02:11:26.367520+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_all_x.py:1739: error: Argument 2 to "commit_all_repositories" has incompatible type "str | None"; expected "str"  [arg-type]
    tests\test_make_all_commit_cli.py:21: error: Function is missing a type annotation for one or more arguments  [no-untyped-def]
    tests\test_make_all_commit_cli.py:28: error: Unused "type: ignore" comment  [unused-ignore]
    tests\test_make_all_commit_cli.py:28: error: Function is missing a return type annotation  [no-untyped-def]
    tests\test_make_all_commit_cli.py:28: note: Error code "no-untyped-def" not covered by "type: ignore" comment
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T02:11:26.371220+00:00 duration: 3.344s tool_version: pyright 1.1…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T02:11:29.715271+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py
      c:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py:128:76 - error: Cannot access attribute "value" for class "None"
      Â Â Attribute "value" is unknown (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T02:11:25.436894+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `monkeypatch`
      --> tests\test_make_all_commit_cli.py:21:45
       |
    21 | def test_main_runs_commit_when_flag_present(monkeypatch, tmp_path: Path) -> None:
       |                                             ^^^^^^^^^^^
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T02:11:21.836136+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `monkeypatch`
      --> tests\test_make_all_commit_cli.py:21:45
       |
    21 | def test_main_runs_commit_when_flag_present(monkeypatch, tmp_path: Path) -> None:
       |                                             ^^^^^^^^^^^
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T02:11:43.031404+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_persistent_env_var_x.py:369: error: "TkFrame" has no attribute "grid_columnconfigure"  [attr-defined]
    x_cls_make_persistent_env_var_x.py:397: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:398: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_persistent_env_var_x.py:399: error: Expression type contains "Any" (has type "Callable[[], Any]")  [misc]
    x_cls_make_persistent_env_var_x.py:399: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — pyright
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T02:11:43.037206+00:00 duration: 2.163s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T02:11:45.200560+00:00
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
  - Captured: 2025-10-18T02:11:42.320142+00:00
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
  - Captured: 2025-10-18T02:11:40.937026+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `run_gui` is too complex (11 > 10)
       --> x_cls_make_persistent_env_var_x.py:260:9
        |
    258 |         return summaries, ok_all
    259 |
    …
