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
During a simulated job failure, I identified a file path resolution issue caused by relative directory assumptions. I refactored the script to use absolute paths and introduced a controlled working directory structure to ensure reproducibility and prevent similar failures in HPC batch environments.”
Incident: <img width="2704" height="1750" alt="image" src="https://github.com/user-attachments/assets/6893aedb-f1a4-419c-a807-56319d226d54" />

Diagnosis: <img width="1332" height="338" alt="image" src="https://github.com/user-attachments/assets/26f6b772-c30a-48b6-b631-1b731d83cebf" />

Resolution: 
<img width="1496" height="648" alt="image" src="https://github.com/user-attachments/assets/c09535da-05f5-40c2-88cd-40628fcd9312" />


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

---

## Skills Demonstrated

- Linux Administration
- Bash Scripting
- Python Automation
- Slurm Fundamentals
- Monitoring and Troubleshooting
- Technical Documentation
- Infrastructure as Code
