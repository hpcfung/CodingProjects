#!/bin/bash
#SBATCH --time=01:00:00
#SBATCH --job-name=qmc_res_prod_test
#SBATCH --mem=8G
#SBATCH --output=qmc_res_prod_test-%J.out
#SBATCH --account=rrg-rgmelko-ab

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod_time2.sh
julia rydberg_bloqade_ver.jl thermal 6 /home/hpcfung/qmc_test --delta -0.364386792453 --radius 1.05 --beta 64 --measurements 100000 --batches 10

echo 'qmc program completed'


# Omega = 1.0 (default)
# delta = table value/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)
