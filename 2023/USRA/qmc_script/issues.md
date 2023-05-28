Consider this configuration listed on the README on https://github.com/PIQuIL/RydbergGPT/tree/main
```
L = 5 # size of square lattice
delta = -1.545
Rb = 1.05
beta = 0.5
```

I am not sure if I am implementing this values correctly. These values are taken from/motivated by https://arxiv.org/abs/2012.12281

# 1
Should we use `Omega = 4.24` (it was mentioned last meeting)(this would mean $\Omega=2\pi\times4.24\mbox{ MHz}$?) or $\Omega=2\pi\times4.3\mbox{ MHz}$ (from the paper)?

# Questions
1. no need to change beta? (energy scale?)
2. lattice spacing: pretend `a = 1 µm`, or use actual value, then change `C`? (Should give the same thing?)
3. `delta`: need to divide by `Omega = 4.24`?

