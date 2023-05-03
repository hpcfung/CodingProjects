using BloqadeQMC
using Random
using Plots

using Bloqade
using Yao: mat, ArrayReg
using LinearAlgebra
using Measurements
using Measurements: value, uncertainty
using Statistics

# 1D chain
nsites = 9
atoms = generate_sites(ChainLattice(), nsites, scale = 5.72)
# 1D chain end


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

# 1D plot
using Plots: bar


results_plot = bar(densities_QMC, label="")
xlabel!("Site number")
ylabel!("Occupation density")
results_plot




