#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --job-name=min_cpu_test
#SBATCH --mem=16G
#SBATCH --gres=gpu:v100:1
#SBATCH --cpus-per-task=4
#SBATCH --output=min_cpu_test-%J.out
#SBATCH --account=def-rgmelko

module purge

module load StdEnv/2020 apptainer/1.1.8

# Declare the Python script name as a variable
python_script_name="train.py"
# python_script_name="examples/3_train_encoder_decoder.py"

# cd RydbergGPT
# sbatch scripts/cpuTrain.sh
apptainer exec --nv --bind /home/hpcfung/scratch:/SCRATCHTAINER /home/hpcfung/RydbergGPT/container/pytorch.sif python /home/hpcfung/RydbergGPT/myTrain.py --config_name=config_small

echo 'python program completed'

# rrg-rgmelko-ab
# def-rgmelko
# nvidia-smi
