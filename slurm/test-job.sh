#!/bin/bash
#SBATCH --job-name=test-job
#SBATCH --output=test-job-%j.out
#SBATCH --time=00:01:00
#SBATCH --partition=debug

set -euo pipefail

echo "Running on host: $(hostname)"
echo "Allocated CPUs: ${SLURM_CPUS_ON_NODE:-unknown}"
sleep 2
echo "Test job completed successfully."
