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
            +----------------+
            |   Head Node    |
            | Slurm Control  |
            +--------+-------+
                     |
      +--------------+--------------+
      |                             |
+-----------+               +-----------+
| Compute 1 |               | Compute 2 |
+-----------+               +-----------+
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

## Incident Response Scenarios

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
