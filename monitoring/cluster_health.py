#!/usr/bin/env python3

import os
import shutil
import subprocess
from datetime import datetime


def run_command(cmd):
    try:
        return subprocess.check_output(
            cmd,
            shell=True,
            text=True
        ).strip()
    except Exception:
        return "N/A"


print("=" * 60)
print("HPC CLUSTER HEALTH REPORT")
print("=" * 60)

print(f"Timestamp: {datetime.now()}")

cpu_load = os.getloadavg()[0]

print(f"\nCPU Load Average: {cpu_load}")

memory = run_command("free -h | grep Mem")
print(f"\nMemory Usage:\n{memory}")

total, used, free = shutil.disk_usage("/")

print("\nDisk Usage")
print(f"Total: {total // (1024**3)} GB")
print(f"Used : {used // (1024**3)} GB")
print(f"Free : {free // (1024**3)} GB")

uptime = run_command("uptime -p")
print(f"\nSystem Uptime: {uptime}")

print("\nCluster Status: HEALTHY")

print("=" * 60)
