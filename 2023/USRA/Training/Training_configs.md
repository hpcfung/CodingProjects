minimal: L=5, Rb=1.05, delta=-0.13, beta=0.5 to 64

### 7665062
save to RAM, 1 gpu, 4 cpus, 4 workers  
48% epoch 0
```
Every 15.0s: nvidia-smi                                gra1338: Wed Jul  5 12:56:47 2023

Wed Jul  5 12:56:47 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |                    0 |
| N/A   43C    P0    60W / 300W |   1681MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     16181      C   /opt/conda/bin/python            1678MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7665062
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:11:15
CPU Efficiency: 28.12% of 00:40:00 core-walltime
Job Wall-clock time: 00:10:00
Memory Utilized: 5.55 GB
Memory Efficiency: 34.68% of 16.00 GB
```
### 7655222
2 gpus, 8 cpus, 8 workers  
76%
```
Every 15.0s: nvidia-smi                                gra1338: Wed Jul  5 00:23:51 2023

Wed Jul  5 00:23:51 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |                    0 |
| N/A   44C    P0    60W / 300W |   2209MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+
|   1  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   51C    P0    71W / 300W |   2209MiB / 32768MiB |    100%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
```
```
Job ID: 7655222
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 00:26:21
CPU Efficiency: 32.45% of 01:21:12 core-walltime
Job Wall-clock time: 00:10:09
Memory Utilized: 16.78 GB
Memory Efficiency: 52.44% of 32.00 GB
```

### 7654335
2 cores, 2 workers  
57%
```
Every 15.0s: nvidia-smi                                gra1338: Wed Jul  5 00:03:21 2023

Wed Jul  5 00:03:21 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |                    0 |
| N/A   43C    P0    60W / 300W |   1681MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     33284      C   /opt/conda/bin/python            1678MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7654335
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:11:38
CPU Efficiency: 55.57% of 00:20:56 core-walltime
Job Wall-clock time: 00:10:28
Memory Utilized: 4.21 GB
Memory Efficiency: 26.32% of 16.00 GB
```

### 7653953
8 workers  
45%
```
Every 15.0s: nvidia-smi                                                                  gra1338: Tue Jul  4 23:47:40 2023

Tue Jul  4 23:47:40 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |                    0 |
| N/A   43C    P0    60W / 300W |   1681MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     23601      C   /opt/conda/bin/python            1678MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7653953
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 00:11:40
CPU Efficiency: 14.25% of 01:21:52 core-walltime
Job Wall-clock time: 00:10:14
Memory Utilized: 7.99 GB
Memory Efficiency: 49.95% of 16.00 GB
```

### 7653720
8 cores  
49% epoch 0
```
Every 15.0s: nvidia-smi                                gra1338: Tue Jul  4 23:25:28 2023

Tue Jul  4 23:25:28 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:15:00.0 Off |                    0 |
| N/A   42C    P0    67W / 300W |   1681MiB / 32768MiB |     20%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     40274      C   /opt/conda/bin/python            1678MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7653720
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 00:11:33
CPU Efficiency: 14.27% of 01:20:56 core-walltime
Job Wall-clock time: 00:10:07
Memory Utilized: 5.55 GB
Memory Efficiency: 34.71% of 16.00 GB
```
### 7649790
batch 2048  
57% epoch 0
```
Every 15.0s: nvidia-smi                                gra1337: Tue Jul  4 21:21:07 2023

Tue Jul  4 21:21:07 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:89:00.0 Off |                    0 |
| N/A   37C    P0    55W / 300W |   1681MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     37180      C   /opt/conda/bin/python            1678MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7649790
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:11:52
CPU Efficiency: 28.39% of 00:41:48 core-walltime
Job Wall-clock time: 00:10:27
Memory Utilized: 5.57 GB
Memory Efficiency: 34.80% of 16.00 GB
```

