#!/usr/bin/env python3
"""Basic cluster health check utility for the lab."""

from __future__ import annotations

import subprocess
import sys


def run_command(command: list[str]) -> tuple[int, str, str]:
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=False)
        return result.returncode, result.stdout.strip(), result.stderr.strip()
    except FileNotFoundError as error:
        return 127, "", str(error)


def main() -> int:
    checks = {
        "sinfo": ["sinfo", "-h"],
        "squeue": ["squeue", "-h"],
    }

    overall_ok = True
    for name, command in checks.items():
        code, stdout, stderr = run_command(command)
        if code == 0:
            line_count = len(stdout.splitlines()) if stdout else 0
            print(f"[OK] {name} reachable ({line_count} line(s) returned)")
        else:
            overall_ok = False
            details = stderr or stdout or "no output"
            print(f"[FAIL] {name} check failed: {details}")

    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
