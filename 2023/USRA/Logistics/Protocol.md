
## RydbergGPT on Graham

(Quality of life: set up VS remote)

### Git clone
1. Go to home directory on Graham
2. Go to https://github.com/PIQuIL/RydbergGPT/tree/main; <> Code button, HTTPS, copy link
3. 
```
git clone https://github.com/PIQuIL/RydbergGPT.git
```
Or (probably should cd to a separate directory for that branch first)
```
git clone -b yihongdev https://github.com/PIQuIL/RydbergGPT.git
git clone -b main https://github.com/PIQuIL/RydbergGPT.git
```
This step creates the `RydbergGPT` directory in your home directory.

### Container
```
cd RydbergGPT/container
apptainer build pytorch.sif pytorch_recipe.def
```
```
Please select a module to run apptainer:
       MODULE          PARENT(S)
    1  apptainer/1.1.8 StdEnv/2020
    2  apptainer/1.1.6 StdEnv/2020
    3  apptainer/1.1.5 StdEnv/2020
    4  apptainer/1.1.3 StdEnv/2020
Make a selection (1-4, q aborts) [1]: 1 # latest version
```
(`yihongdev` branch uses `apptainer/1.1.8 StdEnv/2020`; old: `apptainer/1.1.6 StdEnv/2020`)
### Data
Put the `data` folder inside `RydbergGPT` (after unzippinng)(`dat`a should contain 4 sub folders) 

### Install `rydberggpt`
1.
```
module load python/3.10
```
2. `pip freeze` to check that rydberggpt is not already installed. 
3. If already installed (eg another branch), do
```
python -m pip uninstall rydberggpt
```
Then `pip freeze` to check again
5. Go to `setup.cfg`, comment out the pacakages below `install_requires`:
```
    torch>=2.0.0
    torchvision
    torchaudio
    torch_geometric
    pennylane>=0.29
    numpy>=1.23
    tensorboard>=2.12
    matplotlib
    tqdm
    black
    pandas
    joblib
    seaborn
    imageio
    pytorch-lightning
    # tensorboard-plugin-profile
    torch-tb-profiler
    torchsummary
    h5py
    tables
    pytest
    deepspeed
    torch_geometric
```    
6. Go to the `RydbergGPT` directory, run
```
pip install -e .
```
7. `pip freeze` to check that rydberggpt is installed. You should see
```
-e git+https://github.com/PIQuIL/RydbergGPT.git@aabb59035b7e8c4713a14131697ae0b31ff11f8c#egg=rydberggpt
```
between packages that start with `q` and `s`.

### Run on Slurm
Use this script
```
#!/bin/bash
#SBATCH --time=00:10:00
#SBATCH --job-name=gpt_test
#SBATCH --mem=16G
#SBATCH --gpus-per-node=v100:1
#SBATCH --output=gpt_test-%J.out
#SBATCH --account=def-rgmelko

module purge

module load StdEnv/2020 apptainer/1.1.6

# Declare the Python script name as a variable
python_script_name="train.py"
# python_script_name="examples/3_train_encoder_decoder.py"

# cd to RydbergGPT dir
# sbatch scripts/myTrain.sh
# source scripts/myTrain.sh
apptainer exec --nv ~/RydbergGPT/container/pytorch.sif python ~/RydbergGPT/${python_script_name} --config_name=config_small

echo 'python program completed'
```
This generates a `logs/lightning_logs` directory and a `.out` file inside the `RydbergGPT` directory.  

Changes from `train.sh` in the repo:
- added `--nv` flag for gpu access

By default, this runs for 1000 epochs?

### Tensorboard
#### Set up venv
Go to the `RydbergGPT` directory
```
module load python/3.10
virtualenv --no-download TENSORBOARD_ENV
source TENSORBOARD_ENV/bin/activate
pip install --no-index --upgrade pip
pip install --no-index tensorflow
deactivate
```
#### View tensorboard
Go to the `RydbergGPT` directory
```
module load python/3.10
source TENSORBOARD_ENV/bin/activate
tensorboard --logdir="logs"
```
To look at one version only, use
```
tensorboard --logdir="logs/lightning_logs/version_10" --port=8008
```
Use `--port=8008` flag if `port 6006` is occupied.  

`CTRL+C` then `deactivate`.

