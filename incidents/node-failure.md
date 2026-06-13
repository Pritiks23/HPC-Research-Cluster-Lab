# Incident: Node Failure

## Summary
A compute node became unreachable and was marked down by Slurm.

## Response Steps
1. Verify node status with `sinfo -R`.
2. Drain the node with `scontrol update NodeName=<node> State=DRAIN Reason="investigation"`.
3. Restart `slurmd` and verify hardware/network health.
4. Return node to service with `scontrol update NodeName=<node> State=RESUME`.
