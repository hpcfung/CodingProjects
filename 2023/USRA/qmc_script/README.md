Generating QMC runs on Graham.

1. QMC through `rydberg_bloqade_ver.jl` and BloqadeQMC.

See `qmc_runs` dir for sample scripts (eg `7007771.sh` for `L = 5`).

2. Run `checking.py` to check all Slurm outputs, check if all jobs completed without issue (eg ran out of time/memory)

3. Copy from `scratch` to `projects` for backup.

Recursive copy
```
cp -R /home/hpcfung/scratch/qmc_data/L=11 /home/hpcfung/projects/def-rgmelko/hpcfung/L=11
```
large L take a long time; use globus
