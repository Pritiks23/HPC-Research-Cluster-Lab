# Incident Report: Compute Node Failure

## Summary

A compute node stopped accepting jobs.

## Symptoms

- Jobs remained pending
- Scheduler could not reach node

## Investigation

Checked node state:

```bash
sinfo
```

Reviewed daemon status:

```bash
systemctl status slurmd
```

## Root Cause

slurmd service had stopped unexpectedly.

## Resolution

```bash
sudo systemctl restart slurmd
```

Confirmed node returned to service.

## Prevention

- Add monitoring alerts
- Configure automatic service restart
