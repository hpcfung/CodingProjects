Convention in https://arxiv.org/abs/2107.00766
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

Convention in https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/ (assumiing $\phi=0$)  
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

Inputs of original QMC script
```
Ω
δ
R_b
beta
L
```
No $a$? In `help`, `Rydberg blockade radius (in units of the lattice spacing).`
