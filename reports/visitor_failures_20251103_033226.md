# Visitor TODO Report

- Generated: 2025-11-03T03:32:26.519315+00:00
- Workspace: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 24
- Failing tools: 53
- Recorded failures: 53

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environ…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-03T03:29:20.591882+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\services.py	2025-11-03 03:27:48.051227+00:00
    +++ C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\services.py	2025-11-03 03:29:16.235566+00:00
    @@ -59,11 +59,13 @@
         def load_environment(self, name: str) -> dict[str, Any]:
             """Load a single environment's metadata."""
    …
  - Stderr preview:
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\services.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\naked_entry.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\dialogs.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\app.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\x_cls_make_all_x.py
    …

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environm…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_0_make_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:29:36.951194+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_forceit.py:11: error: Cannot find implementation or library stub for module named "_pytest.capture"  [import-not-found]
    tests\test_forceit.py:11: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_forceit.py:12: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_forceit.py:88: error: Argument 2 to "test_main_handles_copy_error" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_forceit.py:88: error: Argument 3 to "test_main_handles_copy_error" becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\envir…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:29:48.410306+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\app.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\app.py:29:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\app.py:30:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\dialogs.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x\interface\gui\environment_studio\dialogs.py:9:6 - error: Import "PySide6" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config contains unrecognized setting "diagnosticSeverityOverrides".

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\en…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:29:20.961628+00:00
  - Suggested action: Investigate
  - Stdout preview:
    BLE001 Do not catch blind exception: `Exception`
      --> interface\gui\environment_studio\app.py:93:16
       |
    91 |         try:
    92 |             result = self._function(*self._args, **self._kwargs)
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\envi…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_all_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:29:13.779782+00:00
  - Suggested action: Investigate
  - Stdout preview:
    BLE001 Do not catch blind exception: `Exception`
      --> interface\gui\environment_studio\app.py:93:16
       |
    91 |         try:
    92 |             result = self._function(*self._args, **self._kwargs)
    …

- [ ] x_0_make_ppnw_dot_ai_x — pyright
  - Summary: pyright failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_ppnw_dot_ai_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e25…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_ppnw_dot_ai_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:29:58.932484+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_ppnw_dot_ai_x\app\generator_app.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_make_ppnw_dot_ai_x\app\generator_app.py:11:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_0_run_all_x — black
  - Summary: black failed for x_0_run_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environme…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-03T03:30:02.958474+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py	2025-11-03 03:27:51.748296+00:00
    +++ C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py	2025-11-03 03:30:02.809508+00:00
    @@ -1261,11 +1261,13 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 4 files would be left unchanged.

- [ ] x_0_run_all_x — mypy
  - Summary: mypy failed for x_0_run_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environmen…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_0_run_all_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:30:10.533923+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_run_all_x.py:201: error: Explicit "Any" is not allowed  [explicit-any]
    x_cls_run_all_x.py:210: error: Expression type contains "Any" (has type "tuple[str, dict[Any, Any]]")  [misc]
    x_cls_run_all_x.py:210: error: Expression type contains "Any" (has type "dict[Any, Any]")  [misc]
    x_cls_run_all_x.py:216: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    x_cls_run_all_x.py:217: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    …

- [ ] x_0_run_all_x — pyright
  - Summary: pyright failed for x_0_run_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environ…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:13.682237+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\run_environment_studio.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\run_environment_studio.py:12:6 - error: Import "x_0_make_all_x.interface.gui.environment_studio.app" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py:25:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x\x_cls_run_all_x.py:26:6 - error: Import "x_make_common_x.x_env_x" could not be resolved (reportMissingImports)
    …

- [ ] x_0_run_all_x — ruff_check
  - Summary: ruff_check failed for x_0_run_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\envi…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:03.272763+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> run_environment_studio.py:12:1
       |
    10 |       sys.path.insert(0, str(WORKSPACE_ROOT))
    11 |
    …

- [ ] x_0_run_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_run_all_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\enviro…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_0_run_all_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:29:59.996123+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> run_environment_studio.py:12:1
       |
    10 |       sys.path.insert(0, str(WORKSPACE_ROOT))
    11 |
    …

