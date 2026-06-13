# Incident Report: Disk Full

## Summary

Research jobs failed due to lack of disk space.

## Symptoms

- Output files failed to write
- Job failures increased

## Investigation

```bash
df -h
```

Filesystem reached maximum utilization.

## Root Cause

Large temporary files accumulated.

## Resolution

```bash
rm -rf /tmp/*
```

Storage usage returned to normal.

## Prevention

- Implement cleanup policies
- Monitor disk utilization
