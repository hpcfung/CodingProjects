#!/bin/env bash

module purge

module load StdEnv/2020 apptainer/1.1.6

# Declare the Python script name as a variable
python_script_name="train.py"
# python_script_name="examples/3_train_encoder_decoder.py"

# cd to RydbergGPT dir
apptainer exec container/RydbergGPT_container.sif python $HOME/scratch/gpt_test/RydbergGPT/train.py --config_name=gpt2

