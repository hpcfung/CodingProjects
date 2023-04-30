
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

`ChainLattice()`: why `()`?

`nsites` `repeats::Vararg{Int,D}`

The tiling repeat the `sites` of the lattice `m` times along the first dimension,
`n` times along the second dimension, and so on. 

so repeaet unit cell?


`scale` is a real number that re-scales the lattice constant and atom locations.

`generate_sites` return atoms, 1st argument of `rydberg_h`? (internal name: `atom_positions`)
