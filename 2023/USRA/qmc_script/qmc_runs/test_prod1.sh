#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --job-name=qmc_trial_prod_test
#SBATCH --mem=8G
#SBATCH --output=qmc_trial_prod_test-%J.out
#SBATCH --account=def-rgmelko

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod.sh
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta -0.364386792453 --radius 1.05 --beta 0.5 --equilibration 100_000 --measurements 1_000_000 --rand-slice --restart

echo 'qmc program completed'

# L = 5
# Omega = 1.0 (default)
# delta = -0.364386792453 = -1.545/4.24
# seed = 1234 (default)
# batches = 100 (default)

# 6894245
# 31 May 3.15 pm
