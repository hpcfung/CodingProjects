import numpy as np
import os, sys
import matplotlib.pyplot as plt

def read_arr(file_path,batch_idx):
    file_path = file_path + '/batch_'+str(batch_idx).zfill(num_digits)+'_raw_observables.csv'
    raw_arr = np.genfromtxt(file_path, delimiter=',')
    arr = np.delete(raw_arr, 0, axis=0)  # remove first row batch,n_sso,n_ops; nan nan nan
    print(f"arr shape ={arr.shape}")
    return arr

def get_energy_shift():
    file_path = 'seed=1234/energy_shift.csv'
    raw_arr = np.genfromtxt(file_path, delimiter=',')
    return raw_arr.item()

def get_beta_list():
    for (dirpath, dirnames, filenames) in os.walk(file_root):
        beta_list = dirnames
        break
    return [w[5:] for w in beta_list]

def get_energy(j):
    file_path = file_root + '/beta=' + beta_list[j] + '/seed=' + seed
    print(file_path)
    for k in range(1,batch+1): # batch 0 is equilibration
        if k == 1:
            tmp_arr = read_arr(file_path,k)
        else:
            tmp_arr = np.concatenate((tmp_arr, read_arr(k)), axis=0)

    print(tmp_arr)
    print(tmp_arr.shape)

    n_ops = tmp_arr[:,2]

    energy_shift = get_energy_shift()
    print(f"energy shift = {energy_shift}")

    energy = -np.mean(n_ops) / beta + energy_shift
    print(energy)

if __name__ == "__main__":
    batch = 10
    beta = 0.5
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

    # plt.plot([2,1,3],[4,1,9]) # (1,1), (2,4), (3,9)
    # plt.show()

