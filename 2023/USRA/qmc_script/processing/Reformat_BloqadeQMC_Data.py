# Imports

import os
import sys
import copy
import re
import time

import itertools as itr
import numpy as np
import networkx as nx

import torch
from torch import nn
from torch_geometric.data import Batch

import rydberggpt as rgpt
from rydberggpt.data.dataclasses import BaseGraph, GridGraph
from rydberggpt.data.graph_structures import get_graph
from rydberggpt.data.loading.rydberg_dataset import get_rydberg_dataloader
from rydberggpt.data.loading.utils import read_subfolder_data
from rydberggpt.data.utils_graph import networkx_to_pyg_data
from rydberggpt.models.rydberg_encoder_decoder import get_rydberg_graph_encoder_decoder
from rydberggpt.observables.rydberg_energy import get_rydberg_energy
from rydberggpt.utils import create_config_from_yaml, load_yaml_file
from rydberggpt.utils_ckpt import get_ckpt_path, get_model_from_ckpt
from rydberggpt.data.utils_graph import (
    graph_to_dict,
    save_graph_to_json,
    read_graph_from_json,
    dict_to_graph,
)

import pandas as pd
import json


########################################################################################
def slicing_snake_flip(x):
    """
    [[1 2 3 4]
     [5 6 7 8]]
    to
    [[1 2 3 4]
     [8 7 6 5]]
    """
    _x = copy.deepcopy(x)
    for i in range(_x.shape[-2]):
        if i % 2 == 1:
            _x[..., i, :] = _x[..., i, ::-1]
    return _x

def process_qmc_batch(batch_dir):
    """
    Reads batch 1 to 10 in batch_dir
    Returns concatenated numpy array
    Does processing: decorrelation, snake path
    """
    measurements_list = []
    for i in range(1,max_batch+1): # batch 1 to max_batch
        sample_path = os.path.join(batch_dir,"batch_"+str(i).zfill(batch_digits)+"_samples.csv")
        batch_measurements = np.genfromtxt(sample_path, delimiter=",", dtype=str)
        batch_measurements = np.array([i.split(" ") for i in batch_measurements]).astype(
            float
        )
        # decorrelate
        batch_measurements = batch_measurements[::decorrelation_rate,:]

        # snake flip (measurements, spins)
        # start = time.time()
        batch_measurements = np.reshape(batch_measurements, (batch_measurements.shape[0],L,L))
        batch_measurements = slicing_snake_flip(batch_measurements)
        batch_measurements = np.reshape(batch_measurements, (batch_measurements.shape[0],L**2))
        # end = time.time()
        # print(end - start)

        measurements_list.append(batch_measurements)
    measurements = np.concatenate(measurements_list, axis=0)    
    return measurements

def process_qmc_data(qmc_path, save_path):
    """

    """

    # data_path = qmc_path # os.path.join(qmc_path, "data")
    # data_path = "$HOME/scratch/qmc_data/batch_01_samples.csv"
    # data_path = "/home/hpcfung/scratch/qmc_data/batch_01_samples.csv"

    for I, rb_str in enumerate(rb_dict):
        for J, delta_str in enumerate(delta_dict):
            for K, beta_str in enumerate(beta_dict):
                batch_dir = os.path.join(qmc_path,"Rb="+rb_str,"omega="+omega_str,
                               "delta="+delta_str,"beta="+beta_str,
                               "seed="+seed_str)
                measurements = process_qmc_batch(batch_dir=batch_dir)
                Rb = rb_dict[rb_str]
                delta = delta_dict[delta_str]
                beta = beta_dict[beta_str]

                df = pd.DataFrame(
                    {"measurement": list(measurements)},
                    index=range(len(measurements)),
                )


                ########################################################################################

                graph_config = GridGraph(
                    num_atoms=L**2,
                    graph_name="grid_graph",
                    Rb=Rb,
                    delta=delta,
                    omega=omega,
                    beta=beta,
                    n_rows=L,
                    n_cols=L,
                )
                graph = get_graph(graph_config)
                graph_dict = graph_to_dict(graph)

                ########################################################################################

                config_dict = dict(
                    omega=graph_config.omega,
                    lx=graph_config.n_cols,
                    ly=graph_config.n_rows,
                    beta=graph_config.beta,
                    num_atoms=graph_config.num_atoms,
                    delta=graph_config.delta,
                    Rb=graph_config.Rb,
                )

                ########################################################################################

                if save_path is not None:

                    if not os.path.isdir(save_path):
                        os.makedirs(save_path)

                    folder_path = os.path.join(
                        save_path, "BloqadeQMC_L={}_Rb={}_delta={}_beta={}".format(L, rb_str, delta_str, beta_str)
                    )
                    os.mkdir(folder_path)

                    df.to_hdf(
                        os.path.join(folder_path, "dataset.h5"), key="data", mode="w"
                    )
                    save_graph_to_json(
                        graph_dict, os.path.join(folder_path, "graph.json")
                    )

                    with open(os.path.join(folder_path, "config.json"), "w") as f:
                        json.dump(config_dict, f)

                    print(f"{folder_path} generated.")

    return


########################################################################################

if __name__ == "__main__":
    """
    Processes one L=X subdirectory at a time

    Use bash script (need apptainer)
    """

    save_path = os.path.abspath("/SCRATCHTAINER/qmc_data/data")
    # "/home/hpcfung/scratch/qmc_data/tmp_data"
    # os.path.abspath("/home/hpcfung/scratch/qmc_data/data")

    qmc_path = "/SCRATCHTAINER/qmc_data/L=5"
    L = 5

    rb_dict = {"1.05": 1.05, "1.15": 1.15, "1.30": 1.30}
    delta_dict = {"-0.36": -0.364386792453,
                "-0.13": -0.128537735849,
                "0.93": 	0.932783018868,
                "1.05": 1.05070754717,
                "1.17": 1.16863207547,
                "1.29": 	1.28655660377,
                "1.52": 1.52240566038,
                "1.76": 1.75825471698,
                "2.94": 	2.9375,
                "3.17": 3.1733490566}
    beta_dict = {"0.5": 0.5,
                "1.0": 1.0,
                "2.0": 2.0,
                "4.0": 4.0,
                "8.0": 8.0,
                "16.0": 16.0,
                "32.0": 32.0,
                "48.0": 48.0,
                "64.0": 64.0}

    omega_str = "1.00"
    seed_str = "1234"

    max_batch = 10
    batch_digits = len(str(max_batch))
    omega = float(omega_str)

    decorrelation_rate = 10

    

    process_qmc_data(qmc_path, save_path=save_path)
