# app/main.py
import sys
from pathlib import Path
import argparse

from core.registry import get_all
from core.file_sniffer import sniff_file

def list_processors():
    """
    Print a short list of registered processor classes.
    """
    procs = get_all()
    if not procs:
        print("No processors registered.")
        return
    print("Registered processors:")
    for p in procs:
        print(f"- {p.id}: {p.name}")

def test_file(path_str: str):
    """
    Try to detect a processor for the given file, read it, and print a small summary.
    """
    p = Path(path_str)
    if not p.exists():
        print(f"File not found: {p}")
        return

    candidates = sniff_file(p)
    if not candidates:
        print("No matching processors found for this file.")
        return

    proc_cls = candidates[0]
    print(f"Using processor: {proc_cls.name}")
    proc = proc_cls()
    try:
        data = proc.read(p)
    except Exception as e:
        print("Error while reading file:", e)
        return

    try:
        plot = proc.plot(data)
    except Exception as e:
        print("Error while preparing plot payload:", e)
        return

    print("Plot payload type:", plot.get("type"))
    x = plot.get("x", [])
    print("Points loaded:", len(x))

def main(argv=None):
    """
    Simple CLI entry point.
    - No arguments lists processors.
    - --test <path> runs the test_file helper on the provided path.
    """
    parser = argparse.ArgumentParser(prog="app.main", description="Project CLI harness")
    parser.add_argument("--test", "-t", help="Path to a sample file to test the processor pipeline")
    args = parser.parse_args(argv)

    list_processors()

    if args.test:
        test_file(args.test)

if __name__ == "__main__":
    main()
