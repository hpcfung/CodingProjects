import numpy as np
import os, sys
import matplotlib.pyplot as plt

def read_arr(file_path,batch_idx):
    file_path = file_path + '/batch_'+str(batch_idx).zfill(num_digits)+'_raw_observables.csv'
    raw_arr = np.genfromtxt(file_path, delimiter=',')
    arr = np.delete(raw_arr, 0, axis=0)  # remove first row = batch,n_sso,n_ops; nan nan nan
    print(f"arr shape ={arr.shape}")
    return arr

def get_energy_shift(file_path):
    file_path = file_path + '/energy_shift.csv'
    raw_arr = np.genfromtxt(file_path, delimiter=',')
    return raw_arr.item()

def get_beta_list():
    for (dirpath, dirnames, filenames) in os.walk(file_root):
        beta_list = dirnames # the first tuple contains all immediate directories within directory
        break
    return [w[5:] for w in beta_list]

def get_energy(j):
    """
    Returns the energy of the QMC run at the jth beta in beta_list
    Formula: energy = -mean(n_ops) / beta + energy_shift
    """
    file_path = file_root + '/beta=' + beta_list[j] + '/seed=' + seed
    print(file_path)
    for k in range(1,batch+1): # batch 0 is equilibration
        if k == 1:
            tmp_arr = read_arr(file_path,k)
        else:
            tmp_arr = np.concatenate((tmp_arr, read_arr(file_path,k)), axis=0) # merge arrays from different batches

    print(tmp_arr)
    print(tmp_arr.shape)

    n_ops = tmp_arr[:,2] # cols: batch,n_sso,n_ops

    energy_shift = get_energy_shift(file_path)
    print(f"energy shift = {energy_shift}")

    energy = -np.mean(n_ops) / beta_num_list[j] + energy_shift
    print(f"energy = {energy}")
    return energy

if __name__ == "__main__":
    batch = 10
    file_root = 'delta=-0.36'
    seed = '1234'

    num_digits = len(str(batch))


    beta_list = get_beta_list()
    beta_list.sort(key=float)
    beta_num_list = [float(w) for w in beta_list]
    print(beta_list)
    print(beta_num_list)

    energy_list = []
    for j in range(len(beta_list)):
        energy_list.append(get_energy(j))
    print(energy_list)

    results = []
    for i in range(len(beta_list)):
        results.append((beta_num_list[i],energy_list[i]))
    print(f"(beta,energy) = {results}")

    plt.plot(beta_num_list,energy_list)
    plt.show()

