# Visitor TODO Report

- Generated: 2025-11-26T01:18:11.217126+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 44
- Failing tools: 78
- Recorded failures: 78

- [ ] x_0_make_ppnw_dot_ai_change_control_x — black
  - Summary: black failed for x_0_make_ppnw_dot_ai_change_control_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff star…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:06:33.398407+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x\Change Control\0.20.14\evidence\architectura_fabula\runs\2025-11-18\capture_cli_failure.py	2025-11-26 00:48:34.446683+00:00
    +++ C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x\Change Control\0.20.14\evidence\architectura_fabula\runs\2025-11-18\capture_cli_failure.py	2025-11-26 01:06:33.215069+00:00
    @@ -12,10 +12,11 @@
             return value
         if isinstance(value, str):
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x\Change Control\0.20.14\evidence\architectura_fabula\runs\2025-11-18\capture_cli_failure.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 6 files would be left unchanged.

- [ ] x_0_make_ppnw_dot_ai_change_control_x — ruff_check
  - Summary: ruff_check failed for x_0_make_ppnw_dot_ai_change_control_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:06:33.583062+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SIM118 Use `key in dict` instead of `key in dict.keys()`
      --> Change Control\0.20.15\evidence\root_cleanup\diagram_utilities\rebuild_mermaid.py:53:41
       |
    51 |     if isinstance(value, dict):
    52 |         mapping = cast("Mapping[object, object]", value)
    …

- [ ] x_0_make_ppnw_dot_ai_change_control_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_ppnw_dot_ai_change_control_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --l…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_change_control_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:06:31.495757+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SIM118 Use `key in dict` instead of `key in dict.keys()`
      --> Change Control\0.20.15\evidence\root_cleanup\diagram_utilities\rebuild_mermaid.py:53:41
       |
    51 |     if isinstance(value, dict):
    52 |         mapping = cast("Mapping[object, object]", value)
    …

- [ ] x_legatus_architectura_fabula_x — black
  - Summary: black failed for x_legatus_architectura_fabula_x (exit 1) cwd: C:\x_runner_x\x_legatus_architectura_fabula_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_architectura_fabula_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:07:34.645318+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py	2025-11-26 01:00:11.618901+00:00
    +++ C:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py	2025-11-26 01:07:33.848834+00:00
    @@ -9,35 +9,35 @@
     _IMPL_PACKAGE = f"{__name__}.x_legatus_architectura_fabula_x"
     _impl = importlib.import_module(_IMPL_PACKAGE)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py
    would reformat C:\x_runner_x\x_legatus_architectura_fabula_x\architectura_fabula\variant_diff.py
    would reformat C:\x_runner_x\x_legatus_architectura_fabula_x\architectura_fabula\__init__.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_legatus_architectura_fabula_x — mypy
  - Summary: mypy failed for x_legatus_architectura_fabula_x (exit 1) cwd: C:\x_runner_x\x_legatus_architectura_fabula_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_architectura_fabula_x --strict --no-warn-unused-configs…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_architectura_fabula_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_architectura_fabula_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:07:37.739950+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_legatus_architectura_fabula_x\canon.py:41: error: Explicit "Any" is not allowed  [explicit-any]
    x_legatus_architectura_fabula_x\canon.py:42: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    x_legatus_architectura_fabula_x\canon.py:63: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    x_legatus_architectura_fabula_x\canon.py:84: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    x_legatus_architectura_fabula_x\canon.py:105: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    …

- [ ] x_legatus_architectura_fabula_x — pyright
  - Summary: pyright failed for x_legatus_architectura_fabula_x (exit 1) cwd: C:\x_runner_x\x_legatus_architectura_fabula_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:07:37.749579+00:00 duration…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_architectura_fabula_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:07:41.542146+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py
      c:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py:14:2 - error: Type of "_exported" is partially unknown
      Â Â Type of "_exported" is "tuple[Unknown, ...]" (reportUnknownVariableType)
      c:\x_runner_x\x_legatus_architectura_fabula_x\__init__.py:14:20 - error: Argument type is partially unknown
      Â Â Argument corresponds to parameter "iterable" in function "__new__"
    …

