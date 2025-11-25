# Visitor TODO Report

- Generated: 2025-10-18T23:52:31.839691+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 12
- Failing tools: 59
- Recorded failures: 59

- [ ] x_0_make_all_x — black
  - Summary: black failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:47:56.407950+00:00 durat…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:48:10.094686+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py	2025-10-18 02:04:30.533306+00:00
    +++ C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py	2025-10-18 23:48:03.348138+00:00
    @@ -72,11 +72,13 @@
         make_all.main(["--no-gui"])
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_all_x\tests\test_make_all_commit_cli.py
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\textual_control_center.py
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py
    would reformat C:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\shared.py
    would reformat C:\x_runner_x\x_0_make_all_x\x_cls_make_all_x.py
    …

- [ ] x_0_make_all_x — mypy
  - Summary: mypy failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:48:25.130294+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    interface\gui\prototypes\form_schemas.py:149: error: Redundant cast to "object | None"  [redundant-cast]
    C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py:22: error: Library stubs not installed for "jsonschema"  [import-untyped]
    …

- [ ] x_0_make_all_x — pyright
  - Summary: pyright failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:48:25.143282+00:00 duration: 13.306s tool_version: pyright 1.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:48:38.449217+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py
      c:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py:400:20 - error: "label" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py:409:29 - error: "expansion" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py:410:28 - error: "label" is not a known attribute of "None" (reportOptionalMemberAccess)
      c:\x_runner_x\x_0_make_all_x\interface\gui\prototypes\nicegui_control_center.py:413:25 - error: "expansion" is not a known attribute of "None" (reportOptionalMemberAccess)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_0_make_all_x — ruff_check
  - Summary: ruff_check failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:48:10.525183+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> interface\gui\commit.py:7:29
      |
    5 | import json
    6 | import subprocess
    …

- [ ] x_0_make_all_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_all_x (exit 1) cwd: C:\x_runner_x\x_0_make_all_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_all_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:47:56.349373+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> interface\gui\commit.py:7:29
      |
    5 | import json
    6 | import subprocess
    …

- [ ] x_make_common_x — mypy
  - Summary: mypy failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:48:59.057725+00:00
  - Suggested action: Investigate
  - Stdout preview:
    json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    Found 3 errors in 1 file (checked 15 source files)

