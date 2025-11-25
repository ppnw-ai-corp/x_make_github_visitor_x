# Visitor TODO Report

- Generated: 2025-10-17T23:56:59.314394+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 2
- Recorded failures: 2

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-retu…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:56:45.578343+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:54: error: Cannot find implementation or library stub for module named "x_make_common_x"  [import]
    x_cls_make_github_clones_x.py:54: note: You may be running mypy in a subpackage, mypy should be run on the package root
    Found 1 error in 1 file (checked 11 source files)

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-17T23:56:54.417080+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:19: error: Cannot find implementation or library stub for module named "x_make_common_x.exporters"  [import-not-found]
    x_cls_make_graphviz_x.py:19: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_graphviz_x.py:104: error: Argument 4 to "__init__" becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:121: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    x_cls_make_graphviz_x.py:123: error: Type of variable becomes "Any | None" due to an unfollowed import  [no-any-unimported]
    …
