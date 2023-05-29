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

# 5
The default value of `C` in Bloqade is `rydberg_h(atoms; [C=2π * 862690 * MHz*µm^6], Ω[, ϕ, Δ])` but here `C = 61.6215711289 # MHz * µm^6`? Why does the scale differ by this much?

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
See https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/ (assuming $\phi=0$)

```math
\begin{align*}
\frac{\hat{\mathcal{H}}}{\hbar}&=\sum_j\frac{\Omega_j}{2}\hat{\sigma}_{j}^x-\sum_j\Delta_j\hat{n}_j+\sum_{j\lt k}V_{jk}\hat{n}_j\hat{n}_k\\
V_{jk}&=\frac{C_6}{|\mathbf{x}_j-\mathbf{x}_k|^6}
\end{align*}
```
These parameters enter the code through `BloqadeExpr.rydberg_h`  
https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#BloqadeExpr.rydberg_h
```
rydberg_h(atoms; [C=2π * 862690 * MHz*µm^6], Ω[, ϕ, Δ])
```
`C`: default unit is `MHz*µm^6`  
`Ω`: default unit is `MHz`  
`Δ`: default unit is `MHz`

Is `Ω[, ϕ, Δ]` a typo?

Comparing to the above, we see that $C_6=V_0$ so 
```math
\begin{align*}
C_6&=\Omega R_{b}^6
\end{align*}
```

Lattice spacing is given by  
```
atoms = generate_sites(SquareLattice(), L, L, scale = 1)
```
scale defines the unit distance in the unit μm of the lattice  
https://queracomputing.github.io/Bloqade.jl/dev/lattices/#BloqadeLattices.generate_sites:~:text=scale%20%3D%204.5)-,where,-scale%20defines%20the

In my code, I basically used 
```
Rb = 1.05 # a = 1, R_b/a = 1.15 
Ω = 26.6407057024 # MHz, 2*pi*4.24 MHz
C = 61.6215711289 # MHz * µm^6, Omega * (R_b)^6, angular freq * length^6
h = rydberg_h(atoms; C = Ω*(R_b^6), Δ = -1.545, Ω = 26.6407057024)
```

