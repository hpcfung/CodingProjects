#!/bin/env bash

module purge

module load StdEnv/2020 apptainer/1.1.6

# Declare the Python script name as a variable
python_script_name="train.py"
# python_script_name="examples/3_train_encoder_decoder.py"

# cd to RydbergGPT dir
# put this script and train.py in the scripts dir
apptainer exec --bind /home/hpcfung/scratch/gpt_test/RydbergGPT:/mnt container/RydbergGPT_container.sif python /mnt/scripts/train.py --config_name=gpt2
# success