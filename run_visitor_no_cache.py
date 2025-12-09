import sys

from x_make_github_visitor_x import init_main


def main() -> None:
    inst = init_main(enable_cache=False)
    try:
        inst.run_inspect_flow()
    except AssertionError as exc:
        sys.stderr.write(f"FAILED {exc}\n")
    else:
        sys.stdout.write("SUCCESS\n")
    sys.stdout.write(f"REPORT {inst.last_report_path}\n")


if __name__ == "__main__":
    main()
