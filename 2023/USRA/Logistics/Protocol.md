Julia: add to path

## Graham

`ssh username@graham.computecanada.ca`

`module spider julia` found `julia/1.8.5`  
`module spider julia/1.8.5`
`You will need to load`... `StdEnv/2020`  
`module load StdEnv/2020 julia/1.8.5` (although it looks like `StdEnv/2020` is sticky: it is always loaded)

Exercise: write bash script using nano
Exercise: wrie `.jl` using nano


`julia script-name.jl`

file transfer: globus  
from/to: `computecanada#graham-globus`

VS code, VS Julia extension

VS code: remote development extension (used config file in user not C drive)
https://code.visualstudio.com/docs/remote/remote-overview  
(includes 4 extensions)  

follow this
https://code.visualstudio.com/docs/remote/ssh#_connect-to-a-remote-host  
fn+ F1 on laptop not F1
add SSH host

https://saket404.github.io/ssh/ssh-using-vscode/

git the git development community? not google Git for Windows?  
but are they the same?

https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository

steps to pull from repo after cloning it
```
git remote -v
git remote show origin
git pull origin
```

Connect in VS remote:
F1 > connect

setup
```
module load python/3.9
virtualenv --no-download PYTORCH_3_9_ENV
source PYTORCH_TEST_ENV/bin/activate
module load scipy-stack
pip install --no-index --upgrade pip
pip install --no-index torch 
deactivate
```

reactivate
(cd to pytorch_test in scratch first)
```
module load python/3.9 scipy-stack
source PYTORCH_3_9_ENV/bin/activate
python minimal_pytorch_template.py
```

git clone, https, username, 
https://docs.github.com/en/get-started/getting-started-with-git/about-remote-repositories#cloning-with-https-urls
password = personal access token

```
python -m venv local_test
local_test\Scripts\activate.bat
python RydbergGPT\setup.py install
```

Classic token
permission: tick all

## RydbergGPT
(local)(once in RydbergGPT cd) (-e: dev mode)  
after set up local virt env  
`pip install -e .`

### Container
on cluster no need venv, use container file instead
File > Terminal > New Terminal
cd to `RydbergGPT/container`
`apptainer build RydbergGPT_container.sif pytorch_recipe.def` (no need to call Singularity; Singularity now called apptainer) 
`.sif` file: name of container
`.def`: from which the image is built
in general: `apptainer build my_container.sif my_recipe.def`
put `data` folder under `RydbergGPT` (after unzippinng)(data should contain 4 sub folders) 

on cluster also ran `pip install -e .` (with some commented out)

Please select a module to run apptainer
chose newest: `apptainer/1.1.6 StdEnv/2020`

test run: use `train.py`  
results saved; run `tensorboard.sh`
```
# import tensorflow, tensorboard
# not in container! (design: container: for pytorch only)
# saved in logdir (where u want)
# generate link, press link, local host
```

test run
```
module purge # if purged, apptainer command not found?
# cd to RydbergGPT dir first
apptainer exec container/RydbergGPT_container.sif python scratch/gpt_test/RydbergGPT/train.py --config_name=gpt2
apptainer exec container/RydbergGPT_container.sif python scratch/hello_world.py --config_name=gpt2
apptainer exec gpt_test/RydbergGPT/container/RydbergGPT_container.sif python gpt_test/RydbergGPT/train.py --config_name=gpt2
```
chose newest: `apptainer/1.1.6 StdEnv/2020`

does not work: `apptainer exec container/RydbergGPT_container.sif python ~/RydbergGPT/train.py --config_name=gpt2`
`apptainer exec scratch/gpt_test/RydbergGPT/container/RydbergGPT_container.sif python scratch/gpt_test/RydbergGPT/train.py --config_name=gpt2`


apptainer exec container/RydbergGPT_container.sif ls /scratch
apptainer exec container/RydbergGPT_container.sif ls scratch
apptainer exec container/RydbergGPT_container.sif ls

apptainer exec container/RydbergGPT_container.sif ls scratch/gpt_test

comment out 
```
    # torch>=2.0.0
    # torchvision
    # torchaudio
    # torch_geometric
    # pennylane>=0.29
    # numpy>=1.23
    # tensorboard>=2.12
    # matplotlib
    # tqdm
    # black
    # pandas
    # joblib
    # seaborn
    # imageio
    # pytorch-lightning
    # # tensorboard-plugin-profile
    # torch-tb-profiler
    # torchsummary
    # h5py
    # tables
    # pytest
    # deepspeed
    # torch_geometric
 ```
(in container?)
 
module load python/3.9
pip install -e .
remove .egg (but it comes back?)

copy ryberggpt outside of src

change `container/pytorch_recipe.def` `pytorch/pytorch:latest` to `pytorch/pytorch:2.0.0-cuda11.7-cudnn8-runtime`  
from https://hub.docker.com/layers/pytorch/pytorch/2.0.0-cuda11.7-cudnn8-runtime/images/sha256-fabb5a665a05b8ee0ac76f0d943acc40039e13536e11a44d3dc47625a266e759?context=explore

used `module load python/3.10` for tensorboard venv
pip install --no-index tensorflow
