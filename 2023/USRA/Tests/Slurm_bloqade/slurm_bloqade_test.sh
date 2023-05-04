#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --job-name=bloq_test
#SBATCH --mem=8192M
#SBATCH --output=bloq_test-%J.out
#SBATCH --account=def-rgmelko
echo 'Runs the 1D QMC Bloqade tutorial example on Slurm.'
module load StdEnv/2020 julia/1.8.5
julia nano_bloqade_test.jl
echo 'Julia program complete'
