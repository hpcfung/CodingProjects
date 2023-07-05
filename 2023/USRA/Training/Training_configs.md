minimal: L=5, Rb=1.05, delta=-0.13, beta=0.5 to 64

### 7648476
same (print cpu count)

### 7648273
same  
18% epoch 0
```
Every 30.0s: nvidia-smi                                gra1338: Tue Jul  4 20:01:00 2023

Tue Jul  4 20:01:00 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   51C    P0    71W / 300W |   5167MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     23545      C   /opt/conda/bin/python            5164MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7648273
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:38
CPU Efficiency: 25.92% of 00:21:44 core-walltime
Job Wall-clock time: 00:05:26
Memory Utilized: 5.70 GB
Memory Efficiency: 35.64% of 16.00 GB
```
### 7648140
num_workers 4 (previously 0)  
4584MiB / 16384MiB?  
11% epoch 0 
```
Job ID: 7648140
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:22
CPU Efficiency: 25.80% of 00:20:48 core-walltime
Job Wall-clock time: 00:05:12
Memory Utilized: 5.48 GB
Memory Efficiency: 34.23% of 16.00 GB
```

### 7647973
batch 8192  
5168MiB / 16384MiB  
8% epoch 0  
```
Job ID: 7647973
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:09
CPU Efficiency: 25.08% of 00:20:32 core-walltime
Job Wall-clock time: 00:05:08
Memory Utilized: 7.18 GB
Memory Efficiency: 44.85% of 16.00 GB
```

### 7647766
batch 512 (higher VRAM usage?) and 5 mins (faster iteration)  
756MiB / 16384MiB  
10% epoch 0 (5 mins)
```
Job ID: 7647766
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:06:41
CPU Efficiency: 32.23% of 00:20:44 core-walltime
Job Wall-clock time: 00:05:11
Memory Utilized: 3.22 GB
Memory Efficiency: 20.14% of 16.00 GB
```

### 7647439
default: 4 cpu, 1 gpu  
VRAM: 504MiB / 16384MiB  
4%, epoch 0 (10 mins)
```
Job ID: 7647439
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:10:03
CPU Efficiency: 24.43% of 00:41:08 core-walltime
Job Wall-clock time: 00:10:17
Memory Utilized: 2.88 GB
Memory Efficiency: 17.98% of 16.00 GB
```
