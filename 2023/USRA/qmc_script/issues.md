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

# Background
## Convention in https://arxiv.org/abs/2012.12281
```math
\begin{align*}
\frac{\hat{H}}{\hbar}&=\frac{\Omega}{2}\sum_{i}\hat{\sigma}_{i}^x-\Delta\sum_{i}\hat{n}_i+\sum_{i\lt j}V_{ij}\hat{n}_i\hat{n}_j\\
V_{ij}&=\frac{V_0}{\left|\mathbf{x}_i-\mathbf{x}_j\right|^6}\\
R_b&\equiv\left(\frac{V_0}{\Omega}\right)^{1/6}
\end{align*}
```
```math
\begin{align*}
\frac{R_b}{a}&=1.15\\
\Omega&=2\pi\times4.3\mbox{ MHz}\\
\Delta&\in[-16\mbox{ MHz},14\mbox{ MHz}]
\end{align*}
```
Is `∆` (-16 to 14 MHz) angular frequency or frequency?

### Convention in https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/ (assumiing $\phi=0$)  
https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#BloqadeExpr.rydberg_h
```math
\begin{align*}
\frac{\hat{\mathcal{H}}}{\hbar}&=\sum_j\frac{\Omega_j}{2}\hat{\sigma}_{j}^x-\sum_j\Delta_j\hat{n}_j+\sum_{j\lt k}V_{jk}\hat{n}_j\hat{n}_k\\
V_{jk}&=\frac{C_6}{|\mathbf{x}_j-\mathbf{x}_k|^6}
\end{align*}
```
because $\hbar$: angular frequency (code: comes in default units, eg `MHz`)  
parameters passed to `rydberg_h`: `C`, `Ω`, `Δ`  
lattice spacing is implicit in `atoms` (atom positions)  
```math
\frac{\Omega}{\hbar}\left(R_b a\right)^6=C_6
```
`rydberg_h(atoms; [C=2π * 862690 * MHz*µm^6], Ω[, ϕ, Δ])`  
Meaning of `Ω[, ϕ, Δ]`? `Δ` divided by `Ω`?

So among `Ω, δ, R_b, beta, L`, `beta` and `L` stay the same  
`Ω` and `δ` stay the same (but different dimensions)  
`R_b` and `Ω` (and `a`) become `C`