- [ ] x_legatus_architectura_fabula_x — ruff_check
  - Summary: ruff_check failed for x_legatus_architectura_fabula_x (exit 1) cwd: C:\x_runner_x\x_legatus_architectura_fabula_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_architectura_fabula_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:07:34.887902+00:00
  - Suggested action: Investigate
  - Stdout preview:
    W191 Indentation contains tabs
      --> __init__.py:14:1
       |
    12 | _public = getattr(_impl, "__all__", None)
    13 | if isinstance(_public, (list, tuple)):
    …

- [ ] x_legatus_architectura_fabula_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_architectura_fabula_x (exit 1) cwd: C:\x_runner_x\x_legatus_architectura_fabula_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 8…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_architectura_fabula_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:07:32.526018+00:00
  - Suggested action: Investigate
  - Stdout preview:
    W191 Indentation contains tabs
      --> __init__.py:14:1
       |
    12 | _public = getattr(_impl, "__all__", None)
    13 | if isinstance(_public, (list, tuple)):
    …

- [ ] x_legatus_astra_textor_x — black
  - Summary: black failed for x_legatus_astra_textor_x (exit 1) cwd: C:\x_runner_x\x_legatus_astra_textor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-26T01:08:3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_astra_textor_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:08:41.508046+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_astra_textor_x\astra_textor\x_cls_run_all_x.py	2025-11-25 23:49:06.297513+00:00
    +++ C:\x_runner_x\x_legatus_astra_textor_x\astra_textor\x_cls_run_all_x.py	2025-11-26 01:08:41.039833+00:00
    @@ -19,10 +19,11 @@
     from enum import Enum
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_astra_textor_x\astra_textor\x_cls_run_all_x.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 42 files would be left unchanged.

- [ ] x_legatus_astra_textor_x — mypy
  - Summary: mypy failed for x_legatus_astra_textor_x (exit 2) cwd: C:\x_runner_x\x_legatus_astra_textor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_astra_textor_x --strict --no-warn-unused-configs --show-error-codes -…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_astra_textor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_astra_textor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:08:42.136592+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_astra_textor_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_astra_textor_x — pyright
  - Summary: pyright failed for x_legatus_astra_textor_x (exit 1) cwd: C:\x_runner_x\x_legatus_astra_textor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:08:42.144268+00:00 duration: 5.188s tool_…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_astra_textor_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:08:47.332833+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_legatus_astra_textor_x\astra_textor\interface\environment_studio\app.py
      c:\x_runner_x\x_legatus_astra_textor_x\astra_textor\interface\environment_studio\app.py:17:27 - error: "QPainter" is unknown import symbol (reportAttributeAccessIssue)
      c:\x_runner_x\x_legatus_astra_textor_x\astra_textor\interface\environment_studio\app.py:822:14 - error: Cannot access attribute "fitInView" for class "QGraphicsView"
      Â Â Attribute "fitInView" is unknown (reportAttributeAccessIssue)
      c:\x_runner_x\x_legatus_astra_textor_x\astra_textor\interface\environment_studio\app.py:822:30 - error: Cannot access attribute "sceneRect" for class "QGraphicsScene"
    …

