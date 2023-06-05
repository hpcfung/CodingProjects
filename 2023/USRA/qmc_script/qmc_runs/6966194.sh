#!/bin/bash
#SBATCH --time=01:20:00
#SBATCH --job-name=qmc_res_prod_test
#SBATCH --mem=8G
#SBATCH --output=qmc_res_prod_test-%J.out
#SBATCH --account=def-rgmelko

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod_4.sh
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta -0.364386792453 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '1'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta -0.128537735849 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '2'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 0.932783018868 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '3'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 1.05070754717 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '4'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 1.16863207547 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '5'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 1.28655660377 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '6'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 1.52240566038 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '7'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 1.75825471698 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '8'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 2.9375 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '9'
julia rydberg_bloqade_ver.jl thermal 5 /home/hpcfung/qmc_test --delta 3.1733490566 --radius 1.3 --beta 0.5 --measurements 100000 --batches 10
echo '10'

echo 'qmc program completed'


# Omega = 1.0 (default)
# delta = table value/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)
