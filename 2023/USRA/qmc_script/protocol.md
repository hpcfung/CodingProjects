desmos divide (copy all digits) eg -0.364386792453 = -1.545/4.24

| Syntax      | Description |
| ----------- | ----------- |
| -1.545      | -0.364386792453       |
| -0.545   | -0.128537735849        |
| 3.955   | 0.932783018868        |
| 4.455   | 1.05070754717        |
| 4.955   | 1.16863207547        |
| 5.455   | 1.28655660377        |
| 6.455   | 1.52240566038        |
| 7.455   | 1.75825471698        |
| 12.455   | 2.9375        |
| 13.455   | 3.1733490566        |

run script  
upload script  
update progress.md to 0  
google sheets  
update progress.md batch  
move out file to out dir

each time update: download all files, upload to google drive in one go

L = 5, beta = 0.5, Rb = 1.05
1 GB, 2-5 mins, about the same for different delta
beta = 16: 10 mins  
beta = 64: 20 mins

~1 GB for all

larger Rb longer time  


| beta = 64      | Rb = 1.05 | Rb = 1.3 |
| ----------- | ----------- | ----------- |
| L = 5      | 20 mins       | (x10, 1.56 GB) |
| L = 6      | 24 mins       | 1 hr 13 mins |
| L = 11 | 1 h 41 mins (1.24 GB) | 6 h 50 mins (1.26 GB) |
| L = 12 | 2 h 20 mins (1.22 GB) | 11 h 29 mins (pred: 11 h)(1.26 GB) |
| L = 15 | >3 h (1.26 GB) | 15 h 8 mins (pred: 16 h)(1.31 GB)|
| L = 16 | | 17 h 46 mins (pred: 28h)(1.52 GB) |
| L = 19 | | 33 h 22 mins (pred: 37h)(1.34 GB) |
| L = 20   | >6 h (1.38 GB) | 27 h 12 mins(pred: 31.5 h)(1.38 GB) |

```
fluctuations for large `L`

0-26 # 9*3=27
3-26

beta start from 3//3 + 1 = 2 (2nd beta)
```
