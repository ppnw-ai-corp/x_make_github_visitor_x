"""Compatibility shim exposing the GitHub visitor CLI at the repo root."""

from __future__ import annotations

import sys

from x_make_github_visitor_x.runner import *  # noqa: F403
from x_make_github_visitor_x.runner import _run_json_cli


def main() -> None:
    """Entry point retained for legacy bootstrap expectations."""

    _run_json_cli(sys.argv[1:])


if __name__ == "__main__":
    main()
