# Incident: Failed Job

## Summary
A submitted Slurm job failed unexpectedly during runtime.

## Response Steps
1. Inspect job status and reason via `sacct -j <jobid> --format=State,ExitCode`.
2. Review output/error logs produced by the job.
3. Validate requested resources and partition constraints.
4. Apply fixes and resubmit using `sbatch`.
