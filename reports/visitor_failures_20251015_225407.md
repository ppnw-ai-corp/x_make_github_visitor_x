# Visitor TODO Report

- Generated: 2025-10-15T22:54:07.546374+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 25
- Recorded failures: 25

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:53:02.298396+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_all_x.py:870: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_all_x.py:871: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_all_x.py:872: error: Expression has type "Any"  [misc]
    x_cls_make_all_x.py:873: error: Expression has type "Any"  [misc]
    x_cls_make_all_x.py:903: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:01.084244+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_gui_columns.py:5:29
      |
    3 | # ruff: noqa: S101 - pytest assertions are expected within this module.
    4 | import json
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:52:59.420238+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_gui_columns.py:5:29
      |
    3 | # ruff: noqa: S101 - pytest assertions are expected within this module.
    4 | import json
    …

- [ ] x_make_common_x — black
  - Summary: black failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:53:11.848943+00:00 dur…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:53:13.068367+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-15 22:39:38.405050+00:00
    +++ C:\x_runner_x\x_make_common_x\telemetry.py	2025-10-15 22:53:12.885637+00:00
    @@ -163,11 +163,13 @@
     
         candidate: dict[str, object] = dict(payload)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_common_x\telemetry.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 14 files would be left unchanged.

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:53:14.041257+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_board.py:111: error: Function "x_make_common_x.json_board.BoardState.list" is not valid as a type  [valid-type]
    json_board.py:111: note: Perhaps you need "Callable[...]" or a callback protocol?
    telemetry.py:167: error: Expression has type "Any"  [misc]
    telemetry.py:168: error: Expression has type "Any"  [misc]
    telemetry.py:169: error: Expression type contains "Any" (has type "Any | str")  [misc]
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:13.280965+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> run_reports.py:4:29
      |
    3 | import json
    4 | from collections.abc import Mapping, MutableMapping
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:11.844947+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> run_reports.py:4:29
      |
    3 | import json
    4 | from collections.abc import Mapping, MutableMapping
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:53:16.62…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:53:18.411553+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-15 19:15:46.783225+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-15 22:53:18.147110+00:00
    @@ -67,11 +67,13 @@
         resolved_filename = filename or f"{tool_slug}_run_{stamp}.json"
         data = dict(payload)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 10 files would be left unchanged.

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:53:19.396054+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:43: error: Incompatible types in assignment (expression has type "None", variable has type "Callable[[datetime | None], str]")  [assignment]
    x_cls_make_github_clones_x.py:44: error: Incompatible types in assignment (expression has type "None", variable has type "Callable[[str, Mapping[str, object] | MutableMapping[str, object], DefaultNamedArg(Path | str | None, 'base_dir'), DefaultNamedArg(str | None, 'filename'), DefaultNamedArg(datetime | None, 'timestamp'), DefaultNamedArg(str, 'reports_name')], Path]")  [assignment]
    x_cls_make_github_clones_x.py:79: error: Statement is unreachable  [unreachable]
    x_cls_make_github_clones_x.py:96: error: Statement is unreachable  [unreachable]
    x_cls_make_github_clones_x.py:280: error: Returning Any from function declared to return "dict[str, object] | None"  [no-any-return]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T22:53:19.400353+00:00 duration: 1.312s tool_vers…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T22:53:20.712753+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
      c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py:40:10 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py:41:10 - error: Import "x_make_common_x" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:18.634115+00:00
  - Suggested action: Investigate
  - Stdout preview:
    EM101 Exception must not use a string literal, assign to variable first
       --> tests\test_make_github_clones.py:248:28
        |
    246 |         **_kwargs: object,
    247 |     ) -> list[RepoRecord]:
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:16.616896+00:00
  - Suggested action: Investigate
  - Stdout preview:
    EM101 Exception must not use a string literal, assign to variable first
       --> tests\test_make_github_clones.py:248:28
        |
    246 |         **_kwargs: object,
    247 |     ) -> list[RepoRecord]:
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:53:22.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:53:24.739041+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-15 19:15:48.204193+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\runner.py	2025-10-15 22:53:24.316156+00:00
    @@ -690,13 +690,11 @@
             return details
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    would reformat C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:53:25.608502+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_visitor_x.py:661: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    runner.py:661: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    Found 2 errors in 2 files (checked 8 source files)

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T22:53:31.937960+00:00 duration: 1.117s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T22:53:33.055214+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\x_cls_make_graphviz_x.py
      c:\x_runner_x\x_make_graphviz_x\x_cls_make_graphviz_x.py:19:6 - error: Import "x_make_common_x.exporters" could not be resolved (reportMissingImports)
    1 error, 0 warnings, 0 informations

- [ ] x_make_graphviz_x — ruff_check
  - Summary: ruff_check failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:31.525063+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_graphviz_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_graphviz_x — ruff_fix
  - Summary: ruff_fix failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:30.230911+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_graphviz_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:53:34.943033+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:53:35.969489+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py	2025-10-15 19:15:51.160943+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py	2025-10-15 22:53:35.840168+00:00
    @@ -71,10 +71,11 @@
         monkeypatch.setattr(exporters, "_resolve_binary", _no_binary)
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 3 files would be left unchanged.

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:36.236528+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_markdown_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:34.939521+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_markdown_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:53:40.184517+00:00 d…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:53:41.191257+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py	2025-10-15 22:53:40.144127+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py	2025-10-15 22:53:40.996030+00:00
    @@ -68,14 +68,18 @@
             return CompletedProcess(list(command), 0, stdout="done", stderr="")
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 3 files would be left unchanged.

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:41.462670+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_mermaid_builder.py:8:29
       |
     7 | import subprocess
     8 | from collections.abc import Sequence
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 start…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:40.180976+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_mermaid_builder.py:8:29
       |
     7 | import subprocess
     8 | from collections.abc import Sequence
    …

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:54.607748+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> publish_flow.py:700:5
        |
    698 |                 typed_exc_dict = cast("dict[str, object]", exc_dict_raw)
    699 |                 typed_exc_dict["run_report_path"] = report_path
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:53:53.178179+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> publish_flow.py:700:5
        |
    698 |                 typed_exc_dict = cast("dict[str, object]", exc_dict_raw)
    699 |                 typed_exc_dict["run_report_path"] = report_path
    …