- [ ] x_legatus_acta_schedae_x — pyright
  - Summary: pyright failed for x_legatus_acta_schedae_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda0…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:20.871306+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x\tests\test_automation_service.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x\tests\test_automation_service.py:7:8 - error: Import "httpx" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x\tests\test_card_action_service.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x\tests\test_card_action_service.py:6:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x\tests\test_review_service.py
    …
  - Stderr preview:
    venv .venv subdirectory not found in venv path c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_acta_schedae_x.

- [ ] x_legatus_celer_notitia_x — mypy
  - Summary: mypy failed for x_legatus_celer_notitia_x (exit 2) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_legatus_celer_notitia_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:30:22.346963+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_celer_notitia_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_celer_notitia_x — ruff_check
  - Summary: ruff_check failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a4…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:21.747037+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> firmware\boot.py:19:20
       |
    17 |         Pin = _PinStub
    18 |
    …

- [ ] x_legatus_celer_notitia_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41f…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:21.468612+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> firmware\boot.py:19:20
       |
    17 |         Pin = _PinStub
    18 |
    …

- [ ] x_legatus_tactica_impetus_x — mypy
  - Summary: mypy failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41f…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:30:29.254081+00:00
  - Suggested action: Investigate
  - Stdout preview:
    firmware\lib\x_cls_display_tft_x.py:12: error: Name "_st7789_module" already defined on line 10  [no-redef]
    firmware\lib\x_cls_display_tft_x.py:12: note: Error code "no-redef" not covered by "type: ignore" comment
    firmware\lib\x_cls_display_tft_x.py:18: error: Name "_font_small_module" already defined on line 16  [no-redef]
    firmware\lib\x_cls_display_tft_x.py:18: note: Error code "no-redef" not covered by "type: ignore" comment
    firmware\lib\x_cls_display_tft_x.py:24: error: Name "_font_big_module" already defined on line 22  [no-redef]
    …

- [ ] x_legatus_tactica_impetus_x — pyright
  - Summary: pyright failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:32.263424+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x\firmware\lib\mp_time.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x\firmware\lib\mp_time.py:4:12 - error: Import "utime" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_legatus_tactica_impetus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c40…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:26.637911+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:35:22
       |
    34 | class _WLAN(Protocol):
    35 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_tactica_impetus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:26.357060+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:35:22
       |
    34 | class _WLAN(Protocol):
    35 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_vigil_nexus_x — mypy
  - Summary: mypy failed for x_legatus_vigil_nexus_x (exit 2) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e258…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:30:33.738281+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_vigil_nexus_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_vigil_nexus_x — pyright
  - Summary: pyright failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:37.150672+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x\clients\session_client.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x\clients\session_client.py:13:8 - error: Import "httpx" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x\clients\session_client.py:14:8 - error: Import "websockets" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x\control_plane\models.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x\control_plane\models.py:3:6 - error: Import "pydantic" could not be resolved (reportMissingImports)
    …

- [ ] x_legatus_vigil_nexus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:33.110836+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `data` before `return` statement
      --> clients\session_client.py:71:16
       |
    69 |         response = await self._authorized_post(f"/v1/device/{device_id}/session", None)
    70 |         data = response.json()
    …

- [ ] x_legatus_vigil_nexus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:30:32.827628+00:00
  - Suggested action: Investigate
  - Stdout preview:
    RET504 Unnecessary assignment to `data` before `return` statement
      --> clients\session_client.py:71:16
       |
    69 |         response = await self._authorized_post(f"/v1/device/{device_id}/session", None)
    70 |         data = response.json()
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\enviro…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_common_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:30:40.274093+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:6: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_json_contracts.py:7: error: Library stubs not installed for "jsonschema.exceptions"  [import-untyped]
    tests\test_json_contracts.py:7: note: Hint: "python3 -m pip install types-jsonschema"
    tests\test_json_contracts.py:7: note: (or run "mypy --install-types" to install all missing stub packages)
    tests\test_json_contracts.py:65: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_common_x — pyright
  - Summary: pyright failed for x_make_common_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\env…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:43.893483+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x\tests\test_exporters.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x\tests\test_exporters.py:12:12 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x\tests\test_json_board.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x\tests\test_json_board.py:8:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_common_x\tests\test_json_contracts.py
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e25…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:30:53.295407+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x\tests\test_json_contracts.py:12:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x\tests\test_json_contracts.py:36:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x\tests\test_make_github_clones.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_clones_x\tests\test_make_github_clones.py:16:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e258…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:01.747923+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:98: error: Argument 3 to "test_main_json_runs_successfully" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_json_contracts.py:146: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:172: error: Argument 3 to "test_main_json_handles_skip" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_json_contracts.py:189: error: Expression has type "Any"  [misc]
    Found 4 errors in 1 file (checked 13 source files)

