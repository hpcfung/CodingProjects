The chemical potential of a photon = 0

Can we see this from (\frac{\partial{S(U,V,N)}{\partial N})_{U,V} = 0?

Compute \Omega(U,V,N) numerically

## Explanation

(U, V, N) is used to label the macrostate. These 3 state variables are chosen because they are assumed to be conserved. Then for an isolated system (microcanonical ensemble), if we know that the system is in the macrostate (U, V, N) at some time t0, it wil always be in the macrostate (U, V, N) at all future times t.

As stated in Schroeder, the fundamental assumption of statistical mechanics is:
In an isolated system in thermal equilibrium, all accessible microstates are equally probable.
If the system is in the macrostate (U, V, N), then the accessible microstates are those with energy U, volume V, and number N.

Note that the entropy  and the multiplicity Omega counts the number of accessible microstates, since they in some sense quantify our knowledge (or ignorance) of the system.

For photons in a cavity (in the microcanonical ensemble), we know that the photon number N is not a conserved quantity. If the photons are in the state (U, V, N_0) at some time t, it may evolve into the state (U, V, N_1).

As such, if the photons are in the state (U, V, N), actually all microstates corresponding to (U, V, N'), where N' is an arbitrary number, is accessible.

So strictly speaking, for photons, the macrostate is labelled by (U, V) only, and Omega and S are functions of (U, V) only.

(This is why the Omega(U, V, N) computed numerically before is not physical; in actuality, microstates with all values of N are accessible, but we assumed that only microstates with fixed N is accessible.)

Thus for photons, N is not a thermodynamic state variable. If we rederive all the thermodynamic relations in this smaller (U, V) space, we will end up with eg



Now suppose the system is allowed to interact with the reservoir. The combined system + reservoir is once again an isolated system (microcanonical ensemble). As shown in Schroeder Ch.6, when the thermodynamic relation is dU = T dS - P dV, it leads to the Boltzmann distribtuion for the canonical ensemble.

In some sense, since dN do not show up in dU = T dS - P dV, it is like the system is always in the canonical ensemble.

If we really want to reuse the existing (U, V, N) formalism, then to match 
we have to set mu = 0. (Also, if we set mu = 0, the Gibbs factors reduce to the Boltzmann factors. ie the grand canonical probability distribution is equal to the canonical distribution.)

However I think this is technically incorrect, since it would imply that the state variables are (U, V, N), while they should be (U, V). ie it gives the wrong conclusion that you need all (U, V, N) to describe a macrostate, which leads to incorrect multiplicity counting.

Incidentally, we know that at high energies/temperature, particle creation is possible even for massive particles, ie particle number is not conserved. (At relativistic energies, massive particles are effectively massless.) Therefore the argument above also applies. (Unless maybe if you modify the particle number to be particle number - antiparticle number? Or maybe you would use charge conservation instead?)
