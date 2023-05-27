### Convention in https://arxiv.org/abs/2107.00766
```math
\begin{align*}
\hat{H}&=\frac{\Omega}{2}\sum_{i=1}^N\hat{\sigma}_{i}^x-\delta\sum_{i=1}^N\hat{n}_i+\sum_{i\lt j}V_{ij}\hat{n}_i\hat{n}_j\\
V_{ij}&=\Omega\left(\frac{R_b}{r_{ij}}\right)^6\\
\mathbf{r}_{ij}&=\frac{\mathbf{x}_i-\mathbf{x}_j}{a}
\end{align*}
```
distance $r_{ij}$  
lattice spacing $a$ (in paper: $a=1$)  
blockade radius $R_b$ (dimensionless?)  
Parameters: $\Omega,\delta,R_b,a$

### Inputs of original QMC script
```
Ω
δ
R_b
beta
L
```
No $a$? In `help`, `Rydberg blockade radius (in units of the lattice spacing).`

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

### Convention in https://arxiv.org/abs/2012.12281
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

## Test
`delta`: need to divide by `Omega = 4.24`, but why?
```
size = 4
delta = -1.545 # MHz?
R_b = 1.15 # a = 1, R_b/a = 1.15 
Ω = 26.6407057024 # MHz, 2*pi*4.24 MHz
C = 61.6215711289 # MHz * length^6, Omega * (R_b)^6, angular freq * length^6
```


assume `a = 1 µm`
where scale defines the unit distance in the unit μm of the lattice  
The default scale is 1 μm  
https://queracomputing.github.io/Bloqade.jl/dev/lattices/#BloqadeLattices.generate_sites:~:text=scale%20%3D%204.5)-,where,-scale%20defines%20the
```
R_b = 1.15 # µm, R_b/a = 1.15
C = 61.6215711289 # MHz * µm^6, Omega * (R_b)^6, angular freq * length^6
```


use convention in quantum simulator paper

why is C much smaller than the default value in `BloqadeExpr.rydberg_h`?

### To check
1. no need to change beta? (energy scale?)
2. lattice spacing: pretend `a = 1 µm`, or use actual value, then change `C`? (Should give the same thing?
