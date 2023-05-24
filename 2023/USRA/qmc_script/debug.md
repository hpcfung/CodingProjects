

### Config
```
julia rydberg_bloqade_ver.jl thermal 4 /home/hpcfung/qmc_test --rand-slice --restart
```

### Error
#### On login node
```
Running Rydberg((4,4), R_b=1.2, Ω=1.0, δ=1.0)
WARNING: both BloqadeODE and Yao export "iscached"; uses of it in module Bloqade must be qualified
ERROR: LoadError: OutOfMemoryError()
Stacktrace:
 [1] _growend!
   @ ./array.jl:1011 [inlined]
 [2] append!(a::Vector{NTuple{5, Int64}}, items::Vector{NTuple{5, Int64}})
   @ Base ./array.jl:1108
 [3] resize_op_list!(qmc_state::BloqadeQMC.QMCState{BloqadeQMC.Thermal, Bool, 5, Vector{Bool}, Nothing}, H::Rydberg{BloqadeQMC.ImprovedOperatorSampler{5, Float64, ProbabilityAlias{Float64}}, UpperTriangular{Float64, Matrix{Float64}}, Vector{Float64}, Vector{Float64}, Vector{Tuple{Float64, Float64}}}, new_size::Int64)
   @ BloqadeQMC ~/.julia/packages/BloqadeQMC/F4DVZ/src/ising/mixedstate.jl:21
 [4] full_diagonal_update_beta!(rng::RandomNumbers.Xorshifts.Xoroshiro128Plus, qmc_state::BloqadeQMC.QMCState{BloqadeQMC.Thermal, Bool, 5, Vector{Bool}, Nothing}, H::Rydberg{BloqadeQMC.ImprovedOperatorSampler{5, Float64, ProbabilityAlias{Float64}}, UpperTriangular{Float64, Matrix{Float64}}, Vector{Float64}, Vector{Float64}, Vector{Tuple{Float64, Float64}}}, beta::Float64; eq::Bool)
   @ BloqadeQMC ~/.julia/packages/BloqadeQMC/F4DVZ/src/ising/mixedstate.jl:70
 [5] mc_step_beta!(f::var"#7#8"{Bool, RandomNumbers.Xorshifts.Xoroshiro128Plus, Int64, Int64}, rng::RandomNumbers.Xorshifts.Xoroshiro128Plus, qmc_state::BloqadeQMC.QMCState{BloqadeQMC.Thermal, Bool, 5, Vector{Bool}, Nothing}, H::Rydberg{BloqadeQMC.ImprovedOperatorSampler{5, Float64, ProbabilityAlias{Float64}}, UpperTriangular{Float64, Matrix{Float64}}, Vector{Float64}, Vector{Float64}, Vector{Tuple{Float64, Float64}}}, beta::Float64, d::Diagnostics{NoStats, NoTransitionMatrix}; eq::Bool, kw::Base.Pairs{Symbol, Float64, Tuple{Symbol}, NamedTuple{(:p,), Tuple{Float64}}})
   @ BloqadeQMC ~/.julia/packages/BloqadeQMC/F4DVZ/src/ising/mixedstate.jl:5
 [6] thermalstate(parsed_args::Dict{String, Any})
   @ Main ~/qmc_test/rydberg_bloqade_ver.jl:166
 [7] top-level scope
   @ ./timing.jl:262
in expression starting at /home/hpcfung/qmc_test/rydberg_bloqade_ver.jl:310
```
#### Slurm
Only one row generated in csv file
##### 64 GB
```
WARNING: both BloqadeODE and Yao export "iscached"; uses of it in module Bloqade must be qualified
ERROR: LoadError: InexactError: Int64(9.753985038138009e-9)
Stacktrace:
 [1] Int64
   @ ./float.jl:788 [inlined]
 [2] convert
   @ ./number.jl:7 [inlined]
 [3] setindex!(A::Vector{Int64}, x::Float64, i1::Int64)
   @ Base ./array.jl:966
 [4] insert_single_entry!(df::DataFrame, v::Float64, row_ind::Int64, col_ind::Symbol)
   @ DataFrames ~/.julia/packages/DataFrames/LteEl/src/dataframe/dataframe.jl:659
 [5] setindex!(df::DataFrame, v::Float64, row_ind::Int64, col_ind::Symbol)
   @ DataFrames ~/.julia/packages/DataFrames/LteEl/src/dataframe/dataframe.jl:688
 [6] (::var"#7#8"{Bool, RandomNumbers.Xorshifts.Xoroshiro128Plus, Int64, Int64})(#unused#::Int64, qmc_state::BloqadeQMC.QMCState{BloqadeQMC.Thermal, Bool, 5, Vector{Bool}, Nothing}, H::Rydberg{BloqadeQMC.ImprovedOperatorSampler{5, Float64, ProbabilityAlias{Float64}}, UpperTriangular{Float64, Matrix{Float64}}, Vector{Float64}, Vector{Float64}, Vector{Tuple{Float64, Float64}}})
   @ Main ~/qmc_test/rydberg_bloqade_ver.jl:171
 [7] mc_step_beta!(f::var"#7#8"{Bool, RandomNumbers.Xorshifts.Xoroshiro128Plus, Int64, Int64}, rng::RandomNumbers.Xorshifts.Xoroshiro128Plus, qmc_state::BloqadeQMC.QMCState{BloqadeQMC.Thermal, Bool, 5, Vector{Bool}, Nothing}, H::Rydberg{BloqadeQMC.ImprovedOperatorSampler{5, Float64, ProbabilityAlias{Float64}}, UpperTriangular{Float64, Matrix{Float64}}, Vector{Float64}, Vector{Float64}, Vector{Tuple{Float64, Float64}}}, beta::Float64, d::Diagnostics{NoStats, NoTransitionMatrix}; eq::Bool, kw::Base.Pairs{Symbol, Float64, Tuple{Symbol}, NamedTuple{(:p,), Tuple{Float64}}})
   @ BloqadeQMC ~/.julia/packages/BloqadeQMC/F4DVZ/src/ising/mixedstate.jl:7
 [8] thermalstate(parsed_args::Dict{String, Any})
   @ Main ~/qmc_test/rydberg_bloqade_ver.jl:166
 [9] top-level scope
   @ ./timing.jl:262
in expression starting at /home/hpcfung/qmc_test/rydberg_bloqade_ver.jl:310
Running Rydberg((4,4), R_b=1.2, Ω=1.0, δ=1.0)
```
###### seff
```
seff 6767275
Job ID: 6767275
Cluster: graham
User/Group: hpcfung/hpcfung
State: COMPLETED (exit code 0)
Nodes: 1
Cores per node: 2
CPU Utilized: 00:07:18
CPU Efficiency: 49.21% of 00:14:50 core-walltime
Job Wall-clock time: 00:07:25
Memory Utilized: 37.39 GB
Memory Efficiency: 58.42% of 64.00 GB
```

##### 32 GB
```
WARNING: both BloqadeODE and Yao export "iscached"; uses of it in module Bloqade must be qualified
/var/spool/slurmd/job6767023/slurm_script: line 15: 157728 Killed                  julia rydberg_bloqade_ver.jl thermal 4 /home/hpcfung/qmc_test --rand-slice --restart
slurmstepd: error: Detected 1 oom-kill event(s) in StepId=6767023.batch. Some of your processes may have been killed by the cgroup out-of-memory handler.
```
###### seff
```
seff 6767023
Job ID: 6767023
Cluster: graham
User/Group: hpcfung/hpcfung
State: OUT_OF_MEMORY (exit code 0)
Nodes: 1
Cores per node: 8
CPU Utilized: 00:03:15
CPU Efficiency: 11.89% of 00:27:20 core-walltime
Job Wall-clock time: 00:03:25
Memory Utilized: 31.34 GB
Memory Efficiency: 97.95% of 32.00 GB
```