- [ ] x_make_common_x — pyright
  - Summary: pyright failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:48:59.060510+00:00 duration: 3.864s tool_version: pyright 1…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:49:02.924071+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_common_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_common_x\tests\test_json_contracts.py:8:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    1 error, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:48:46.725236+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `_resolve_binary` is too complex (11 > 10)
      --> exporters.py:65:5
       |
    65 | def _resolve_binary(
       |     ^^^^^^^^^^^^^^^
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:48:43.745188+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C901 `_resolve_binary` is too complex (11 > 10)
      --> exporters.py:65:5
       |
    65 | def _resolve_binary(
       |     ^^^^^^^^^^^^^^^
    …

- [ ] x_make_github_clones_x — black
  - Summary: black failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:49:05.53…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:49:11.307712+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-18 23:46:52.930044+00:00
    +++ C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py	2025-10-18 23:49:10.934821+00:00
    @@ -250,11 +250,13 @@
         return default
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_clones_x\x_cls_make_github_clones_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 12 files would be left unchanged.

- [ ] x_make_github_clones_x — mypy
  - Summary: mypy failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable -…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:49:12.827663+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_github_clones_x.py:35: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_github_clones_x.py:35: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_github_clones_x.py:35: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_github_clones_x.py:35: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_github_clones_x.py:39: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import]
    …

- [ ] x_make_github_clones_x — pyright
  - Summary: pyright failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:49:12.832001+00:00 duration: 3.558s tool_vers…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:49:16.390102+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:24:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:30:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:36:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_github_clones_x\tests\test_json_contracts.py:113:12 - error: "__getitem__" method not defined on type "object" (reportIndexIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_github_clones_x — ruff_check
  - Summary: ruff_check failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:11.495200+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> tests\test_json_contracts.py:77:9
       |
    76 |     def fake_fetch(
    77 |         self,
    …

- [ ] x_make_github_clones_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_clones_x (exit 1) cwd: C:\x_runner_x\x_make_github_clones_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_clones_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:05.519171+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ANN001 Missing type annotation for function argument `self`
      --> tests\test_json_contracts.py:77:9
       |
    76 |     def fake_fetch(
    77 |         self,
    …

- [ ] x_make_github_visitor_x — black
  - Summary: black failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:49:18.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:49:25.244705+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-18 23:46:56.125085+00:00
    +++ C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py	2025-10-18 23:49:21.793543+00:00
    @@ -97,11 +97,13 @@
                 failure_messages=(),
                 failure_details=(),
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_github_visitor_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_github_visitor_x\runner.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 8 files would be left unchanged.

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:49:33.764980+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    runner.py:19: error: Library stubs not installed for "jsonschema"  [import-untyped]
    runner.py:19: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_github_visitor_x — pyright
  - Summary: pyright failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:49:33.768647+00:00 duration: 5.416s tool_ve…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:49:39.184565+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_github_visitor_x\runner.py
      c:\x_runner_x\x_make_github_visitor_x\runner.py:1662:15 - error: Argument of type "object" cannot be assigned to parameter "output_filename" of type "str" in function "__init__"
      Â Â "object" is not assignable to "str" (reportArgumentType)
      c:\x_runner_x\x_make_github_visitor_x\runner.py:1662:15 - error: Argument of type "object" cannot be assigned to parameter "enable_cache" of type "bool" in function "__init__"
      Â Â "object" is not assignable to "bool" (reportArgumentType)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_github_visitor_x — ruff_check
  - Summary: ruff_check failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:25.551690+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> runner.py:42:1
       |
    40 |         from x_4357_make_common_x import get_logger  # type: ignore[attr-defined]
    41 |
    …

- [ ] x_make_github_visitor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:18.536295+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E402 Module level import not at top of file
      --> runner.py:42:1
       |
    40 |         from x_4357_make_common_x import get_logger  # type: ignore[attr-defined]
    41 |
    …

- [ ] x_make_graphviz_x — black
  - Summary: black failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:49:50.559577+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:49:57.564200+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_graphviz_x\json_contracts.py	2025-10-18 23:49:50.458854+00:00
    +++ C:\x_runner_x\x_make_graphviz_x\json_contracts.py	2025-10-18 23:49:54.390141+00:00
    @@ -5,25 +5,25 @@
     _NODE_SCHEMA: dict[str, object] = {
         "type": "object",
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_graphviz_x\json_contracts.py
    would reformat C:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_graphviz_x\x_cls_make_graphviz_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:49:59.090257+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_json_contracts.py:8: error: Cannot find implementation or library stub for module named "x_make_common_x.json_contracts"  [import-not-found]
    tests\test_json_contracts.py:8: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    tests\test_json_contracts.py:9: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.json_contracts"  [import-not-found]
    tests\test_json_contracts.py:14: error: Cannot find implementation or library stub for module named "x_make_graphviz_x.x_cls_make_graphviz_x"  [import-not-found]
    tests\test_json_contracts.py:20: error: Module has no attribute "fixture"  [attr-defined]
    …

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:49:59.093981+00:00 duration: 2.542s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:50:01.635994+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py:20:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py:26:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py:32:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_graphviz_x\tests\test_json_contracts.py:55:16 - error: "skip" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_graphviz_x — ruff_check
  - Summary: ruff_check failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:57.879633+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:68:5
       |
    66 |     result = main_json(sample_input)
    67 |     validate_payload(result, OUTPUT_SCHEMA)
    …

- [ ] x_make_graphviz_x — ruff_fix
  - Summary: ruff_fix failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:49:50.556439+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:68:5
       |
    66 |     result = main_json(sample_input)
    67 |     validate_payload(result, OUTPUT_SCHEMA)
    …

- [ ] x_make_markdown_x — black
  - Summary: black failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:50:10.447251+00:00…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:50:13.946497+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-18 23:50:10.396591+00:00
    +++ C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py	2025-10-18 23:50:13.101167+00:00
    @@ -67,11 +67,13 @@
         result = main_json(sample_input)
         validate_payload(result, OUTPUT_SCHEMA)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_markdown_x\x_cls_make_markdown_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 4 files would be left unchanged.

- [ ] x_make_markdown_x — mypy
  - Summary: mypy failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:50:15.373191+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_markdown_x.py:22: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_markdown_x.py:22: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:50:15.379407+00:00 duration: 2.219s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:50:17.598755+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:21:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:27:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:33:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:56:16 - error: "skip" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_markdown_x — ruff_check
  - Summary: ruff_check failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:14.099433+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:69:5
       |
    67 |     result = main_json(sample_input)
    68 |     validate_payload(result, OUTPUT_SCHEMA)
    …

- [ ] x_make_markdown_x — ruff_fix
  - Summary: ruff_fix failed for x_make_markdown_x (exit 1) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 sta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:10.443791+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:69:5
       |
    67 |     result = main_json(sample_input)
    68 |     validate_payload(result, OUTPUT_SCHEMA)
    …

- [ ] x_make_mermaid_x — black
  - Summary: black failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:50:26.903395+00:00 d…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:50:32.891903+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-18 23:50:26.858282+00:00
    +++ C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py	2025-10-18 23:50:32.309847+00:00
    @@ -90,16 +90,11 @@
     
     SCHEMA_VERSION = "x_make_mermaid_x.run/1.0"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_mermaid_x\x_cls_make_mermaid_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 5 files would be left unchanged.

- [ ] x_make_mermaid_x — mypy
  - Summary: mypy failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-an…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:50:36.055281+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_mermaid_x.py:22: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_mermaid_x.py:22: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:50:36.060738+00:00 duration: 6.159s tool_version: pyright…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:50:42.220056+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:21:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:27:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:33:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:56:16 - error: "skip" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_mermaid_x — ruff_check
  - Summary: ruff_check failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_a…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:33.066046+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
      --> tests\test_json_contracts.py:80:9
       |
    78 |     payload["parameters"]["mermaid_cli_path"] = str(fake_cli)
    79 |
    …

- [ ] x_make_mermaid_x — ruff_fix
  - Summary: ruff_fix failed for x_make_mermaid_x (exit 1) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 start…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:26.896790+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PLR0913 Too many arguments in function definition (6 > 5)
      --> tests\test_json_contracts.py:80:9
       |
    78 |     payload["parameters"]["mermaid_cli_path"] = str(fake_cli)
    79 |
    …

- [ ] x_make_persistent_env_var_x — black
  - Summary: black failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:50:50.059896+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py	2025-10-18 23:50:46.085466+00:00
    +++ C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py	2025-10-18 23:50:48.316392+00:00
    @@ -130,11 +130,13 @@
         snapshot = result["environment_snapshot"]
         assert snapshot["provided"]["API_TOKEN"] == "<hidden>"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\tests\test_persistent_env.py
    would reformat C:\x_runner_x\x_make_persistent_env_var_x\x_cls_make_persistent_env_var_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_persistent_env_var_x — mypy
  - Summary: mypy failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unr…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:50:56.682849+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_persistent_env_var_x.py:20: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_persistent_env_var_x.py:20: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_persistent_env_var_x — pyright
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:50:56.686474+00:00 duration: 3.637s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:51:00.323066+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:24:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:30:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:36:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:59:16 - error: "skip" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_persistent_env_var_x — ruff_check
  - Summary: ruff_check failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:50.251717+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> tests\test_json_contracts.py:112:5
        |
    111 |     validate_payload(result, OUTPUT_SCHEMA)
    112 |     assert result["status"] == "success"
    …

- [ ] x_make_persistent_env_var_x — ruff_fix
  - Summary: ruff_fix failed for x_make_persistent_env_var_x (exit 1) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:50:46.153861+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> tests\test_json_contracts.py:112:5
        |
    111 |     validate_payload(result, OUTPUT_SCHEMA)
    112 |     assert result["status"] == "success"
    …

- [ ] x_make_pip_updates_x — black
  - Summary: black failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:51:13.183217…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:51:18.525169+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-18 23:51:13.128920+00:00
    +++ C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py	2025-10-18 23:51:17.112434+00:00
    @@ -64,11 +64,13 @@
         result = main_json(sample_input)
         validate_payload(result, OUTPUT_SCHEMA)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
    would reformat C:\x_runner_x\x_make_pip_updates_x\x_cls_make_pip_updates_x.py
    would reformat C:\x_runner_x\x_make_pip_updates_x\update_flow.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_make_pip_updates_x — mypy
  - Summary: mypy failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --dis…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:51:19.763172+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    update_flow.py:16: error: Library stubs not installed for "jsonschema"  [import-untyped]
    update_flow.py:16: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:51:19.767937+00:00 duration: 4.101s tool_version:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:51:23.868679+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:21:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:27:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:33:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
    3 errors, 0 warnings, 0 informations
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:18.697417+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:56:5
       |
    54 | def test_existing_reports_align_with_schema() -> None:
    55 |     report_files = sorted(REPORTS_DIR.glob("x_make_pip_updates_x_run_*.json"))
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:13.180138+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
      --> tests\test_json_contracts.py:56:5
       |
    54 | def test_existing_reports_align_with_schema() -> None:
    55 |     report_files = sorted(REPORTS_DIR.glob("x_make_pip_updates_x_run_*.json"))
    …

- [ ] x_make_py_mod_sideload_x — black
  - Summary: black failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:51:2…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:51:32.082699+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-18 23:51:28.039371+00:00
    +++ C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py	2025-10-18 23:51:31.801718+00:00
    @@ -154,11 +154,13 @@
             obj: optional attribute name to return from the module
             """
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_py_mod_sideload_x\x_cls_make_py_mod_sideload_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_make_py_mod_sideload_x — mypy
  - Summary: mypy failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:51:39.522772+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_py_mod_sideload_x.py:16: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_py_mod_sideload_x.py:16: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_py_mod_sideload_x — pyright
  - Summary: pyright failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:51:39.528414+00:00 duration: 3.466s tool_…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:51:42.994053+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:41:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:47:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:53:9 - error: "fixture" is not a known attribute of module "pytest" (reportAttributeAccessIssue)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:93:5 - error: "__setitem__" method not defined on type "object" (reportIndexIssue)
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_py_mod_sideload_x — ruff_check
  - Summary: ruff_check failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:32.255648+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> tests\test_json_contracts.py:98:5
        |
     97 |     validate_payload(result, OUTPUT_SCHEMA)
     98 |     assert result["status"] == "success"
    …

- [ ] x_make_py_mod_sideload_x — ruff_fix
  - Summary: ruff_fix failed for x_make_py_mod_sideload_x (exit 1) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:28.086413+00:00
  - Suggested action: Investigate
  - Stdout preview:
    S101 Use of `assert` detected
       --> tests\test_json_contracts.py:98:5
        |
     97 |     validate_payload(result, OUTPUT_SCHEMA)
     98 |     assert result["status"] == "success"
    …

- [ ] x_make_pypi_x — black
  - Summary: black failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:51:48.788284+00:00 duratio…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:51:54.303036+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-18 23:51:48.737516+00:00
    +++ C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py	2025-10-18 23:51:53.179737+00:00
    @@ -136,11 +136,13 @@
             report_payload = _run_report_payload(tmp_path)
             report_path = tmp_path / "reports" / "x_make_pypi_x_run_test.json"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    would reformat C:\x_runner_x\x_make_pypi_x\x_cls_make_pypi_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 6 files would be left unchanged.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unim…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:52:00.600736+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C:\x_runner_x\x_make_common_x\json_contracts.py:26: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "Any | None")  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_pypi_x.py:30: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_pypi_x.py:30: note: Hint: "python3 -m pip install types-jsonschema"
    …

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:52:00.604667+00:00 duration: 4.208s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:52:04.812480+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:6:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:7:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:9:6 - error: Import "x_make_pypi_x.json_contracts" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_pypi_x — ruff_check
  - Summary: ruff_check failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:54.482412+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:6:29
      |
    4 | import json
    5 | import sys
    …

- [ ] x_make_pypi_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:51:48.782849+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:6:29
      |
    4 | import json
    5 | import sys
    …

- [ ] x_make_yahw_x — black
  - Summary: black failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-10-18T23:52:14.744060+00:00 duratio…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: python -m black, 25.9.0 (compiled: no)
Python (CPython) 3.14.0
  - Captured: 2025-10-18T23:52:19.749358+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py	2025-10-18 23:52:14.690039+00:00
    +++ C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py	2025-10-18 23:52:19.364917+00:00
    @@ -28,31 +28,37 @@
     
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_yahw_x\x_cls_make_yahw_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 7 files would be left unchanged.

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unim…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy . --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-10-18T23:52:24.150813+00:00
  - Suggested action: Investigate
  - Stdout preview:
    __init__.py:7: error: Expression has type "Any"  [misc]
    __init__.py:8: error: Expression has type "Any"  [misc]
    __init__.py:9: error: Expression has type "Any"  [misc]
    C:\x_runner_x\x_make_common_x\json_contracts.py:27: error: Expression type contains "Any" (has type "type[type]")  [misc]
    x_cls_make_yahw_x.py:11: error: Library stubs not installed for "jsonschema"  [import-untyped]
    …

- [ ] x_make_yahw_x — pyright
  - Summary: pyright failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-10-18T23:52:24.156094+00:00 duration: 7.656s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: pyright 1.1.406
  - Captured: 2025-10-18T23:52:31.811848+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py
      c:\x_runner_x\x_make_yahw_x\tests\test_yahw.py:52:14 - error: Argument of type "str | None" cannot be assigned to parameter "args" of type "StrPath" in function "__new__"
      Â Â Type "str | None" is not assignable to type "StrPath"
      Â Â Â Â Type "None" is not assignable to type "StrPath"
      Â Â Â Â Â Â "None" is not assignable to "str"
    …
  - Stderr preview:
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.
    Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Apps > Advanced app settings > App execution aliases.

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:52:20.286199+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.1
  - Captured: 2025-10-18T23:52:14.739024+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> tests\test_main_json.py:4:29
      |
    3 | import importlib
    4 | from collections.abc import Mapping
    …