- [ ] x_make_github_visitor_x — pyright
  - Summary: pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:05.675282+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_github_visitor_x\tests\test_json_contracts.py:30:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Config contains unrecognized setting "diagnosticSeverityOverrides".
    venv .venv subdirectory not found in venv path c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace.

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\en…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:08.640314+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:518: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:522: error: Expression type contains "Any" (has type "tuple[str, Any]")  [misc]
    x_cls_make_graphviz_x.py:522: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:523: error: Expression has type "Any"  [misc]
    x_cls_make_graphviz_x.py:524: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:11.463932+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x\tests\test_graphviz_builder.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x\tests\test_graphviz_builder.py:17:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_graphviz_x\tests\test_json_contracts.py:9:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\en…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_markdown_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:14.582181+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_markdown_builder.py:48: error: Argument 1 to "test_to_html_fallback_when_markdown_missing" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_markdown_builder.py:56: error: Expression has type "Any"  [misc]
    tests\test_markdown_builder.py:64: error: Argument 1 to "test_to_pdf_requires_existing_wkhtmltopdf" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_markdown_builder.py:72: error: Expression has type "Any"  [misc]
    tests\test_markdown_builder.py:74: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:17.434789+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x\tests\test_markdown_builder.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x\tests\test_markdown_builder.py:12:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_markdown_x\tests\test_markdown_builder.py:20:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    …

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\envi…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_mermaid_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:20.478643+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_mermaid_builder.py:42: error: Argument 2 to "test_to_svg_returns_none_when_cli_missing" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_mermaid_builder.py:46: error: Expression has type "Any"  [misc]
    tests\test_mermaid_builder.py:51: error: Expression has type "Any"  [misc]
    tests\test_mermaid_builder.py:111: error: Argument 1 to "test_run_command_returns_completed_process" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_mermaid_builder.py:126: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\e…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:23.580292+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x\tests\test_json_contracts.py:18:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x\tests\test_mermaid_builder.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_mermaid_x\tests\test_mermaid_builder.py:18:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41f…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_persistent_env_var_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:28.044925+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:115: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:118: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:130: error: Argument 1 to "test_main_json_persist_values_success" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_json_contracts.py:138: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:139: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_persistent_env_var_x — pyright
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:31.437963+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_persistent_env_var_x\tests\test_json_contracts.py:11:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_pip_updates_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:38.335469+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_pip_updates.py:13: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_pip_updates.py:25: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_pip_updates.py:25: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_pip_updates.py:67: error: Argument 1 to "test_get_installed_version_handles_missing_package" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_pip_updates.py:73: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:41.181735+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x\tests\test_pip_updates.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x\tests\test_pip_updates.py:13:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x\tests\test_pip_updates.py:25:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pip_updates_x\tests\test_pip_updates.py:173:39 - error: Cannot access attribute "_run" for class "type[PipUpdatesRunner]"
      Â Â Attribute "_run" is unknown (reportAttributeAccessIssue)
    …

- [ ] x_make_progress_board_x — black
  - Summary: black failed for x_make_progress_board_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e25…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-03T03:31:43.288586+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\cli.py	2025-11-03 03:27:39.701272+00:00
    +++ C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\cli.py	2025-11-03 03:31:42.842817+00:00
    @@ -25,11 +25,13 @@
         return stages
     
    …
  - Stderr preview:
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\cli.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\tests\test_entry_module.py
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\x_cls_make_progress_board_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e258…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:49.770300+00:00
  - Suggested action: Investigate
  - Stdout preview:
    progress_board_widget.py:21: error: Explicit "Any" is not allowed  [explicit-any]
    progress_board_widget.py:21: error: Expression has type "Any"  [misc]
    progress_board_widget.py:22: error: Explicit "Any" is not allowed  [explicit-any]
    progress_board_widget.py:22: error: Expression has type "Any"  [misc]
    progress_board_widget.py:23: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_make_progress_board_x — pyright
  - Summary: pyright failed for x_make_progress_board_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:52.655033+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\progress_board_widget.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\progress_board_widget.py:14:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\progress_board_widget.py:15:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\progress_board_widget.py:16:10 - error: Import "PySide6" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x\tests\test_progress_board.py
    …

