`csv_conversion.jl`: change `L` in `base_path`, `num_spins` (to `L^2`)  
`julia csv_conversion.jl`: choose `1`  
(this takes too long, use bash script)

copy `csv_con.sh`  
change `job-name`, `output`, `sbatch XX.sh`, `julia XX.jl`, `program XX.jl completed`

copy `Reformat_BloqadeQMC_Data.py`, rename, put in `reformat` dir  
change `qmc_path`, `L =`
copy script  
change `job-name`, `output`, `python LX.py`, `sbatch XX.sh`

