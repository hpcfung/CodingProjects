using BloqadeQMC
using Random
using Plots

using Bloqade
using Yao: mat, ArrayReg
using LinearAlgebra
using Measurements
using Measurements: value, uncertainty
using Statistics


# 2D
nx = ny = 10;
nsites = nx*ny;
atoms = generate_sites(SquareLattice(), nx, ny, scale = 6.51);


Ω = 2π * 4
Δ = 2π * 10
h = rydberg_h(atoms; Δ, Ω)

h_qmc = rydberg_qmc(h);



EQ_MCS = 100;
MCS = 100_000;

M = 50;
ts = BinaryThermalState(h_qmc, M);

d = Diagnostics();

β = 0.5;

rng = MersenneTwister(3214);

[mc_step_beta!(rng, ts, h_qmc,β, d, eq=true) for i in 1:EQ_MCS] # equilibration phase

densities_QMC = zeros(nsites)
occs = zeros(MCS, nsites)

for i in 1:MCS # Monte Carlo Steps
    mc_step_beta!(rng, ts, h_qmc,β, d, eq=false) do lsize, ts, h_qmc
        SSE_slice = sample(h_qmc,ts, 1)
        occs[i, :] = ifelse.(SSE_slice .== true, 1.0, 0.0)
    end
end

for jj in 1:nsites
    densities_QMC[jj] = mean(occs[:,jj])
end

# 2D plot
mat_densities_QMC = reshape(densities_QMC,(nx,ny))
heatmap(mat_densities_QMC, c=cgrad([:blue, :green, :yellow]))
# somehow the color bar on 
# https://queracomputing.github.io/Bloqade.jl/dev/tutorials/7.QMC/main/
# the green is duller