- [ ] x_legatus_astra_textor_x — ruff_check
  - Summary: ruff_check failed for x_legatus_astra_textor_x (exit 1) cwd: C:\x_runner_x\x_legatus_astra_textor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_astra_textor_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:08:41.698250+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> astra_textor\astrocyte_adapters\__init__.py:5:29
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_legatus_astra_textor_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_astra_textor_x (exit 1) cwd: C:\x_runner_x\x_legatus_astra_textor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_astra_textor_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:08:37.825800+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Callable` into a type-checking block
     --> astra_textor\astrocyte_adapters\__init__.py:5:29
      |
    3 | from __future__ import annotations
    4 |
    …

- [ ] x_legatus_capsula_calculus_x — mypy
  - Summary: mypy failed for x_legatus_capsula_calculus_x (exit 1) cwd: C:\x_runner_x\x_legatus_capsula_calculus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_capsula_calculus_x --strict --no-warn-unused-configs --show-e…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_capsula_calculus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_capsula_calculus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:09:32.251569+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_legatus_capsula_calculus_x\inference\inference_service.py:34: error: Explicit "Any" is not allowed  [explicit-any]
    x_legatus_capsula_calculus_x\inference\inference_service.py:38: error: Explicit "Any" is not allowed  [explicit-any]
    x_legatus_capsula_calculus_x\inference\inference_service.py:132: error: Unused "type: ignore" comment  [unused-ignore]
    Found 3 errors in 1 file (checked 7 source files)

- [ ] x_legatus_celer_notitia_x — mypy
  - Summary: mypy failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_celer_notitia_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_celer_notitia_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:09:47.368036+00:00
  - Suggested action: Investigate
  - Stdout preview:
    firmware\input_handler.py:97: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\input_handler.py:98: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\config_store.py:105: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\config_store.py:106: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\config_store.py:109: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_legatus_celer_notitia_x — ruff_check
  - Summary: ruff_check failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:09:46.612172+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `duration_ms`
      --> firmware\boot.py:56:26
       |
    54 |     Pin = _PinStub()
    55 |
    …

- [ ] x_legatus_celer_notitia_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_celer_notitia_x (exit 1) cwd: C:\x_runner_x\x_legatus_celer_notitia_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_celer_notitia_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:09:44.934981+00:00
  - Suggested action: Investigate
  - Stdout preview:
    ARG002 Unused method argument: `duration_ms`
      --> firmware\boot.py:56:26
       |
    54 |     Pin = _PinStub()
    55 |
    …

- [ ] x_legatus_inceptio_praesidium_x — mypy
  - Summary: mypy failed for x_legatus_inceptio_praesidium_x (exit 2) cwd: C:\x_runner_x\x_legatus_inceptio_praesidium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_inceptio_praesidium_x --strict --no-warn-unused-configs…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_inceptio_praesidium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_inceptio_praesidium_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:09:56.009367+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_inceptio_praesidium_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_inceptio_praesidium_x — ruff_check
  - Summary: ruff_check failed for x_legatus_inceptio_praesidium_x (exit 1) cwd: C:\x_runner_x\x_legatus_inceptio_praesidium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_inceptio_praesidium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:09:55.608054+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
      --> inceptio_praesidium\cli.py:8:29
       |
     6 | import json
     7 | import sys
    …

- [ ] x_legatus_inceptio_praesidium_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_inceptio_praesidium_x (exit 1) cwd: C:\x_runner_x\x_legatus_inceptio_praesidium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 8…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_inceptio_praesidium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:09:55.396384+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
      --> inceptio_praesidium\cli.py:8:29
       |
     6 | import json
     7 | import sys
    …

- [ ] x_legatus_mentis_multiplex_x — black
  - Summary: black failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-26…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:10:25.330515+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core\messages.pyi	2025-11-25 23:49:38.791300+00:00
    +++ C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core\messages.pyi	2025-11-26 01:10:25.184948+00:00
    @@ -1,17 +1,14 @@
    -
     from typing import Any, Protocol
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core\messages.pyi
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core\prompts.pyi
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    2 files would be reformatted, 3 files would be left unchanged.

- [ ] x_legatus_mentis_multiplex_x — mypy
  - Summary: mypy failed for x_legatus_mentis_multiplex_x (exit 2) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_mentis_multiplex_x --strict --no-warn-unused-configs --show-e…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_mentis_multiplex_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:10:25.846933+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_mentis_multiplex_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_mentis_multiplex_x — ruff_check
  - Summary: ruff_check failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:10:25.488089+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `scripts\audit_contract.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> scripts\audit_contract.py:1:1
    
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> scripts\audit_contract.py:7:29
    …

