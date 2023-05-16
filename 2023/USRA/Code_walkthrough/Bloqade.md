
## 1D chain
`BloqadeLattices>t5g0l>src>lattice.jl` (VS code: right click `generate_sites`, Go to Definition)  
`AbstractLattice{D}` implemented as abstract type  
structs defined include
- `GeneralLattice` (any dim)
- `HoneycombLattice` (2D)
- `SquareLattice` (2D)
- `TriangularLattice` (2D)
- `ChainLattice` (1D)
- `LiebLattice` (2D)
- `KagomeLattice` (2D)
- `RectangularLattice` (2D)

Note usage in code: `ChainLattice()` with `()` at the end
initialize struct but this struct has no fields  
struct subtype of `AbstractLattice`

syntax `abstract type Pointy{T} end`  
`Pointy{T}` is a distinct abstract type for each type or integer value of `T`
https://docs.julialang.org/en/v1/manual/types/#Parametric-Abstract-Types

whole thing: basically this https://stackoverflow.com/a/60220581

`nsites` `repeats::Vararg{Int,D}`

The tiling repeat the `sites` of the lattice `m` times along the first dimension,
`n` times along the second dimension, and so on. 

so repeat unit cell?


`scale` is a real number that re-scales the lattice constant and atom locations.

`generate_sites` return `atoms`, 1st argument of `rydberg_h`? (internal name: `atom_positions`)

type:
```
9-element AtomList{1, Float64}:
 (0.0,)
 (5.72,)
 (11.44,)
 (17.16,)
 (22.88,)
 (28.599999999999998,)
 (34.32,)
 (40.04,)
 (45.76,)
```
`NTuple{D,T}`: a tuple type containing exactly `D` elements of type T  
(`D`-dimensional, `D` components in coordinates)  
`locations = NTuple{D,T}[]`: creates an empty array  
`AtomList(_generate_sites(...))`: instance of `AtomList` (`struct`)

`rydberg_h`: Create a rydberg hamiltonian  
type: `RydbergHamiltonian`  
to use it, argument of the function `rydberg_qmc`

https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#Hamiltonian-Expressions
https://queracomputing.github.io/Bloqade.jl/dev/hamiltonians/#BloqadeExpr.rydberg_h
`BloqadeExpr/src/types.jl` or just source button in link above (lower right corner of whole box)

`rydberg_qmc` is an instance of the struct `Rydberg`  
includes atom positions  
https://queracomputing.github.io/Bloqade.jl/dev/tutorials/7.QMC/main/#:~:text=must%20be%20qualified-,The%20object,-h_qmc%20still%20contains

The object h_qmc still contains all the previous information about the lattice geometry as well as the Hamiltonian parameters 
Ω
Ω and 
Δ
Δ. However, the object now also stores the distribution of weights from which the algorithm will sample. 
```
struct Rydberg{O,M <: UpperTriangular,UΩ <: AbstractVector{Float64}, Uδ <: AbstractVector{Float64}, A} <: AbstractRydberg{O}
    op_sampler::O   # distribution of weights sampled
    V::M          # interaction matrix
    Ω::UΩ 
    δ::Uδ
    atoms::A          # atom positions
    energy_shift::Float64
end
```
### MC
`100_000`: The underscore `_` can be used as digit separator
https://docs.julialang.org/en/v1/manual/integers-and-floating-point-numbers/#Floating-Point-Numbers-1:~:text=be%20used%20as-,digit%20separator,-%3A

`EQ_MCS = 100`: number of iterations for equilibration/during equilibration phase
`MCS = 100_000`: number of Monte Carlo steps

`M` is the cutoff

looks like the function `BinaryThermalState` is recursive and returns the last line `BinaryThermalState(z, init_op_list(cutoff, Val{K}()))::BinaryThermalState{K, typeof(z)}`?  
https://docs.julialang.org/en/v1/manual/functions/#man-functions return keyword omitted
The value returned by a function is the value of the last expression evaluated
https://docs.julialang.org/en/v1/manual/functions/#The-return-Keyword

where is the type `BinaryThermalState{K, typeof(z)}` defined?
`BinaryThermalState` return type is `BloqadeQMC.QMCState`? struct?

`d = Diagnostics();` did nothing?

```
[mc_step_beta!(rng, ts, h_qmc,β, d, eq=true) for i in 1:EQ_MCS]
```
array not saved, one liner for 100 iterations?
each `mc_step_beta!` does one MC iteration on `ts`?

size of `occs`: `(MCS, nsites)`
same MC code runs for 1D chain/2D square lattice?

`densities_QMC`: mean across all MC iterations at each lattice site