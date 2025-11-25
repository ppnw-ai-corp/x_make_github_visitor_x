# Visitor TODO Report

- Generated: 2025-10-17T23:18:12.290984+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 16
- Recorded failures: 16

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:16:35.484399+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_forceit.py:11: error: Cannot find implementation or library stub for module named "_pytest.capture"  [import-not-found]
    tests\test_forceit.py:11: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_forceit.py:12: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_forceit.py:88: error: Argument 2 to "test_main_handles_copy_error" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_forceit.py:88: error: Argument 3 to "test_main_handles_copy_error" becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:16:35.490033+00:00 duration: 4.969…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:16:40.458748+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\tests\test_forceit.py
      c:\x_runner_x\x_0_make_all_x\tests\test_forceit.py:11:10 - error: Import "_pytest.capture" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_0_make_all_x\tests\test_forceit.py:12:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_0_make_all_x\tests\test_gui_columns.py
      c:\x_runner_x\x_0_make_all_x\tests\test_gui_columns.py:8:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:16:45.659616+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_board.py:8: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_json_board.py:47: error: Expression has type "Any"  [misc]
    tests\test_telemetry.py:9: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_telemetry.py:14: error: Cannot find implementation or library stub for module named "_pytest.capture"  [import-not-found]
    tests\test_telemetry.py:15: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    …

- [ ] x_make_common_x — pyright
  - Summary: pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:16:45.664555+00:00 duration: 4.2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:16:49.910915+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_common_x\tests\test_exporters.py
      c:\x_runner_x\x_make_common_x\tests\test_exporters.py:12:12 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_common_x\tests\test_json_board.py
      c:\x_runner_x\x_make_common_x\tests\test_json_board.py:8:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_common_x\tests\test_subprocess_utils.py
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:16:56.988522+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:54: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import]
    x_cls_make_github_clones_x.py:54: note: You may be running mypy in a subpackage, mypy should be run on the package root
    tests\test_make_github_clones.py:16: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_make_github_clones.py:16: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_make_github_clones.py:58: error: Argument 1 to "test_fetch_repos_filters_forks_and_names" becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:16:56.995491+00:00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:17:01.318298+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\tests\test_make_github_clones.py
      c:\x_runner_x\x_make_github_clones_x\tests\test_make_github_clones.py:16:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:17:18.785751+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:19: error: Cannot find implementation or library stub for module named "x_make_common_x.exporters"  [import-not-found]
    x_cls_make_graphviz_x.py:104: error: Argument 4 to "__init__" becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:121: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:123: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:389: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:17:18.789652+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:17:21.251986+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py
      c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py:17:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:17:26.817528+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_markdown_builder.py:12: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_markdown_builder.py:20: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_markdown_builder.py:20: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_markdown_builder.py:48: error: Argument 1 to "test_to_html_fallback_when_markdown_missing" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_markdown_builder.py:56: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:17:26.822133+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:17:29.453823+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py
      c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py:12:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py:20:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --war…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:17:34.916378+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_mermaid_builder.py:18: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_mermaid_builder.py:18: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_mermaid_builder.py:98: error: Argument 1 to "test_run_command_returns_completed_process" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_mermaid_builder.py:113: error: Expression has type "Any"  [misc]
    tests\test_mermaid_builder.py:123: error: Argument 1 to "test_run_command_raises_command_error" becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:17:34.921190+00:00 duration: 2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:17:37.170229+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py
      c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py:18:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-a…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:17:50.265445+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_pip_updates.py:13: error: Cannot find implementation or library stub for module named "pytest"  [import-not-found]
    tests\test_pip_updates.py:25: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_pip_updates.py:25: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_pip_updates.py:67: error: Argument 1 to "test_get_installed_version_handles_missing_package" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_pip_updates.py:73: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:17:50.269315+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:17:52.785700+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py
      c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py:13:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py:25:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unre…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:18:10.555057+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_yahw.py:14: error: Cannot find implementation or library stub for module named "_pytest.capture"  [import-not-found]
    tests\test_yahw.py:14: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_yahw.py:15: error: Cannot find implementation or library stub for module named "_pytest.monkeypatch"  [import-not-found]
    tests\test_yahw.py:26: error: Argument 1 to "test_main_invokes_runner" becomes "Any" due to an unfollowed import  [no-any-unimported]
    tests\test_yahw.py:37: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_yahw_x — pyright
  - Summary: pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:18:10.558691+00:00 duration: 1.728s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:18:12.286205+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:14:10 - error: Import "_pytest.capture" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:15:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
