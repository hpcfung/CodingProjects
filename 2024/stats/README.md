
## 2
https://media.discordapp.net/attachments/1259678646440820827/1274381732094672976/image.png?ex=66c94c39&is=66c7fab9&hm=239de95b7bddc84f7368f78dc61c28ffb7ab2c2aca283443f305fc253202989b&=&format=webp&quality=lossless&width=819&height=545
```
from math import comb
from random import random

p = 0.65
n = 8

N = 1000

q = 1 - p
# for k in range(n+1):
#     prob = comb(n, k) * (p ** k) * (q ** (n-k))
#     print(f"{k}\t{comb(n, k)}\t{prob}")
_sum = 0
for k in range(N):
    _sum += sum(random() < p for i in range(n))
print(f"avg X = {_sum/N}")
```
