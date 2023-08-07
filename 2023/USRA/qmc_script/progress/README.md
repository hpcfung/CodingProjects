
|     | L=5 | L=6 | L=11 | L=12 | L=15 | L=16 | L=19 | L=20 |
| ------- | ------- | ------ | ------ | ------ | ----- | ------- | ---- | ---- |
| raw from qmc, no csv   | 3.2G | 3.6G | 7.3G| 7.6G | 11G | 13G | 17G | 24G |
| with csv   |         | |  |


```
du -hs /home/hpcfung/scratch/qmc_data/L=11
```
https://unix.stackexchange.com/questions/185764/how-do-i-get-the-size-of-a-directory-on-the-command-line

copy script  
change `job-name`, `output`, `sbatch XX.sh`, `L=XX`  
(actually, just run command; L=19 less than 1 min)

L5 to 19 backed raw QMC backed up at proj; csv generated  
