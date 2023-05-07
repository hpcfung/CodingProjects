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

VS code: remote development extension (used config file in user)
https://saket404.github.io/ssh/ssh-using-vscode/

git the git development community? not google Git for Windows?  
but are they the same?

https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository

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



