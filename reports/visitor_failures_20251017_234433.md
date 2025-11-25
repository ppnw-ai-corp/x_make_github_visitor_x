# Visitor TODO Report

- Generated: 2025-10-17T23:44:33.103960+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 10
- Recorded failures: 10

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-un…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:43:47.412434+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\typings\pytest\__init__.pyi:40: error: Missing type parameters for generic type "_Decorator"  [type-arg]
    C:\x_runner_x\typings\pytest\__init__.pyi:51: error: Missing type parameters for generic type "_Decorator"  [type-arg]
    tests\test_gui_exit_code.py:27: error: Expression type contains "Any" (has type "Callable[[Callable[[VarArg(Any), KwArg(Any)], Any]], Callable[[VarArg(Any), KwArg(Any)], Any]]")  [misc]
    tests\test_gui_exit_code.py:28: error: Type of decorated function contains type "Any" ("Callable[[VarArg(Any), KwArg(Any)], Any]")  [misc]
    Found 4 errors in 2 files (checked 18 source files)

- [ ] x_make_common_x — pyright
  - Summary: pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:43:51.368773+00:00 duration: 2.5…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:43:53.940763+00:00
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
  - Captured: 2025-10-17T23:43:55.594609+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:54: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import]
    x_cls_make_github_clones_x.py:54: note: You may be running mypy in a subpackage, mypy should be run on the package root
    Found 1 error in 1 file (checked 11 source files)

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:43:55.598295+00:00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:43:58.822325+00:00
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
  - Captured: 2025-10-17T23:44:07.806924+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:19: error: Cannot find implementation or library stub for module named "x_make_common_x.exporters"  [import-not-found]
    x_cls_make_graphviz_x.py:19: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_graphviz_x.py:104: error: Argument 4 to "__init__" becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:121: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:123: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:44:07.810579+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:44:09.847952+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py
      c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py:17:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:44:12.343463+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:44:14.489381+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py
      c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py:12:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py:20:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:44:17.051289+00:00 duration: 2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:44:19.305020+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py
      c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py:18:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:44:22.131116+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:44:24.287994+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py
      c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py:13:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py:25:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_yahw_x — pyright
  - Summary: pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:44:31.466275+00:00 duration: 1.633s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:44:33.099398+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:14:10 - error: Import "_pytest.capture" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:15:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