- [ ] x_legatus_mentis_multiplex_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:10:24.094509+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `scripts\audit_contract.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> scripts\audit_contract.py:1:1
    
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> scripts\audit_contract.py:7:29
    …

- [ ] x_legatus_politia_tabularium_x — mypy
  - Summary: mypy failed for x_legatus_politia_tabularium_x (exit 2) cwd: C:\x_runner_x\x_legatus_politia_tabularium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_politia_tabularium_x --strict --no-warn-unused-configs --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_politia_tabularium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_politia_tabularium_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:10:29.616992+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_politia_tabularium_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_politia_tabularium_x — ruff_check
  - Summary: ruff_check failed for x_legatus_politia_tabularium_x (exit 1) cwd: C:\x_runner_x\x_legatus_politia_tabularium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_politia_tabularium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:10:29.265579+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
     --> politia_tabularium\cleanup_env.py:6:29
      |
    5 | import subprocess
    6 | from collections.abc import Iterable, Sequence
    …

- [ ] x_legatus_politia_tabularium_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_politia_tabularium_x (exit 1) cwd: C:\x_runner_x\x_legatus_politia_tabularium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 …
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_politia_tabularium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:10:29.078809+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterable` into a type-checking block
     --> politia_tabularium\cleanup_env.py:6:29
      |
    5 | import subprocess
    6 | from collections.abc import Iterable, Sequence
    …

- [ ] x_legatus_scriba_machina_x — mypy
  - Summary: mypy failed for x_legatus_scriba_machina_x (exit 2) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_scriba_machina_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_scriba_machina_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:11:07.812060+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_scriba_machina_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_scriba_machina_x — ruff_check
  - Summary: ruff_check failed for x_legatus_scriba_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ver…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:07.452952+00:00
  - Suggested action: Investigate

- [ ] x_legatus_scriba_machina_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_scriba_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:07.242009+00:00
  - Suggested action: Investigate

- [ ] x_legatus_segmentum_judicium_x — mypy
  - Summary: mypy failed for x_legatus_segmentum_judicium_x (exit 2) cwd: C:\x_runner_x\x_legatus_segmentum_judicium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_segmentum_judicium_x --strict --no-warn-unused-configs --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_segmentum_judicium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_segmentum_judicium_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:11:26.416928+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_segmentum_judicium_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_segmentum_judicium_x — pyright
  - Summary: pyright failed for x_legatus_segmentum_judicium_x (exit 1) cwd: C:\x_runner_x\x_legatus_segmentum_judicium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:11:26.425449+00:00 duration: …
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_segmentum_judicium_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:11:29.563485+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_legatus_segmentum_judicium_x\src\segmentum_judicium\cli.py
      c:\x_runner_x\x_legatus_segmentum_judicium_x\src\segmentum_judicium\cli.py:248:45 - error: Argument of type "Any | None" cannot be assigned to parameter "source" of type "Path" in function "build_manifest"
      Â Â Type "Any | None" is not assignable to type "Path"
      Â Â Â Â "None" is not assignable to "Path" (reportArgumentType)
      c:\x_runner_x\x_legatus_segmentum_judicium_x\src\segmentum_judicium\cli.py:260:45 - error: Argument of type "Any | None" cannot be assigned to parameter "source" of type "Path" in function "build_manifest"
    …

