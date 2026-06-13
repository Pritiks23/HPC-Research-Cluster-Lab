# Incident Report: Failed Slurm Job

## Summary

A submitted research workload exited immediately.

## Investigation

```bash
sacct
```

```bash
cat job.log
```

## Root Cause

Incorrect file path in job script.

## Resolution

Updated path and resubmitted workload.

## Verification

Job completed successfully after correction.
