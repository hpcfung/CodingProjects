Consider this configuration listed on the README on https://github.com/PIQuIL/RydbergGPT/tree/main
```
L = 5 # size of square lattice
delta = -1.545
Rb = 1.05
beta = 0.5
```

I am not sure if I am implementing this values correctly. These values are taken from/motivated by https://arxiv.org/abs/2012.12281.

# 1
Should we use `Omega = 4.24` (it was mentioned last meeting)(this would mean $\Omega=2\pi\times4.24\mbox{ MHz}$?) or $\Omega=2\pi\times4.3\mbox{ MHz}$ (from the paper)?

# 2
## (a)
The `∆` value used in the paper is $\Delta\in[-16\mbox{ MHz},14\mbox{ MHz}]$. Is this `∆` (-16 to 14 MHz) the frequency or angular frequency? ie does it need an additional factor of $2\pi$?

## (b)
I think it was mentioned last meeting that `delta` needs to be divided by `Omega = 4.24`? But if we are using $\Delta = -1.545\mbox{ MHz}$ (up to $13.455\mbox{ MHz}$), then it is already in the range $[-16\mbox{ MHz},14\mbox{ MHz}]$ and of the right dimensions. Is division by $\Omega$ still necessary?

# 3
Are we using the convention where length is nondimensionalized by the lattice spacing $a$? However the Bloqade code uses units of `µm` (eg interaction matrix). Is nondimensionalization equivalent to setting `a = 1 µm`? Alternatively I can use `a = 6.7 µm` from the paper and adjust the interaction matrix accordingly.

# 4
Do we simply use `beta = [0.5, 1, 2, 4, 8, 16, 32, 48, 64]`? ie no nondimensionalization is necessary? (I cannot find the corresponding documentation for Bloqade.)


# Background
## Convention in arXiv:2012.12281 (quantum simulator paper)
See https://arxiv.org/abs/2012.12281. The Hamiltonian is in the form
```math
\begin{align*}
\frac{\hat{H}}{\hbar}&=\frac{\Omega}{2}\sum_{i}\hat{\sigma}_{i}^x-\Delta\sum_{i}\hat{n}_i+\sum_{i\lt j}V_{ij}\hat{n}_i\hat{n}_j\\
V_{ij}&=\frac{V_0}{\left|\mathbf{x}_i-\mathbf{x}_j\right|^6}\\
R_b&\equiv\left(\frac{V_0}{\Omega}\right)^{1/6}
\end{align*}
```
$\hbar$ implies that the parameters $\Omega$ and $\Delta$ are angular frequencies.
```math
\begin{align*}
\frac{R_b}{a}&=1.15\\
\Omega&=2\pi\times4.3\mbox{ MHz}\\
\Delta&\in[-16\mbox{ MHz},14\mbox{ MHz}]
\end{align*}
```


## Convention in Bloqade
See https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/

```math
\begin{align*}
\frac{\hat{\mathcal{H}}}{\hbar}&=\sum_j\frac{\Omega_j}{2}\hat{\sigma}_{j}^x-\sum_j\Delta_j\hat{n}_j+\sum_{j\lt k}V_{jk}\hat{n}_j\hat{n}_k\\
V_{jk}&=\frac{C_6}{|\mathbf{x}_j-\mathbf{x}_k|^6}
\end{align*}
```

 (assumiing $\phi=0$)  
https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#BloqadeExpr.rydberg_h

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

