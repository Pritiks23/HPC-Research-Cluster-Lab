# Incident: Disk Full

## Summary
Job execution failed due to insufficient disk space on a compute node.

## Response Steps
1. Identify utilization with `df -h` and `du -sh /var/log/*`.
2. Clear temporary files and rotate/archive old logs.
3. Confirm free space threshold is restored.
4. Re-run failed jobs and monitor disk growth.
