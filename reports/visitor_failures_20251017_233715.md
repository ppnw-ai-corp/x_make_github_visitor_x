# Visitor TODO Report

- Generated: 2025-10-17T23:37:15.043303+00:00
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
  - Captured: 2025-10-17T23:35:14.825453+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\typings\pytest\__init__.pyi:27: error: Explicit "Any" is not allowed  [explicit-any]
    C:\x_runner_x\typings\pytest\__init__.pyi:38: error: Explicit "Any" is not allowed  [explicit-any]
    C:\x_runner_x\typings\pytest\__init__.pyi:47: error: Explicit "Any" is not allowed  [explicit-any]
    C:\x_runner_x\typings\pytest\__init__.pyi:65: error: Explicit "Any" is not allowed  [explicit-any]
    C:\x_runner_x\typings\PySide6\QtCore.pyi:14: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_make_common_x — pyright
  - Summary: pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:35:28.160867+00:00 duration: 3.0…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:35:31.245467+00:00
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
  - Captured: 2025-10-17T23:35:41.954712+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:54: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import]
    x_cls_make_github_clones_x.py:54: note: You may be running mypy in a subpackage, mypy should be run on the package root
    Found 1 error in 1 file (checked 11 source files)

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:35:41.958180+00:00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:35:44.233177+00:00
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
  - Captured: 2025-10-17T23:36:02.629136+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:19: error: Cannot find implementation or library stub for module named "x_make_common_x.exporters"  [import-not-found]
    x_cls_make_graphviz_x.py:19: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_graphviz_x.py:104: error: Argument 4 to "__init__" becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:121: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:123: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:36:02.632976+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:36:04.892825+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py
      c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py:17:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:36:11.161438+00:00 duration:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:36:13.460522+00:00
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
  - Summary: pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:36:23.703129+00:00 duration: 5…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:36:28.908367+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py
      c:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py:18:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:36:46.928901+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:36:49.285771+00:00
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
  - Summary: pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-10-17T23:37:13.091555+00:00 duration: 1.947s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-17T23:37:15.038658+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:14:10 - error: Import "_pytest.capture" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:15:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
