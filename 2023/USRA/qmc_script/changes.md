Convention in https://arxiv.org/abs/2107.00766
```math
\begin{align*}
\hat{H}&=\frac{\Omega}{2}\sum_{i=1}^N\hat{\sigma}_{i}^x-\delta\sum_{i=1}^N\hat{n}_i+\sum_{i\lt j}V_{ij}\hat{n}_i\hat{n}_j\\
V_{ij}&=\Omega\left(\frac{R_b}{r_{ij}}\right)^6\\
\mathbf{r}_{ij}&=\frac{\mathbf{x}_i-\mathbf{x}_j}{a}
\end{align*}
```
distance $r_{ij}$  
lattice spacing $a$  
blockade radius $R_b$

Convention in https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/ (assumiing $\phi=0$)  
https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#BloqadeExpr.rydberg_h
```math
\begin{align*}
\frac{\hat{\mathcal{H}}}{\hbar}&=\sum_j\frac{\Omega_j}{2}\hat{\sigma}_{j}^x-\sum_j\Delta_j\hat{n}_j+\sum_{j\lt k}V_{jk}\hat{n}_j\hat{n}_k\\
V_{jk}&=\frac{C_6}{|\mathbf{x}_j-\mathbf{x}_k|^6}
\end{align*}
```
angular frequency
