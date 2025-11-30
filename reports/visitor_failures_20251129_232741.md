# Visitor TODO Report

- Generated: 2025-11-29T23:27:41.185294+00:00
- Workspace: C:\x_runner_x
- Schema: x_make_github_visitor_x.run/1.0
- Total repositories: 44
- Failing tools: 52
- Recorded failures: 52

- [ ] x_0_make_ppnw_dot_ai_x — black
  - Summary: black failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff started…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.14.0
  - Captured: 2025-11-29T23:14:32.130532+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_0_make_ppnw_dot_ai_x\typings\reportlab\graphics\renderPM\__init__.pyi	2025-11-29 23:09:54.886175+00:00
    +++ C:\x_runner_x\x_0_make_ppnw_dot_ai_x\typings\reportlab\graphics\renderPM\__init__.pyi	2025-11-29 23:14:31.796774+00:00
    @@ -1,6 +1,5 @@
    -
     from typing import Protocol
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_x\typings\reportlab\graphics\renderPM\__init__.pyi
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_x\typings\reportlab\graphics\renderPM.pyi
    would reformat C:\x_runner_x\x_0_make_ppnw_dot_ai_x\typings\svglib\svglib.pyi
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_0_make_ppnw_dot_ai_x — mypy
  - Summary: mypy failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_0_make_ppnw_dot_ai_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:14:32.724661+00:00
  - Suggested action: Investigate
  - Stdout preview:
    svg_to_many.py:18: error: Expression has type "Any"  [misc]
    svg_to_many.py:87: error: Expression type contains "Any" (has type "Callable[[Path], Iterator[Any]]")  [misc]
    svg_to_many.py:88: error: Return type becomes "Iterator[Any]" due to an unfollowed import  [no-any-unimported]
    svg_to_many.py:88: error: Type of decorated function contains type "Any" ("Callable[[Path], _GeneratorContextManager[Any, None, None]]")  [misc]
    svg_to_many.py:89: error: Target type of cast becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_check
  - Summary: ruff_check failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:14:32.275828+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N802 Function name `drawToFile` should be lowercase
     --> typings\reportlab\graphics\renderPM.pyi:5:9
      |
    4 | class RenderEngine(Protocol):
    5 |     def drawToFile(
    …

- [ ] x_0_make_ppnw_dot_ai_x — ruff_fix
  - Summary: ruff_fix failed for x_0_make_ppnw_dot_ai_x (exit 1) cwd: C:\x_runner_x\x_0_make_ppnw_dot_ai_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_0_make_ppnw_dot_ai_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:14:30.644753+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N802 Function name `drawToFile` should be lowercase
     --> typings\reportlab\graphics\renderPM.pyi:5:9
      |
    4 | class RenderEngine(Protocol):
    5 |     def drawToFile(
    …

- [ ] x_legatus_capsula_calculus_x — mypy
  - Summary: mypy failed for x_legatus_capsula_calculus_x (exit 1) cwd: C:\x_runner_x\x_legatus_capsula_calculus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_capsula_calculus_x --strict --no-w…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_capsula_calculus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_capsula_calculus_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:16:05.975381+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_legatus_capsula_calculus_x\inference\inference_service.py:28: error: Skipping analyzing "uvicorn.main": module is installed, but missing library stubs or py.typed marker  [import-untyped]
    x_legatus_capsula_calculus_x\inference\inference_service.py:28: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_legatus_capsula_calculus_x\inference\inference_service.py:30: error: Expression has type "Any"  [misc]
    x_legatus_capsula_calculus_x\inference\inference_service.py:37: error: Class cannot subclass "BaseModel" (has type "Any")  [misc]
    x_legatus_capsula_calculus_x\inference\inference_service.py:37: error: Base type BaseModel becomes "Any" due to an unfollowed import  [no-any-unimported]
    …

- [ ] x_legatus_inceptio_praesidium_x — mypy
  - Summary: mypy failed for x_legatus_inceptio_praesidium_x (exit 1) cwd: C:\x_runner_x\x_legatus_inceptio_praesidium_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_inceptio_praesidium_x --stri…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_inceptio_praesidium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_inceptio_praesidium_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:16:41.879324+00:00
  - Suggested action: Investigate
  - Stdout preview:
    inceptio_praesidium\__init__.py:13: error: Redundant cast to Module  [redundant-cast]
    inceptio_praesidium\__init__.py:14: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    inceptio_praesidium\__init__.py:15: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    inceptio_praesidium\__init__.py:17: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    inceptio_praesidium\__init__.py:18: error: Expression type contains "Any" (has type "Any | list[Any]")  [misc]
    …

- [ ] x_legatus_mentis_multiplex_x — black
  - Summary: black failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.14.0
  - Captured: 2025-11-29T23:17:18.124412+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core_stub\messages\__init__.pyi	2025-11-29 08:40:54.443278+00:00
    +++ C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core_stub\messages\__init__.pyi	2025-11-29 23:17:17.822494+00:00
    @@ -1,10 +1,9 @@
     class SystemMessage:
         content: object
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core_stub\messages\__init__.pyi
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\langchain_core_stub\prompts\__init__.py
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\scripts\langchain_probe.py
    would reformat C:\x_runner_x\x_legatus_mentis_multiplex_x\typings\langchain_core\messages\__init__.pyi
    
    …

- [ ] x_legatus_mentis_multiplex_x — pyright
  - Summary: pyright failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:17:20.…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:17:22.284052+00:00
  - Suggested action: Investigate
  - Stdout preview:
    c:\x_runner_x\x_legatus_mentis_multiplex_x\scripts\langchain_probe.py
      c:\x_runner_x\x_legatus_mentis_multiplex_x\scripts\langchain_probe.py:40:36 - error: Method "from_messages" cannot be called because it is abstract and unimplemented (reportAbstractUsage)
    1 error, 0 warnings, 0 informations

- [ ] x_legatus_mentis_multiplex_x — ruff_check
  - Summary: ruff_check failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:17:18.269997+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TID252 Prefer absolute imports over relative imports from parent modules
     --> langchain_core_stub\prompts\__init__.py:6:1
      |
    4 | from typing import ClassVar, TypeAlias
    5 |
    …

- [ ] x_legatus_mentis_multiplex_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_mentis_multiplex_x (exit 1) cwd: C:\x_runner_x\x_legatus_mentis_multiplex_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC00…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_mentis_multiplex_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:17:16.346779+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TID252 Prefer absolute imports over relative imports from parent modules
     --> langchain_core_stub\prompts\__init__.py:6:1
      |
    4 | from typing import ClassVar, TypeAlias
    5 |
    …

- [ ] x_legatus_politia_tabularium_x — black
  - Summary: black failed for x_legatus_politia_tabularium_x (exit 1) cwd: C:\x_runner_x\x_legatus_politia_tabularium_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --chec…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_politia_tabularium_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.14.0
  - Captured: 2025-11-29T23:17:32.540875+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_politia_tabularium_x\politia_tabularium\markdown_audit.py	2025-11-29 15:16:43.583320+00:00
    +++ C:\x_runner_x\x_legatus_politia_tabularium_x\politia_tabularium\markdown_audit.py	2025-11-29 23:17:32.125381+00:00
    @@ -15,10 +15,12 @@
         "`markdown_inventory.json`. Update the Owner, Status, and Notes columns "
         "as reviews progress. Status legend: `TBD`, `In Review`, `Complete`.\n\n"
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_politia_tabularium_x\politia_tabularium\markdown_audit.py
    would reformat C:\x_runner_x\x_legatus_politia_tabularium_x\politia_tabularium\release_checklists.py
    would reformat C:\x_runner_x\x_legatus_politia_tabularium_x\politia_tabularium\cli.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    …

- [ ] x_legatus_politia_tabularium_x — mypy
  - Summary: mypy failed for x_legatus_politia_tabularium_x (exit 2) cwd: C:\x_runner_x\x_legatus_politia_tabularium_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_politia_tabularium_x --strict …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_politia_tabularium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 2
  - Repo path: C:\x_runner_x\x_legatus_politia_tabularium_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:17:33.103649+00:00
  - Suggested action: Investigate
  - Stderr preview:
    Package 'x_legatus_politia_tabularium_x' cannot be type checked due to missing py.typed marker. See https://mypy.readthedocs.io/en/stable/installed_packages.html for more details

- [ ] x_legatus_scriba_machina_x — mypy
  - Summary: mypy failed for x_legatus_scriba_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_scriba_machina_x --strict --no-warn-un…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_scriba_machina_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:18:33.678299+00:00
  - Suggested action: Investigate
  - Stdout preview:
    scripts\verify_factory_outputs.py:20: error: Explicit "Any" is not allowed  [explicit-any]
    scripts\verify_factory_outputs.py:22: error: Expression has type "Any"  [misc]
    scripts\verify_factory_outputs.py:23: error: Expression has type "Any"  [misc]
    scripts\verify_factory_outputs.py:26: error: Expression type contains "Any" (has type "list[dict[str, Any]]")  [misc]
    scripts\verify_factory_outputs.py:35: error: Explicit "Any" is not allowed  [explicit-any]
    …

- [ ] x_legatus_scriba_machina_x — ruff_check
  - Summary: ruff_check failed for x_legatus_scriba_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:18:21.476942+00:00
  - Suggested action: Investigate

- [ ] x_legatus_scriba_machina_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_scriba_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_scriba_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_scriba_machina_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:18:19.095761+00:00
  - Suggested action: Investigate

- [ ] x_legatus_segmentum_judicium_x — mypy
  - Summary: mypy failed for x_legatus_segmentum_judicium_x (exit 1) cwd: C:\x_runner_x\x_legatus_segmentum_judicium_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_segmentum_judicium_x --strict …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_segmentum_judicium_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_segmentum_judicium_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:19:16.423401+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tools\midnight_firefight.py:11: error: Expression type contains "Any" (has type "Any | type[c_long]")  [misc]
    tools\midnight_firefight.py:54: error: Expression type contains "Any" (has type "type[_Pointer[Any]]")  [misc]
    tools\install_vlc_backend.py:70: error: Statement is unreachable  [unreachable]
    tools\install_vlc_backend.py:142: error: Expression has type "Any"  [misc]
    tools\bootstrap_chocolatey.py:28: error: Expression has type "Any"  [misc]
    …

- [ ] x_legatus_senatus_machina_x — mypy
  - Summary: mypy failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_senatus_machina_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_senatus_machina_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:19:33.516538+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_legatus_senatus_machina_x\models.py:31: error: Explicit "Any" is not allowed  [explicit-any]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_legatus_senatus_machina_x\models.py:32: error: Expression type contains "Any" (has type "Any | str")  [misc]
    x_legatus_senatus_machina_x\models.py:36: error: Expression type contains "Any" (has type "Mapping[str, Any]")  [misc]
    …

- [ ] x_legatus_senatus_machina_x — ruff_check
  - Summary: ruff_check failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:19:29.508556+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use `list.extend` to create a transformed list
      --> models.py:73:25
       |
    71 |                 for item in intel_raw:
    72 |                     if isinstance(item, Mapping):
    …

- [ ] x_legatus_senatus_machina_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_senatus_machina_x (exit 1) cwd: C:\x_runner_x\x_legatus_senatus_machina_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_senatus_machina_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:19:27.538616+00:00
  - Suggested action: Investigate
  - Stdout preview:
    PERF401 Use `list.extend` to create a transformed list
      --> models.py:73:25
       |
    71 |                 for item in intel_raw:
    72 |                     if isinstance(item, Mapping):
    …

- [ ] x_legatus_tactica_impetus_x — black
  - Summary: black failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --di…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.14.0
  - Captured: 2025-11-29T23:19:53.568529+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi	2025-11-28 09:43:03.405655+00:00
    +++ C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi	2025-11-29 23:19:53.348080+00:00
    @@ -1,33 +1,24 @@
     from typing import Any, Protocol, TypeAlias
     
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_tactica_impetus_x\typings\ujson.pyi
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 43 files would be left unchanged.

- [ ] x_legatus_tactica_impetus_x — mypy
  - Summary: mypy failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_tactica_impetus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:19:54.357237+00:00
  - Suggested action: Investigate
  - Stdout preview:
    typings\ujson.pyi:3: error: Explicit "Any" is not allowed  [explicit-any]
    typings\ujson.pyi:17: error: Explicit "Any" is not allowed  [explicit-any]
    typings\ujson.pyi:29: error: Explicit "Any" is not allowed  [explicit-any]
    firmware\lib\x_cls_display_tft_x.py:49: error: Expression type contains "Any" (has type "Any | None")  [misc]
    firmware\lib\x_cls_display_tft_x.py:50: error: Expression type contains "Any" (has type "Any | None")  [misc]
    …

- [ ] x_legatus_tactica_impetus_x — ruff_check
  - Summary: ruff_check failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:19:53.705433+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:41:22
       |
    40 | class _WLAN(Protocol):
    41 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_tactica_impetus_x — ruff_fix
  - Summary: ruff_fix failed for x_legatus_tactica_impetus_x (exit 1) cwd: C:\x_runner_x\x_legatus_tactica_impetus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_tactica_impetus_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:19:51.933217+00:00
  - Suggested action: Investigate
  - Stdout preview:
    FBT001 Boolean-typed positional argument in function definition
      --> firmware\boot.py:41:22
       |
    40 | class _WLAN(Protocol):
    41 |     def active(self, is_active: bool | None = ...) -> bool: ...
    …

- [ ] x_legatus_vigil_nexus_x — black
  - Summary: black failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff start…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m black . --line-length 88 --target-version py311 --check --diff
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: python -m black, 25.11.0 (compiled: yes)
Python (CPython) 3.14.0
  - Captured: 2025-11-29T23:20:41.774259+00:00
  - Suggested action: Investigate
  - Stdout preview:
    --- C:\x_runner_x\x_legatus_vigil_nexus_x\clients\windows\main.py	2025-11-29 10:01:36.013411+00:00
    +++ C:\x_runner_x\x_legatus_vigil_nexus_x\clients\windows\main.py	2025-11-29 23:20:41.543215+00:00
    @@ -362,13 +362,11 @@
         if not isinstance(factory_token_obj, str):
             factory_token = str(factory_token_obj)
    …
  - Stderr preview:
    would reformat C:\x_runner_x\x_legatus_vigil_nexus_x\clients\windows\main.py
    
    Oh no! \U0001f4a5 \U0001f494 \U0001f4a5
    1 file would be reformatted, 19 files would be left unchanged.

- [ ] x_legatus_vigil_nexus_x — mypy
  - Summary: mypy failed for x_legatus_vigil_nexus_x (exit 1) cwd: C:\x_runner_x\x_legatus_vigil_nexus_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-conf…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_legatus_vigil_nexus_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_legatus_vigil_nexus_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:20:48.785287+00:00
  - Suggested action: Investigate
  - Stdout preview:
    control_plane\config.py:22: error: Expression type contains "Any" (has type "Callable[[Callable[..., _T]], _lru_cache_wrapper[_T]]")  [misc]
    control_plane\models.py:3: error: Unused "type: ignore" comment  [unused-ignore]
    control_plane\models.py:6: error: Class cannot subclass "BaseModel" (has type "Any")  [misc]
    control_plane\models.py:6: error: Base type BaseModel becomes "Any" due to an unfollowed import  [no-any-unimported]
    control_plane\models.py:11: error: Class cannot subclass "BaseModel" (has type "Any")  [misc]
    …

- [ ] x_make_copilot_cli_one_time_setup_x — mypy
  - Summary: mypy failed for x_make_copilot_cli_one_time_setup_x (exit 1) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_copilot_cli_one_time_se…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_copilot_cli_one_time_setup_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:21:40.441987+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_copilot_cli_one_time_setup_x.py:16: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_copilot_cli_one_time_setup_x.py:44: error: Explicit "Any" is not allowed  [explicit-any]
    x_cls_make_copilot_cli_one_time_setup_x.py:57: error: Unused "type: ignore" comment  [unused-ignore]
    x_cls_make_copilot_cli_one_time_setup_x.py:58: error: Expression type contains "Any" (has type "tuple[Any, int]")  [misc]
    x_cls_make_copilot_cli_one_time_setup_x.py:58: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_copilot_cli_one_time_setup_x — ruff_check
  - Summary: ruff_check failed for x_make_copilot_cli_one_time_setup_x (exit 1) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,CO…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:21:37.476555+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (94 > 88)
       --> x_cls_make_copilot_cli_one_time_setup_x.py:122:89
        |
    120 |     command = (
    121 |         "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; "
    …

- [ ] x_make_copilot_cli_one_time_setup_x — ruff_fix
  - Summary: ruff_fix failed for x_make_copilot_cli_one_time_setup_x (exit 1) cwd: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_copilot_cli_one_time_setup_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:21:36.017444+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (94 > 88)
       --> x_cls_make_copilot_cli_one_time_setup_x.py:122:89
        |
    120 |     command = (
    121 |         "Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force; "
    …

- [ ] x_make_github_visitor_x — mypy
  - Summary: mypy failed for x_make_github_visitor_x (exit 1) cwd: C:\x_runner_x\x_make_github_visitor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-conf…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_github_visitor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_github_visitor_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:23:00.452030+00:00
  - Suggested action: Investigate
  - Stdout preview:
    report_validator.py:212: error: Expression type contains "Any" (has type "tuple[int, Any]")  [misc]
    report_validator.py:212: error: Expression has type "Any"  [misc]
    report_validator.py:212: error: Expression type contains "Any" (has type "enumerate[Any]")  [misc]
    report_validator.py:213: error: Expression has type "Any"  [misc]
    report_validator.py:300: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_graphviz_x — mypy
  - Summary: mypy failed for x_make_graphviz_x (exit 1) cwd: C:\x_runner_x\x_make_graphviz_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-c…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_graphviz_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_graphviz_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:23:36.826181+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_graphviz_x.py:23: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_graphviz_x.py:23: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_graphviz_x.py:23: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_graphviz_x.py:23: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_graphviz_x.py:512: error: Expression has type "Any"  [misc]
    …
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_mermaid_x — pyright
  - Summary: pyright failed for x_make_mermaid_x (exit 3) cwd: C:\x_runner_x\x_make_mermaid_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:24:08.057090+00:00 duration: 2…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_mermaid_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:24:10.838823+00:00
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
  - Summary: pyright failed for x_make_persistent_env_var_x (exit 3) cwd: C:\x_runner_x\x_make_persistent_env_var_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:24:23.85…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_persistent_env_var_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:24:26.412637+00:00
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
  - Summary: pyright failed for x_make_pip_updates_x (exit 3) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:24:43.272836+00:00 dur…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:24:45.502919+00:00
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
  - Summary: ruff_check failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:24:43.266716+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
      --> tests\test_pip_updates.py:10:29
       |
     8 | import subprocess
     9 | import typing
    …

- [ ] x_make_pip_updates_x — ruff_fix
  - Summary: ruff_fix failed for x_make_pip_updates_x (exit 1) cwd: C:\x_runner_x\x_make_pip_updates_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-len…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pip_updates_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:24:43.137706+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
      --> tests\test_pip_updates.py:10:29
       |
     8 | import subprocess
     9 | import typing
    …

- [ ] x_make_progress_board_x — mypy
  - Summary: mypy failed for x_make_progress_board_x (exit 1) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-conf…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_progress_board_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:25:03.979430+00:00
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
  - Summary: pyright failed for x_make_progress_board_x (exit 3) cwd: C:\x_runner_x\x_make_progress_board_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:25:03.982438+00:…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_progress_board_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:25:06.126172+00:00
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
  - Summary: pyright failed for x_make_py_mod_sideload_x (exit 3) cwd: C:\x_runner_x\x_make_py_mod_sideload_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:25:34.552923+0…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_py_mod_sideload_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:25:36.731040+00:00
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
  - Summary: mypy failed for x_make_pypi_x (exit 1) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_pypi_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:26:01.213779+00:00
  - Suggested action: Investigate
  - Stdout preview:
    x_cls_make_pypi_x.py:28: error: Library stubs not installed for "jsonschema"  [import-untyped]
    x_cls_make_pypi_x.py:28: note: Hint: "python3 -m pip install types-jsonschema"
    x_cls_make_pypi_x.py:28: note: (or run "mypy --install-types" to install all missing stub packages)
    x_cls_make_pypi_x.py:28: note: See https://mypy.readthedocs.io/en/stable/running_mypy.html#missing-imports
    x_cls_make_pypi_x.py:548: error: Expression has type "Any"  [misc]
    …
  - Stderr preview:
    mypy.ini: File contains no section headers.
    file: 'mypy.ini', line: 1
    'ï»¿[mypy]\n'

- [ ] x_make_pypi_x — pyright
  - Summary: pyright failed for x_make_pypi_x (exit 3) cwd: C:\x_runner_x\x_make_pypi_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error started_at: 2025-11-29T23:26:01.216727+00:00 duration: 2.992s …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m pyright . --level error
  - Exit: exit 3
  - Repo path: C:\x_runner_x\x_make_pypi_x
  - Tool version: pyright 1.1.407
  - Captured: 2025-11-29T23:26:04.208343+00:00
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

- [ ] x_make_slack_dump_and_reset_x — mypy
  - Summary: mypy failed for x_make_slack_dump_and_reset_x (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_slack_dump_and_reset_x --strict --n…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_slack_dump_and_reset_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:26:32.092449+00:00
  - Suggested action: Investigate
  - Stdout preview:
    tests\test_persistent_env_isolation.py:14: error: Expression type contains "Any" (has type "Any | None")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:675: error: Expression type contains "Any" (has type "list[Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:953: error: Expression type contains "Any" (has type "Callable[[Any], Any]")  [misc]
    x_cls_make_slack_dump_and_reset_x.py:953: error: Expression has type "Any"  [misc]
    x_cls_make_slack_dump_and_reset_x.py:1070: error: Expression has type "Any"  [misc]
    …

- [ ] x_make_slack_dump_and_reset_x — ruff_check
  - Summary: ruff_check failed for x_make_slack_dump_and_reset_x (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:26:25.689231+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
     --> tests\test_persistent_env_isolation.py:5:19
      |
    3 | import importlib
    4 | import sys
    …

- [ ] x_make_slack_dump_and_reset_x — ruff_fix
  - Summary: ruff_fix failed for x_make_slack_dump_and_reset_x (exit 1) cwd: C:\x_runner_x\x_make_slack_dump_and_reset_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_slack_dump_and_reset_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:26:24.049032+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `types.ModuleType` into a type-checking block
     --> tests\test_persistent_env_isolation.py:5:19
      |
    3 | import importlib
    4 | import sys
    …

- [ ] x_make_telemetry_vector_x — mypy
  - Summary: mypy failed for x_make_telemetry_vector_x (exit 1) cwd: C:\x_runner_x\x_make_telemetry_vector_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_telemetry_vector_x --strict --no-warn-unuse…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_telemetry_vector_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_telemetry_vector_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:26:57.131127+00:00
  - Suggested action: Investigate
  - Stdout preview:
    src\x_make_telemetry_vector_x\__init__.py:11: error: Module "datetime" has no attribute "UTC"  [attr-defined]
    src\x_make_telemetry_vector_x\__init__.py:17: error: Expression has type "Any"  [misc]
    src\x_make_telemetry_vector_x\__init__.py:29: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:30: error: Explicit "Any" is not allowed  [explicit-any]
    src\x_make_telemetry_vector_x\__init__.py:32: error: Expression type contains "Any" (has type "Callable[[Callable[..., _T]], Callable[..., _T]]")  [misc]
    …

- [ ] x_make_telemetry_vector_x — ruff_check
  - Summary: ruff_check failed for x_make_telemetry_vector_x (exit 1) cwd: C:\x_runner_x\x_make_telemetry_vector_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --li…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_telemetry_vector_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:26:54.494597+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (102 > 88)
     --> __init__.py:3:89
      |
    1 | """Workspace shim that exposes the telemetry toolkit when the repo root is on sys.path.
    2 |
    …

- [ ] x_make_telemetry_vector_x — ruff_fix
  - Summary: ruff_fix failed for x_make_telemetry_vector_x (exit 1) cwd: C:\x_runner_x\x_make_telemetry_vector_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_telemetry_vector_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:26:52.852246+00:00
  - Suggested action: Investigate
  - Stdout preview:
    E501 Line too long (102 > 88)
     --> __init__.py:3:89
      |
    1 | """Workspace shim that exposes the telemetry toolkit when the repo root is on sys.path.
    2 |
    …

- [ ] x_make_who_is_John_Connor_x — mypy
  - Summary: mypy failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_who_is_John_Connor_x --strict --no-warn…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_who_is_John_Connor_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:27:07.033189+00:00
  - Suggested action: Investigate
  - Stdout preview:
    SETUP_COPILOT_CLI.py:71: error: Expression type contains "Any" (has type "tuple[str, str, str, str, str, str, str, str, str]")  [misc]
    SETUP_COPILOT_CLI.py:114: error: Expression has type "Any"  [misc]
    who_is_jc.py:18: error: Unused "type: ignore" comment  [unused-ignore]
    who_is_jc.py:55: error: Unused "type: ignore" comment  [unused-ignore]
    who_is_jc.py:56: error: Expression type contains "Any" (has type "tuple[Any, int]")  [misc]
    …

- [ ] x_make_who_is_John_Connor_x — ruff_check
  - Summary: ruff_check failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 …
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:27:04.174155+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N999 Invalid module name: 'SETUP_COPILOT_CLI'
    --> SETUP_COPILOT_CLI.py:1:1
    
    RUF005 Consider iterable unpacking instead of concatenation
      --> SETUP_COPILOT_CLI.py:71:16
    …

- [ ] x_make_who_is_John_Connor_x — ruff_fix
  - Summary: ruff_fix failed for x_make_who_is_John_Connor_x (exit 1) cwd: C:\x_runner_x\x_make_who_is_John_Connor_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_who_is_John_Connor_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:27:02.798856+00:00
  - Suggested action: Investigate
  - Stdout preview:
    N999 Invalid module name: 'SETUP_COPILOT_CLI'
    --> SETUP_COPILOT_CLI.py:1:1
    
    RUF005 Consider iterable unpacking instead of concatenation
      --> SETUP_COPILOT_CLI.py:71:16
    …

- [ ] x_make_yahw_x — mypy
  - Summary: mypy failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m mypy --package x_make_yahw_x --strict --no-warn-unused-configs --show-error-codes --warn-return-any --warn-unreachable --disallow-any-unimported --disallow-any-expr --disallow-any-decorated --disallow-any-explicit
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: mypy 1.19.0 (compiled: yes)
  - Captured: 2025-11-29T23:27:38.597040+00:00
  - Suggested action: Investigate
  - Stdout preview:
    projection.py:82: error: Expression type contains "Any" (has type "dict[str, Any]")  [misc]
    Found 1 error in 1 file (checked 14 source files)

- [ ] x_make_yahw_x — ruff_check
  - Summary: ruff_check failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-ve…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:27:35.169972+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> projection.py:6:29
      |
    5 | import json
    6 | from collections.abc import Mapping, Sequence
    …

- [ ] x_make_yahw_x — ruff_fix
  - Summary: ruff_fix failed for x_make_yahw_x (exit 1) cwd: C:\x_runner_x\x_make_yahw_x command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --targe…
  - Command: C:\Users\eye43\AppData\Local\Programs\Python\Python314\python.exe -m ruff check . --fix --select ALL --ignore D,COM812,ISC001,T20 --line-length 88 --target-version py311
  - Exit: exit 1
  - Repo path: C:\x_runner_x\x_make_yahw_x
  - Tool version: ruff 0.14.7
  - Captured: 2025-11-29T23:27:33.660249+00:00
  - Suggested action: Investigate
  - Stdout preview:
    TC003 Move standard library import `collections.abc.Mapping` into a type-checking block
     --> projection.py:6:29
      |
    5 | import json
    6 | from collections.abc import Mapping, Sequence
    …