- [ ] x_legatus_segmentum_judicium_x — ruff_check
  - Summary: ruff_check failed for x_legatus_segmentum_judicium_x (exit 1) cwd: C:\x_runner_x\x_legatus_segmentum_judicium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --ta…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_segmentum_judicium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:26.035060+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `paging the judge.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> paging the judge.py:1:1
    
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> paging the judge.py:9:29
    …

- [ ] x_legatus_segmentum_judicium_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_segmentum_judicium_x (exit 1) cwd: C:\x_runner_x\x_legatus_segmentum_judicium_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 …
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_segmentum_judicium_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:25.838176+00:00
  - Suggested action: Investigate
  - Stdout preview:
    INP001 File `paging the judge.py` is part of an implicit namespace package. Add an `__init__.py`.
    --> paging the judge.py:1:1
    
    TC003 Move standard library import `collections.abc.Sequence` into a type-checking block
      --> paging the judge.py:9:29
    …

- [ ] x_legatus_senatus_machina_x — mypy
  - Summary: mypy failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_senatus_machina_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_senatus_machina_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:11:37.170764+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_legatus_senatus_machina_x\models.py:31: error: Explicit "Any" is not allowed  [explicit-any]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Any | str")  [misc]
    x_legatus_senatus_machina_x\models.py:35: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    …

- [ ] x_legatus_senatus_machina_x — ruff_check
  - Summary: ruff_check failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:36.282036+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
      --> models.py:38:23
       |
    36 |             title = str(raw.get("title") or "").strip()
    37 |             if not title:
    …

- [ ] x_legatus_senatus_machina_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:36.059595+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TRY003 Avoid specifying long messages outside the exception class
      --> models.py:38:23
       |
    36 |             title = str(raw.get("title") or "").strip()
    37 |             if not title:
    …

- [ ] x_legatus_tactica_impetus_x — black
  - Summary: black failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-26T0…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:11:53.648462+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi	2025-11-10 22:18:07.309474+00:00
    +++ C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi	2025-11-26 01:11:53.446425+00:00
    @@ -6,16 +6,16 @@
     def dumps(
         value: object,
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 43 files would be left unchanged.

- [ ] x_legatus_tactica_impetus_x — mypy
  - Summary: mypy failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:11:54.562068+00:00
  - Suggested action: Investigate
  - Stdout preview:
    firmware\lib\x_cls_display_tft_x.py:49: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\lib\x_cls_display_tft_x.py:50: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\lib\x_cls_display_tft_x.py:55: error: Redundant cast to Module | None  [redundant-cast]
    firmware\lib\x_cls_display_tft_x.py:56: error: Redundant cast to Module | None  [redundant-cast]
    firmware\lib\x_cls_display_tft_x.py:57: error: Redundant cast to Module | None  [redundant-cast]
    …

- [ ] x_legatus_tactica_impetus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:53.837453+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:41:22
       |
    40 | class _WLAN(Protocol):
    41 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_tactica_impetus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:11:52.143276+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:41:22
       |
    40 | class _WLAN(Protocol):
    41 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_vigil_nexus_x — mypy
  - Summary: mypy failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:12:39.138948+00:00
  - Suggested action: Investigate
  - Stdout preview:
    typings\pydantic\__init__.pyi:7: error: Explicit "Any" is not allowed  [explicit-any]
    typings\pydantic\__init__.pyi:8: error: Explicit "Any" is not allowed  [explicit-any]
    typings\pydantic\__init__.pyi:10: error: Explicit "Any" is not allowed  [explicit-any]
    control_plane\models.py:3: error: Unused "type: ignore" comment  [unused-ignore]
    control_plane\models.py:6: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_legatus_vigil_nexus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version p…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:12:37.615103+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C416 Unnecessary dict comprehension (rewrite using `dict()`)
       --> clients\session_client.py:174:26
        |
    172 |         }
    173 |         async with websockets.connect(ws_url, extra_headers=headers) as ws:
    …

- [ ] x_legatus_vigil_nexus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-versi…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:12:37.440804+00:00
  - Suggested action: Investigate
  - Stdout preview:
    C416 Unnecessary dict comprehension (rewrite using `dict()`)
       --> clients\session_client.py:174:26
        |
    172 |         }
    173 |         async with websockets.connect(ws_url, extra_headers=headers) as ws:
    …

- [ ] x_make_common_x — ruff_check
  - Summary: ruff_check failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:13:03.978213+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …

- [ ] x_make_common_x — ruff_fix
  - Summary: ruff_fix failed for x_make_common_x (exit 1) cwd: C:\x_runner_x\x_make_common_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_common_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:13:03.769786+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Iterator` into a type-checking block
     --> detect\entrypoints.py:7:29
      |
    5 | import hashlib
    6 | import re
    …

