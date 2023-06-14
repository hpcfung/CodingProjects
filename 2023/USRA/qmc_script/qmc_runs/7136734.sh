#!/bin/bash
#SBATCH --time=48:00:00
#SBATCH --job-name=L20_re_time_test
#SBATCH --mem=3G
#SBATCH --output=L20_re_time_test-%J.out
#SBATCH --account=rrg-rgmelko-ab

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod_time20.sh
julia rydberg_bloqade_ver.jl thermal 20 /home/hpcfung/qmc_test --delta -0.364386792453 --radius 1.3 --beta 64 --measurements 100000 --batches 10

echo 'qmc program L = 20 completed'


# Omega = 1.0 (default)
# delta = table value/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)
