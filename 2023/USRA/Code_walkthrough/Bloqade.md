
## QMC script

### Documentation
For each batch generates `raw_observables.csv` and `samples.bin`  

#### `raw_observables.csv`
batch 0: equilibration  
batch,n_sso,n_ops (number of operators sampled?)

#### `samples.bin`
`.bin` is binary

1s and 0s  
shape: `(num_spins, num_measurements)`

### L1
In additional to "main", 3 functions:
```
function init_mc_cli(parsed_args)
function continue_simulation(path, parsed_args)
function thermalstate(parsed_args)
```

#### Runtime
the "main" here (the stuff after the `########` divider around line 212) is just argparse, then all the computation is in one-line:  
`thermalstate(parsed_args["thermal"])` (~line 144)(goes from main to functions)  

##### `function thermalstate(parsed_args)`
Calls `init_mc_cli(parsed_args)` in the first line

##### function init_mc_cli(parsed_args)
If no restart flag, calls `continue_simulation(path, parsed_args)`

### L2
##### `function thermalstate(parsed_args)`
two nested loops, over batches, and over Monte Carlo steps  
`batches`: param passed in argparse (or from `continue_simulation`? actually no, that `batches` is not passed/is an internal var?)


if no restart flag but no previous path  
return nothing  
res === nothing  
so still generates anyway

how much precision from path?  
no: enter param through cmd  
construct/search path from param  
param not constructed from path!

`measurements` saved as `samples.bin`

### mapping
| QMC script      | Bloqade tutorial | Remarks |
| ----------- | ----------- | ----------- |
| `qmc_state`      | `ts`       | instance of `BinaryThermalState` object |
| `H`   | `h_qmc`        | `h = rydberg_h` then `h_qmc = rydberg_qmc(h)`|

### L4
unlike python: `ArgParse` is not in the standard library  
https://github.com/carlobaldassi/ArgParse.jl
which links to official docs https://carlobaldassi.github.io/ArgParse.jl/stable/

`thermal` is a flag? (compare `action = :store_true`)  
it doesn't take any argument?  
actually, this is `action = :command`
https://carlobaldassi.github.io/ArgParse.jl/stable/arg_table/#Commands

Commands are a special kind of arguments which introduce sub-parsing sessions as soon as they are encountered by parse_args (and are therefore mutually exclusive).


```
julia rydberg_edited.jl --help
```

```
julia rydberg_edited.jl thermal --help
```
give help for sub-commands (see below "commands have their own help screens")

cannot run `ArgParse` in REPL? need to specify Julia version each time?

`===` operator  
https://stackoverflow.com/questions/56852880/comparing-julia-variable-to-nothing-using-or  
https://stackoverflow.com/questions/38601141/what-is-the-difference-between-and-comparison-operators-in-julia

ternary operator https://docs.julialang.org/en/v1/manual/control-flow/#:~:text=The%20so%2Dcalled%20%22-,ternary%20operator,-%22%2C%20%3F%3A%2C%20is

"When a bare identifier or dot expression occurs after a semicolon, the keyword argument name is implied by the identifier or field name. For example `plot(x, y; width) is equivalent to plot(x, y; width=width)`"
https://docs.julialang.org/en/v1/manual/functions/

https://docs.julialang.org/en/v1/manual/strings/#string-interpolation

`rm(old_qmc_state)` deletes old `state.jld2` file  
https://docs.julialang.org/en/v1/base/file/#Base.Filesystem.rm

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