- [ ] x_make_copilot_cli_one_time_setup_x — mypy
  - Summary: mypy failed for x_make_copilot_cli_one_time_setup_x (exit 2) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_copilot_cli_one_time_setup_x --strict --no-warn-un…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_copilot_cli_one_time_setup_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:13:18.677888+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_make_copilot_cli_one_time_setup_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_make_copilot_cli_one_time_setup_x — ruff_check
  - Summary: ruff_check failed for x_make_copilot_cli_one_time_setup_x (exit 1) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-leng…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:13:18.316875+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (94 > 88)
       --> x_cls_make_copilot_cli_one_time_setup_x.py:122:89
        |
    120 |     command = (
    121 |         "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; "
    …

- [ ] x_make_copilot_cli_one_time_setup_x — ruff_fix
  - Summary: ruff_fix failed for x_make_copilot_cli_one_time_setup_x (exit 1) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:13:18.136512+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (94 > 88)
       --> x_cls_make_copilot_cli_one_time_setup_x.py:122:89
        |
    120 |     command = (
    121 |         "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; "
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:14:09.113470+00:00
  - Suggested action: Investigate
  - Stdout preview:
    report_validator.py:212: error: Expression type contains "Any" (has type "tuple[int, Any]")  [misc]
    report_validator.py:212: error: Expression has type "Any"  [misc]
    report_validator.py:212: error: Expression type contains "Any" (has type "enumerate[Any]")  [misc]
    report_validator.py:213: error: Expression has type "Any"  [misc]
    report_validator.py:300: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_gitignore_sync_x — mypy
  - Summary: mypy failed for x_make_gitignore_sync_x (exit 2) cwd: C:\x_runner_x\x_make_gitignore_sync_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_gitignore_sync_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_gitignore_sync_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_gitignore_sync_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:14:13.323886+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_make_gitignore_sync_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:14:34.672364+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:512: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_graphviz_x.py:527: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    Found 2 errors in 1 file (checked 12 source files)
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_graphviz_x — pyright
  - Summary: pyright failed for x_make_graphviz_x (exit 3) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:14:34.687025+00:00 duration: 2.344s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:14:37.029887+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_graphviz_x\__init__.py
      c:\x_runner_x\x_make_graphviz_x\__init__.py:5:6 - error: Import "x_make_graphviz_x.x_cls_make_graphviz_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py
      c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py:12:6 - error: Import "x_make_graphviz_x" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_graphviz_x\tests\test_graphviz_builder.py:17:10 - error: Import "_pytest.monkeypatch" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_graphviz_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_markdown_x — pyright
  - Summary: pyright failed for x_make_markdown_x (exit 3) cwd: C:\x_runner_x\x_make_markdown_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:14:49.519014+00:00 duration: 2.096s tool_version: pyrig…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_markdown_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:14:51.608200+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:12:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:13:6 - error: Import "x_make_markdown_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_markdown_x\tests\test_json_contracts.py:18:6 - error: Import "x_make_markdown_x.x_cls_make_markdown_x" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_markdown_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 3) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:15:02.814899+00:00 duration: 2.342s tool_version: pyright…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:15:05.153301+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:12:6 - error: Import "x_make_common_x.exporters" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:13:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_mermaid_x\tests\test_json_contracts.py:14:6 - error: Import "x_make_mermaid_x.json_contracts" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_mermaid_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_persistent_env_var_x — pyright
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 3) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:15:18.408168+00:00 duration: 2.485s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:15:20.893118+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_persistent_env_var_x\tests\test_cli_dispatch.py
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_cli_dispatch.py:6:8 - error: Import "x_make_persistent_env_var_x.x_cls_make_persistent_env_var_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:11:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_persistent_env_var_x\tests\test_json_contracts.py:13:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_persistent_env_var_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_pip_updates_x — pyright
  - Summary: pyright failed for x_make_pip_updates_x (exit 3) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:15:40.249806+00:00 duration: 2.273s tool_version:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:15:42.518988+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:9:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:10:6 - error: Import "x_make_pip_updates_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pip_updates_x\tests\test_json_contracts.py:15:6 - error: Import "x_make_pip_updates_x.update_flow" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_pip_updates_x\tests\test_pip_updates.py
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_pip_updates_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_pip_updates_x — ruff_check
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 s…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:15:39.671279+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
      --> tests\test_pip_updates.py:10:29
       |
     8 | import subprocess
     9 | import typing
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py3…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:15:38.016180+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
      --> tests\test_pip_updates.py:10:29
       |
     8 | import subprocess
     9 | import typing
    …

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --wa…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:15:59.014071+00:00
  - Suggested action: Investigate
  - Stdout preview:
    progress_board_widget.py:160: error: Expression has type "Any"  [misc]
    progress_board_widget.py:240: error: Argument 1 to "setCheckState" of "QListWidgetItem" has incompatible type "int"; expected "CheckState"  [arg-type]
    progress_board_widget.py:252: error: Expression has type "Any"  [misc]
    progress_board_widget.py:305: error: Argument 1 to "closeEvent" of "QWidget" has incompatible type "_CloseEvent"; expected "QCloseEvent"  [arg-type]
    progress_board_widget.py:319: error: Incompatible return value type (got "CheckState", expected "int")  [return-value]
    …
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_progress_board_x — pyright
  - Summary: pyright failed for x_make_progress_board_x (exit 3) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:15:59.020053+00:00 duration: 2.281s tool_ve…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:16:01.300682+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_progress_board_x\__init__.py
      c:\x_runner_x\x_make_progress_board_x\__init__.py:3:6 - error: Import "x_make_progress_board_x.progress_board_widget" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_progress_board_x\cli.py
      c:\x_runner_x\x_make_progress_board_x\cli.py:13:6 - error: Import "x_make_common_x.progress_snapshot" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_progress_board_x\cli.py:14:6 - error: Import "x_make_progress_board_x.progress_board_widget" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_progress_board_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_py_mod_sideload_x — pyright
  - Summary: pyright failed for x_make_py_mod_sideload_x (exit 3) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:16:22.973670+00:00 duration: 2.103s tool_…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:16:25.075183+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:10:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:12:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:13:6 - error: Import "x_make_py_mod_sideload_x" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_py_mod_sideload_x\tests\test_json_contracts.py:14:6 - error: Import "x_make_py_mod_sideload_x.json_contracts" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_py_mod_sideload_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_pypi_x — mypy
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:16:48.640457+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_pypi_x.py:548: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_pypi_x.py:660: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    x_cls_make_pypi_x.py:808: error: Expression type contains "Any" (has type "type[ValidationError]")  [misc]
    Found 3 errors in 1 file (checked 11 source files)
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 3) cwd: C:\x_runner_x\x_make_pypi_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:16:48.648267+00:00 duration: 3.068s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:16:51.714280+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:7:8 - error: Import "pytest" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:9:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_pypi_x\tests\test_json_contracts.py:10:6 - error: Import "x_make_pypi_x.json_contracts" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_pypi_x\tests\test_main_json.py
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_pypi_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_slack_dump_and_reset_z — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --sho…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_slack_dump_and_reset_z --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:17:13.374205+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_persistent_env_isolation.py:14: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:675: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:953: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:953: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1070: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_slack_dump_and_reset_z — pyright
  - Summary: pyright failed for x_make_slack_dump_and_reset_z (exit 3) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:17:13.377817+00:00 duration: 2.…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:17:15.647871+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\__main__.py:3:6 - error: Import "x_make_slack_dump_and_reset_z.x_cls_make_slack_dump_and_reset_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:3:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_slack_dump_and_reset_z\tests\test_json_contracts.py:4:6 - error: Import "x_make_slack_dump_and_reset_z.json_contracts" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_slack_dump_and_reset_z\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_slack_dump_and_reset_z — ruff_check
  - Summary: ruff_check failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:17:11.817809+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
     --> tests\test_persistent_env_isolation.py:5:19
      |
    3 | import importlib
    4 | import sys
    …