- [ ] x_make_progress_board_x — ruff_check
  - Summary: ruff_check failed for x_make_progress_board_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:31:43.542956+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
     --> cli.py:7:29
      |
    5 | import argparse
    6 | import threading
    …

- [ ] x_make_progress_board_x — ruff_fix
  - Summary: ruff_fix failed for x_make_progress_board_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_progress_board_x
  - Tool version: ruff 0.14.3
  - Captured: 2025-11-03T03:31:41.624289+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
     --> cli.py:7:29
      |
    5 | import argparse
    6 | import threading
    …

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_py_mod_sideload_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:31:55.976284+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:10: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_json_contracts.py:10: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:37: error: Expression has type "Any"  [misc]
    Found 2 errors in 1 file (checked 9 source files)

- [ ] x_make_py_mod_sideload_x — pyright
  - Summary: pyright failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda0…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:31:58.708416+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x\tests\test_json_contracts.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_mod_sideload_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_make_py_venv_x — pyright
  - Summary: pyright failed for x_make_py_venv_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_venv_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\e…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_venv_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:32:01.379682+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_venv_x\x_cls_make_py_venv_x.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_py_venv_x\x_cls_make_py_venv_x.py:18:6 - error: Import "x_make_common_x.x_subprocess_utils_x" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environmen…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:32:08.883006+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:7: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_json_contracts.py:7: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:47: error: Expression has type "Any"  [misc]
    tests\test_json_contracts.py:50: error: Expression has type "Any"  [misc]
    x_cls_make_pypi_x.py:28: error: Library stubs not installed for "jsonschema"  [import-untyped]
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environ…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:32:12.420232+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x\publish_flow.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x\publish_flow.py:17:5 - error: "HttpClient" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x\publish_flow.py:18:5 - error: "HttpError" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x\publish_flow.py:19:5 - error: "isoformat_timestamp" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_pypi_x\publish_flow.py:20:5 - error: "log_error" is unknown import symbol (reportAttributeAccessIssue)
    …

- [ ] x_make_slack_dump_and_reset_z — black
  - Summary: black failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c403…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-03T03:32:14.680244+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-11-03 03:27:43.877388+00:00
    +++ C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py	2025-11-03 03:32:14.483232+00:00
    @@ -886,11 +886,11 @@
                 raise RuntimeError(message)
             return Path(archive_root_raw).expanduser().resolve()
    …
  - Stderr preview:
    would reformat C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z\x_cls_make_slack_dump_and_reset_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:32:17.953384+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_slack_dump_and_reset_x.py:120: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_slack_dump_and_reset_x.py:676: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:956: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1074: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:32:20.901580+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z\tests\test_slack_dump_and_reset.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_slack_dump_and_reset_z\tests\test_slack_dump_and_reset.py:11:10 - error: Import "pytest" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environmen…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-03T03:32:23.915805+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_yahw.py:12: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_yahw.py:34: error: Cannot find implementation or library stub for module named "_pytest.capture"  [import-not-found]
    tests\test_yahw.py:35: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_yahw.py:46: error: Argument 1 to "test_main_invokes_runner" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_yahw.py:57: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — pyright
  - Summary: pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environ…
  - Command: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\runtime\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-03T03:32:26.508417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x\tests\test_main_json.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x\tests\test_main_json.py:16:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x\tests\test_yahw.py
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x\tests\test_yahw.py:12:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_all_venv_x\runs\20251103_032658_0c19b1c4030a41fda00e2583e4885e9b\environment\workspace\x_make_yahw_x\tests\test_yahw.py:34:10 - error: Import "_pytest.capture" could not be resolved (reportMissingImports)
    …
