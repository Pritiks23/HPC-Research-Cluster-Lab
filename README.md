# HPC Research Cluster Lab

A portfolio project demonstrating core High Performance Computing (HPC) systems administration concepts including Linux administration, workload scheduling, monitoring, automation, and incident response.

## Project Objectives

This project simulates responsibilities commonly performed by HPC Systems Engineers supporting university and research computing environments.

Key areas demonstrated:

- Linux System Administration
- Slurm Workload Management
- Cluster Monitoring
- Infrastructure Automation
- Incident Response
- Documentation and Operations

---

## Repository Structure

```text
HPC-Research-Cluster-Lab/

README.md

architecture/
├── cluster-diagram.png

slurm/
├── slurm.conf
├── test-job.sh

monitoring/
├── cluster_health.py

automation/
├── install_packages.yml

incidents/
├── node-failure.md
├── disk-full.md
├── failed-job.md

screenshots/
├── sinfo.png
├── squeue.png
├── monitoring.png
```

---

## Simulated Cluster Architecture

```text
                  Head Node
          +---------------------+
          | Slurm Controller    |
          | Monitoring Scripts  |
          +----------+----------+
                     |
       +-------------+-------------+
       |                           |
+--------------+           +--------------+
| Compute Node |           | Compute Node |
| Research Jobs|           | Research Jobs|
+--------------+           +--------------+
```

---

## Monitoring

Cluster health information is collected using Python and includes:

- CPU Load
- Memory Utilization
- Disk Utilization
- System Uptime

Run:

```bash
python3 monitoring/cluster_health.py
```

---
<img width="2704" height="1750" alt="image" src="https://github.com/user-attachments/assets/1ad7ed21-6b88-42a3-8438-0ad9effaf744" />

## Example Workload

Run:

```bash
./slurm/test-job.sh
```

Example output:

```text
HPC Research Job Started
Running scientific workload...
Simulation Complete
```

---

## Automation

Ansible is used to automate package installation.

Run:

```bash
ansible-playbook automation/install_packages.yml
```

---
<img width="2704" height="1750" alt="image" src="https://github.com/user-attachments/assets/a15da322-68b6-4b6e-8694-db08e3351bb1" />


## Incident Response Scenarios
💥 INCIDENT: “HPC Job Failure Due to Missing Input File”
A simulated HPC batch job failed during execution due to a missing input file dependency. The incident was used to demonstrate troubleshooting workflows commonly performed in HPC environments, including job failure analysis, file system validation, and corrective remediation.

Incident: <img width="2704" height="1750" alt="image" src="https://github.com/user-attachments/assets/6893aedb-f1a4-419c-a807-56319d226d54" />
The job script attempted to read an input dataset (`missing_input.dat`) that was not present in the expected working directory. As a result, the job terminated with a file-not-found error during execution of the `cat` command.

Diagnosis: <img width="1332" height="338" alt="image" src="https://github.com/user-attachments/assets/26f6b772-c30a-48b6-b631-1b731d83cebf" />
The issue was diagnosed using standard Linux debugging techniques:

- Verified script contents and execution flow using `cat`
- Inspected file existence using `ls`
- Observed runtime error indicating missing file dependency
- Identified that the script relied on a relative file path, which caused a mismatch between expected and actual file locations

This confirmed the root cause as a **missing input file combined with an unvalidated file path assumption in the job script**.


Resolution: 
<img width="1496" height="648" alt="image" src="https://github.com/user-attachments/assets/c09535da-05f5-40c2-88cd-40628fcd9312" />
The issue was resolved by refactoring the job script to improve robustness and reproducibility:

- Introduced a defined working directory (`/tmp/hpc_incident`)
- Converted file paths to absolute references to eliminate ambiguity
- Added a conditional check to detect missing input files
- Implemented automatic generation of a fallback dataset when input data is unavailable
- Re-ran the job successfully, confirming recovery

---
The corrected workflow executed successfully, demonstrating proper handling of missing dependencies and improved fault tolerance. This exercise reflects real-world HPC operational practices where user-submitted jobs must be validated, debugged, and made resilient to common execution errors.

## Skills Demonstrated

- Linux command-line debugging
- File system and path resolution troubleshooting
- Shell scripting and error handling
- HPC-style job failure analysis
- Operational incident response workflow

Extra:

The project includes operational runbooks for:

1. Compute Node Failure
2. Disk Full Condition
3. Failed Slurm Job

Each incident includes:

- Symptoms
- Investigation
- Root Cause
- Resolution
- Prevention