- [ ] x_make_slack_dump_and_reset_z — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_z (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_z command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_z
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:17:11.665357+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
     --> tests\test_persistent_env_isolation.py:5:19
      |
    3 | import importlib
    4 | import sys
    …

- [ ] x_make_telemetry_vector_x — mypy
  - Summary: mypy failed for x_make_telemetry_vector_x (exit 1) cwd: C:\x_runner_x\x_make_telemetry_vector_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_telemetry_vector_x --strict --no-warn-unused-configs --show-error-code…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_telemetry_vector_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_telemetry_vector_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:17:41.921908+00:00
  - Suggested action: Investigate
  - Stdout preview:
    src\x_make_telemetry_vector_x\__init__.py:19: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:28: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:29: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:71: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:92: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    …
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_telemetry_vector_x — pyright
  - Summary: pyright failed for x_make_telemetry_vector_x (exit 3) cwd: C:\x_runner_x\x_make_telemetry_vector_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:17:41.925793+00:00 duration: 1.804s too…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_telemetry_vector_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:17:43.722776+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_telemetry_vector_x\src\x_make_telemetry_vector_x\__init__.py
      c:\x_runner_x\x_make_telemetry_vector_x\src\x_make_telemetry_vector_x\__init__.py:14:6 - error: Import "pydantic" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_telemetry_vector_x\tests\test_telemetry_vector.py
      c:\x_runner_x\x_make_telemetry_vector_x\tests\test_telemetry_vector.py:7:8 - error: Import "pytest" could not be resolved (reportMissingImports)
    2 errors, 0 warnings, 0 informations
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_telemetry_vector_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_who_is_John_Connor_x — black
  - Summary: black failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff started_at: 2025-11-26T0…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.12.6
  - Captured: 2025-11-26T01:17:46.179042+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_make_who_is_John_Connor_x\__init__.py	2025-11-21 18:36:58.630485+00:00
    +++ C:\x_runner_x\x_make_who_is_John_Connor_x\__init__.py	2025-11-26 01:17:45.279565+00:00
    @@ -2,8 +2,8 @@
     
     from .john_connor_service import JohnConnorPersonaService
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_make_who_is_John_Connor_x\__init__.py
    would reformat C:\x_runner_x\x_make_who_is_John_Connor_x\john_connor_service.py
    would reformat C:\x_runner_x\x_make_who_is_John_Connor_x\SETUP_COPILOT_CLI.py
    would reformat C:\x_runner_x\x_make_who_is_John_Connor_x\x_cls_make_who_is_John_Connor_x.py
    would reformat C:\x_runner_x\x_make_who_is_John_Connor_x\who_is_jc.py
    …

- [ ] x_make_who_is_John_Connor_x — mypy
  - Summary: mypy failed for x_make_who_is_John_Connor_x (exit 2) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_who_is_John_Connor_x --strict --no-warn-unused-configs --show-erro…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_who_is_John_Connor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:17:46.697536+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_make_who_is_John_Connor_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_make_who_is_John_Connor_x — ruff_check
  - Summary: ruff_check failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-v…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:17:46.352145+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N999 Invalid module name: 'SETUP_COPILOT_CLI'
    --> SETUP_COPILOT_CLI.py:1:1
    
    RUF005 Consider iterable unpacking instead of concatenation
      --> SETUP_COPILOT_CLI.py:71:16
    …

- [ ] x_make_who_is_John_Connor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targ…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:17:44.270552+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N999 Invalid module name: 'SETUP_COPILOT_CLI'
    --> SETUP_COPILOT_CLI.py:1:1
    
    RUF005 Consider iterable unpacking instead of concatenation
      --> SETUP_COPILOT_CLI.py:71:16
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 2) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachab…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.18.2 (compiled: yes)
  - Captured: 2025-11-26T01:18:08.697044+00:00
  - Suggested action: Investigate
  - Stdout preview:
    projection.py: error: Source file found twice under different module names: "x_make_yahw_x.projection" and "projection"
    Found 1 error in 1 file (errors prevented further checking)
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_yahw_x — pyright
  - Summary: pyright failed for x_make_yahw_x (exit 3) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error started_at: 2025-11-26T01:18:08.706323+00:00 duration: 2.005s tool_version: pyright 1.1.4…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-26T01:18:10.704559+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_make_yahw_x\__init__.py
      c:\x_runner_x\x_make_yahw_x\__init__.py:3:6 - error: Import "x_make_yahw_x.x_cls_make_yahw_x" could not be resolved (reportMissingImports)
    c:\x_runner_x\x_make_yahw_x\tests\test_json_contracts.py
      c:\x_runner_x\x_make_yahw_x\tests\test_json_contracts.py:7:6 - error: Import "x_make_common_x.json_contracts" could not be resolved (reportMissingImports)
      c:\x_runner_x\x_make_yahw_x\tests\test_json_contracts.py:8:6 - error: Import "x_make_yahw_x.json_contracts" could not be resolved (reportMissingImports)
    …
  - Stderr preview:
    Config file "c:\x_runner_x\x_make_yahw_x\pyrightconfig.json" could not be parsed. Verify that format is correct.

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at: 202…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:18:08.234593+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> projection.py:6:29
      |
    5 | import json
    6 | from collections.abc import Mapping, Sequence
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311 started_at:…
  - Command: C:\x_runner_x\.venv\Scripts\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.6
  - Captured: 2025-11-26T01:18:08.077162+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> projection.py:6:29
      |
    5 | import json
    6 | from collections.abc import Mapping, Sequence
    …
