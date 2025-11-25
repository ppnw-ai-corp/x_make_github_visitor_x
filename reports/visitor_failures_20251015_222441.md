# Visitor TODO Report

- Generated: 2025-10-15T22:24:41.923024+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 14
- Failing tools: 27
- Recorded failures: 27

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:23:31.302291+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_all_x.py:861: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_all_x.py:862: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_all_x.py:863: error: Expression has type "Any"  [misc]
    x_cls_make_all_x.py:864: error: Expression has type "Any"  [misc]
    x_cls_make_all_x.py:904: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:23:29.393368+00:00
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
  - Captured: 2025-10-15T22:23:27.140101+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_gui_columns.py:5:29
      |
    3 | # ruff: noqa: S101 - pytest assertions are expected within this module.
    4 | import json
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:23:44.883320+00:00
  - Suggested action: Investigate
  - Stdout preview:
    telemetry.py:167: error: Expression has type "Any"  [misc]
    telemetry.py:168: error: Expression type contains "Any" (has type "Any | tuple[()]")  [misc]
    telemetry.py:168: error: Expression has type "Any"  [misc]
    telemetry.py:171: error: Expression type contains "Any" (has type "Any | str")  [misc]
    telemetry.py:171: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:23:43.969581+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `builtins` into a type-checking block
     --> json_board.py:5:8
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:23:42.162777+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `builtins` into a type-checking block
     --> json_board.py:5:8
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:23:47.86…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:23:49.912769+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-15 19:15:46.783225+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-15 22:23:49.579720+00:00
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
  - Captured: 2025-10-15T22:23:51.143206+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:43: error: Incompatible types in assignment (expression has type "None", variable has type "Callable[[datetime | None], str]")  [assignment]
    x_cls_make_github_clones_x.py:44: error: Incompatible types in assignment (expression has type "None", variable has type "Callable[[str, Mapping[str, object] | MutableMapping[str, object], DefaultNamedArg(Path | str | None, 'base_dir'), DefaultNamedArg(str | None, 'filename'), DefaultNamedArg(datetime | None, 'timestamp'), DefaultNamedArg(str, 'reports_name')], Path]")  [assignment]
    x_cls_make_github_clones_x.py:79: error: Statement is unreachable  [unreachable]
    x_cls_make_github_clones_x.py:96: error: Statement is unreachable  [unreachable]
    x_cls_make_github_clones_x.py:280: error: Returning Any from function declared to return "dict[str, object] | None"  [no-any-return]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T22:23:51.147557+00:00 duration: 1.573s tool_vers…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T22:23:52.720296+00:00
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
  - Captured: 2025-10-15T22:23:50.156756+00:00
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
  - Captured: 2025-10-15T22:23:47.861415+00:00
  - Suggested action: Investigate
  - Stdout preview:
    EM101 Exception must not use a string literal, assign to variable first
       --> tests\test_make_github_clones.py:248:28
        |
    246 |         **_kwargs: object,
    247 |     ) -> list[RepoRecord]:
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:23:54.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:23:57.410231+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py	2025-10-15 21:27:01.967690+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py	2025-10-15 22:23:56.902790+00:00
    @@ -690,13 +690,11 @@
             return details
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\x_cls_make_github_visitor_x.py
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-15T22:23:58.623918+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_visitor_x.py:661: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    runner.py:661: error: Expression type contains "Any" (has type "dict[str, Any | None]")  [misc]
    Found 2 errors in 2 files (checked 8 source files)

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T22:24:06.061820+00:00 duration: 1.388s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T22:24:07.449489+00:00
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
  - Captured: 2025-10-15T22:24:05.178357+00:00
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
  - Captured: 2025-10-15T22:24:03.739910+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_graphviz_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:24:09.513599+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:24:10.639843+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py	2025-10-15 19:15:51.160943+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_markdown_builder.py	2025-10-15 22:24:10.449003+00:00
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
  - Captured: 2025-10-15T22:24:10.907603+00:00
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
  - Captured: 2025-10-15T22:24:09.509119+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_markdown_builder.py:8:29
       |
     7 | import importlib
     8 | from collections.abc import Sequence
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-15T22:24:15.328463+00:00 d…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: yes)
Python (CPython) 3.13.7
  - Captured: 2025-10-15T22:24:16.578662+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py	2025-10-15 19:15:52.626578+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\tests\test_mermaid_builder.py	2025-10-15 22:24:16.328508+00:00
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
  - Captured: 2025-10-15T22:24:16.827903+00:00
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
  - Captured: 2025-10-15T22:24:15.324646+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> tests\test_mermaid_builder.py:8:29
       |
     7 | import subprocess
     8 | from collections.abc import Sequence
    …

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:24:23.585623+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (71 > 50)
       --> update_flow.py:346:5
        |
    346 | def run_updates_for_packages(  # noqa: PLR0913
        |     ^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:24:22.413135+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0915 Too many statements (71 > 50)
       --> update_flow.py:346:5
        |
    346 | def run_updates_for_packages(  # noqa: PLR0913
        |     ^^^^^^^^^^^^^^^^^^^^^^^^
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-15T22:24:29.978727+00:00 duration: 1.587s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-15T22:24:31.565562+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\publish_flow.py
      c:\x_runner_x\x_make_pypi_x\publish_flow.py:699:53 - error: Type "tuple[dict[str, str | None], dict[str, dict[str, object]], Unknown | Path | None]" is not assignable to return type "tuple[dict[str, str | None], dict[str, dict[str, object]], Path]"
      Â Â Type "Unknown | Path | None" is not assignable to type "Path"
      Â Â Â Â "None" is not assignable to "Path" (reportReturnType)
    1 error, 0 warnings, 0 informations

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:24:29.373679+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use a list comprehension to create a transformed list
       --> publish_flow.py:563:9
        |
    561 |       manifest_inputs: list[dict[str, object]] = []
    562 |       for entry in entries:
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.0
  - Captured: 2025-10-15T22:24:28.127859+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use a list comprehension to create a transformed list
       --> publish_flow.py:563:9
        |
    561 |       manifest_inputs: list[dict[str, object]] = []
    562 |       for entry in entries:
    …
