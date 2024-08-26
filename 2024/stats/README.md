
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

## 3
https://media.discordapp.net/attachments/1259678646440820827/1276004270235451524/image.png?ex=66c9ed55&is=66c89bd5&hm=4c9f380acea0c798eba8b4ab417c9297c80b52eb390b881828257b78a95e2cf8&=&format=webp&quality=lossless&width=428&height=545
```
from math import comb

N = 2+3+4+5
n = 5
r = 3

print('X')
for x in range(r+1):
    hg = comb(r, x) * comb(N-r,n-x)/comb(N,n)
    print(x, hg)
    
p = r / N
print()
print('Y')
for x in range(n+1):
    print(x, comb(n, x)*(p**x)*((1-p)**(n-x)))
```

## 4
edit
```
from math import comb, sqrt
from random import random, sample
import itertools

def value(seq):
    if 2 in seq:
        return 10
    r,b,y = seq
    return 20*r+10*b+5*y

N = 10**2 # 5
# colors = {'red':0, 'black':1, 'yellow':2}
colors = ['red', 'black', 'yellow']
history = {(x,y,z):0 for x in range(3) for y in range(3) for z in range(3) if x+y+z==2}

value_sum = 0
for k in range(N):
    balls = sample(range(3), counts=[2, 3, 6], k=2)
    seq = [0,0,0]
    for ball in balls:
        seq[ball] += 1
    # print(seq)
    seq = tuple(seq)
    history[seq] += 1
    value_sum += value(seq)
print(history)
for seq in history.keys():
    in_words = list(itertools.chain.from_iterable([colors[x]]*seq[x] for x in range(3)))
    print(in_words)
print(value_sum/N)
```

## 7
https://media.discordapp.net/attachments/1259678646440820827/1276313487257243688/Screenshot_20240822-185351.png?ex=66c91310&is=66c7c190&hm=247de183ca98cb90bd50db8bc383d3ad13f5a4fbf8d1647951c08748de089b0e&=&format=webp&quality=lossless&width=257&height=545
