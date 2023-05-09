#!/bin/env bash
# does not work #!/bin/bash

# if purge, apptainer: command not found
module purge

module load StdEnv/2020 apptainer/1.1.6

# Declare the Python script name as a variable
python_script_name="train.py"
# python_script_name="examples/3_train_encoder_decoder.py"

# change .sif
# apptainer run --bind /host/data:/container/RydbergGPT_container.sif
apptainer run container/RydbergGPT_container.sif

# chmod +rx script/home/hpcfung/scratch/gpt_test/RydbergGPT/apptainer_test.sh
# apptainer exec container/RydbergGPT_container.sif /home/hpcfung/scratch/gpt_test/RydbergGPT/apptainer_test.sh

# echo "$PWD"
# let count=0
# for f in "$PWD"/*
# do
#     echo $(basename $f)
#     let count=count+1
# done
# echo ""
# echo "Count: $count"


# apptainer exec container/RydbergGPT_container.sif python $PWD/train.py
# apptainer exec container/RydbergGPT_container.sif python $HOME/scratch/hello_world.py
# apptainer exec container/RydbergGPT_container.sif python ~/scratch/gpt_test/RydbergGPT/train.py --config_name=gpt2
# apptainer exec container/RydbergGPT_container.sif python /home/hpcfung/scratch/gpt_test/RydbergGPT/train.py --config_name=gpt2

# apptainer exec container/RydbergGPT_container.sif python /scratch/gpt_test/RydbergGPT/${python_script_name} --config_name=gpt2
# apptainer exec scratch/gpt_test/RydbergGPT/container/RydbergGPT_container.sif python scratch/gpt_test/RydbergGPT/${python_script_name} --config_name=gpt2
# apptainer exec ~/RydbergGPT/container/RydbergGPT_container.sif python ~/RydbergGPT/${python_script_name} --config_name=gpt2