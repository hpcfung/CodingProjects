#!/bin/bash
#SBATCH --array=0-269
#SBATCH --time=57:00:00
#SBATCH --job-name=L19_prod_test
#SBATCH --mem=2G
#SBATCH --output=L19_prod_test-%J.out
#SBATCH --account=rrg-rgmelko-ab

module purge

module load julia/1.8.5 StdEnv/2020

# cd to qmc_test dir
# sbatch qmc_prod_L19.sh
echo "Starting task $SLURM_ARRAY_TASK_ID"
MACRO_ID=$((SLURM_ARRAY_TASK_ID / 10))
BETA_ID=$((MACRO_ID / 3 + 1))
RB_ID=$((MACRO_ID % 3 + 1))
DELTA_ID=$((SLURM_ARRAY_TASK_ID % 10 + 1))

RB=$(sed -n "${RB_ID}p" rb_list)
BETA=$(sed -n "${BETA_ID}p" beta_list)
DELTA=$(sed -n "${DELTA_ID}p" delta_list)
L=19
save_path="/home/hpcfung/scratch/qmc_data"

echo "BETA_ID = $BETA_ID"
echo "RB_ID = $RB_ID"
echo "DELTA_ID = $DELTA_ID"
echo "Beta $BETA"
echo "Radius $RB"
echo "Delta $DELTA"
echo "L $L"
echo "path $save_path"
echo " "

julia rydberg_bloqade_ver.jl thermal $L $save_path --delta $DELTA --radius $RB --beta $BETA --measurements 100000 --batches 10

echo "qmc program L $L beta $BETA Rb $RB delta $DELTA completed"


# Omega = 1.0 (default)
# delta = table value/4.24
# seed = 1234 (default)
# equilibration = 100000 = measurements (default)
# batches = 100 (default)
