"""
Physics Preamble:
- Photons in a 1D cavity come in modes indexed by m = 1, 2, 3, ...
- Any (energy eigen)state is indexed by the number of photons in each mode: (n1, n2, n3, ...)
- In general, the multiplicity is the function Omega(U,V,N)
- Here we compute Omega(U,N)
- Note that the energy per photon in the mth mode is hcm/2L
- Hence U is always an integer multiple of hcm/2L for any state
- We use units where hc/2L = 1
- Then the energy of a single photon in the mth mode is just m
- Note that when the energy is bounded by U, then the highest occupied mode is the Uth mode or lower
- So we only consider states of the form (n1, n2, n3, ..., nU)

Program:
- We write (n1, n2, n3, ..., nU) as the array [n1 n2 n3 ... nU]
- The program outputs the multiplicities as the array Omega:
[Omega(U,N=1) Omega(U,N=2) ... Omega(U,N=U)]
"""

import numpy as np
import sys
import matplotlib.pyplot as plt

def one_more_digit(seq,pointer,length,remaining_energy):
    """
    eg seq = ( , , 0) [(0, 0, 0)]
    pointer = 1
    length = 3
    remaining_energy = 3

    pointer = 1 -> 2nd index: try j = 0, 1 (not 2: total energy 4 > 3)
    """
    if pointer == 0:
        new_seq = np.copy(seq)
        new_seq[0] = remaining_energy
        increment_Omega(seq=new_seq)
    else:
        energy_per_particle_at_pointer = pointer+1
        max_particle_num_at_pointer = remaining_energy//energy_per_particle_at_pointer
        for particle_num_at_pointer in range(max_particle_num_at_pointer+1):
            new_seq = np.copy(seq)
            new_seq[pointer] = particle_num_at_pointer
            new_remaining_energy = remaining_energy - particle_num_at_pointer * energy_per_particle_at_pointer
            # print(new_seq, pointer - 1, new_remaining_energy)
            one_more_digit(seq=new_seq, pointer=pointer - 1, length=length,
                           remaining_energy=new_remaining_energy)

def increment_Omega(seq):
    global Omega
    N = np.sum(seq) # total particle number of state
    Omega[N - 1] += 1
    print(f"{seq}   N = {N}")

if __name__ == "__main__":
    U = 30  # 5
    Omega = np.zeros(U, dtype=np.int64)

    seq = np.zeros(U, dtype=np.int64)
    one_more_digit(seq=seq,pointer=U-1,length=U,remaining_energy=U)
    print(f"Omega = {Omega}")
    x_axis = np.arange(start=1,stop=U+1)
    plt.plot(x_axis,Omega)
    plt.show()