### 7649408
batch 32768, 10 mins  
29% epoch 0 (10 mins)
```
Every 15.0s: nvidia-smi                                gra1337: Tue Jul  4 21:09:27 2023

Tue Jul  4 21:09:28 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:89:00.0 Off |                    0 |
| N/A   39C    P0    66W / 300W |  19261MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     32886      C   /opt/conda/bin/python           19258MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7649408
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:10:23
CPU Efficiency: 25.12% of 00:41:20 core-walltime
Job Wall-clock time: 00:10:20
Memory Utilized: 7.61 GB
Memory Efficiency: 47.59% of 16.00 GB
```
### 7649184
batch 65536  
did not start training?
```
Every 15.0s: nvidia-smi                                gra1337: Tue Jul  4 20:54:26 2023

Tue Jul  4 20:54:26 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:89:00.0 Off |                    0 |
| N/A   36C    P0    41W / 300W |      0MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7649184
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:13
CPU Efficiency: 24.08% of 00:21:40 core-walltime
Job Wall-clock time: 00:05:25
Memory Utilized: 6.22 GB
Memory Efficiency: 38.85% of 16.00 GB
```

### 7649018
num_workers = 4, precision 16  
18% epoch 0
```
Every 15.0s: nvidia-smi                                gra1338: Tue Jul  4 20:41:40 2023

Tue Jul  4 20:41:40 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   49C    P0    58W / 300W |   5747MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A     20271      C   /opt/conda/bin/python            5744MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7649018
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:29
CPU Efficiency: 25.86% of 00:21:12 core-walltime
Job Wall-clock time: 00:05:18
Memory Utilized: 5.72 GB
Memory Efficiency: 35.72% of 16.00 GB
```
### 7648855
num_workers = 8  
7% epoch 0
```
Every 30.0s: nvidia-smi                                gra1338: Tue Jul  4 20:34:23 2023

Tue Jul  4 20:34:23 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   50C    P0    58W / 300W |   5167MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      3863      C   /opt/conda/bin/python            5164MiB |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7648855
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:04:56
CPU Efficiency: 23.79% of 00:20:44 core-walltime
Job Wall-clock time: 00:05:11
Memory Utilized: 7.45 GB
Memory Efficiency: 46.58% of 16.00 GB
```

### 7648646
num_workers = 40  
did not start training?
```
Every 30.0s: nvidia-smi                                gra1338: Tue Jul  4 20:21:37 2023

Tue Jul  4 20:21:37 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   47C    P0    43W / 300W |      0MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|  No running processes found                                                 |
+-----------------------------------------------------------------------------+
```
```
Job ID: 7648646
Cluster: graham
User/Group: hpcfung/hpcfung
State: TIMEOUT (exit code 0)
Nodes: 1
Cores per node: 4
CPU Utilized: 00:05:05
CPU Efficiency: 25.17% of 00:20:12 core-walltime
Job Wall-clock time: 00:05:03
Memory Utilized: 5.46 GB
Memory Efficiency: 34.11% of 16.00 GB
```
### 7648476
same (print cpu count)  
15% epoch 0
```
Every 30.0s: nvidia-smi                                gra1338: Tue Jul  4 20:13:34 2023

Tue Jul  4 20:13:34 2023
+-----------------------------------------------------------------------------+
| NVIDIA-SMI 525.105.17   Driver Version: 525.105.17   CUDA Version: 12.0     |
|-------------------------------+----------------------+----------------------+
| GPU  Name        Persistence-M| Bus-Id        Disp.A | Volatile Uncorr. ECC |
| Fan  Temp  Perf  Pwr:Usage/Cap|         Memory-Usage | GPU-Util  Compute M. |
|                               |                      |               MIG M. |
|===============================+======================+======================|
|   0  Tesla V100-SXM2...  Off  | 00000000:8A:00.0 Off |                    0 |
| N/A   50C    P0    71W / 300W |   5167MiB / 32768MiB |      0%      Default |
|                               |                      |                  N/A |
+-------------------------------+----------------------+----------------------+

+-----------------------------------------------------------------------------+
| Processes:                                                                  |
|  GPU   GI   CI        PID   Type   Process name                  GPU Memory |
|        ID   ID                                                   Usage      |
|=============================================================================|
|    0   N/A  N/A      4002      C   /opt/conda/bin/python            5164MiB |
+-----------------------------------------------------------------------------+
```

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
