# Imports

import os
import sys

import copy

import re

import itertools as itr

import numpy as np

# import matplotlib
# from matplotlib import colors, cm, patches
# import matplotlib.pyplot as plt
# from mpl_toolkits.axes_grid1 import make_axes_locatable

# import networkx as nx

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

#######################################################################################

# Package parameters

# matplotlib.rcParams["figure.figsize"] = (12, 8)
# matplotlib.rcParams["font.size"] = 30
# matplotlib.rcParams["text.usetex"] = True
# matplotlib.rcParams["mathtext.fontset"] = "stix"
# matplotlib.rcParams["font.family"] = "STIXGeneral"


########################################################################################


def process_qmc_data(qmc_path, save_path):
    """
    Expects eg batch_02_samples.csv
    csv file may be in nested directories
    """

    # data_path = qmc_path # os.path.join(qmc_path, "data")
    data_path = "/home/hpcfung/scratch/qmc_data/batch_01_samples.csv"

    dfs = []
    filenames = []
    # TMP BEGINS
    sample_path = "/home/hpcfung/scratch/qmc_data/batch_01_samples.csv" # os.path.join(directory, file)

    filenames.append(sample_path)

    # m = re.findall(r"(\w+)=([+-]?[0-9]*[.]?[0-9]*)", sample_path)

    L = 5 # int(m[0][1])
    delta = -0.364386792453 # float(m[1][1])
    Rb = 1.05
    beta = 64.0

    print(
        "{:<80}".format(
            "\rCurrently processing L={}, delta={} data".format(L, delta)
        ),
        end="\n",
    )
    sys.stdout.flush()

    ########################################################################################

    measurements = np.genfromtxt(sample_path, delimiter=",", dtype=str)
    measurements = np.array([i.split(" ") for i in measurements]).astype(
        float
    )

    df = pd.DataFrame(
        {"measurement": list(measurements)},
        index=range(len(measurements)),
    )

    dfs.append(df)

    ########################################################################################

    graph_config = GridGraph(
        num_atoms=L**2,
        graph_name="grid_graph",
        Rb=Rb,
        delta=delta,
        omega=1.0,
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
            save_path, "QMC_L={}_delta={}".format(L, delta)
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

    # TMP ENDS

    # for I, rb in enumerate(rb_dict):
    #     for J, delta in enumerate(delta_dict):
    #         for K, beta in enumerate(beta_dict):
                

    # for directory, subdirlist, filelist in os.walk(data_path):
    #     for file in filelist:
    #         if file.endswith("samples.csv"):

    #             sample_path = os.path.join(directory, file)

    #             filenames.append(sample_path)

    #             m = re.findall(r"(\w+)=([+-]?[0-9]*[.]?[0-9]*)", sample_path)

    #             L = int(m[0][1])
    #             delta = float(m[1][1])

    #             print(
    #                 "{:<80}".format(
    #                     "\rCurrently processing L={}, delta={} data".format(L, delta)
    #                 ),
    #                 end="\n",
    #             )
    #             sys.stdout.flush()

    #             ########################################################################################

    #             measurements = np.genfromtxt(sample_path, delimiter=",", dtype=str)
    #             measurements = np.array([i.split(" ") for i in measurements]).astype(
    #                 float
    #             )

    #             df = pd.DataFrame(
    #                 {"measurement": list(measurements)},
    #                 index=range(len(measurements)),
    #             )

    #             dfs.append(df)

    #             ########################################################################################

    #             graph_config = GridGraph(
    #                 num_atoms=L,
    #                 graph_name="grid_graph",
    #                 Rb=1.2,
    #                 delta=delta,
    #                 omega=1.0,
    #                 beta=1.0,
    #                 n_rows=1,
    #                 n_cols=L,
    #             )
    #             graph = get_graph(graph_config)
    #             graph_dict = graph_to_dict(graph)

    #             ########################################################################################

    #             config_dict = dict(
    #                 omega=graph_config.omega,
    #                 lx=graph_config.n_cols,
    #                 ly=graph_config.n_rows,
    #                 beta=graph_config.beta,
    #                 num_atoms=graph_config.num_atoms,
    #                 delta=graph_config.delta,
    #                 Rb=graph_config.Rb,
    #             )

    #             ########################################################################################

    #             if save_path is not None:

    #                 if not os.path.isdir(save_path):
    #                     os.makedirs(save_path)

    #                 folder_path = os.path.join(
    #                     save_path, "EssiQQurke_L={}_delta={}".format(L, delta)
    #                 )
    #                 os.mkdir(folder_path)

    #                 df.to_hdf(
    #                     os.path.join(folder_path, "dataset.h5"), key="data", mode="w"
    #                 )
    #                 save_graph_to_json(
    #                     graph_dict, os.path.join(folder_path, "graph.json")
    #                 )

    #                 with open(os.path.join(folder_path, "config.json"), "w") as f:
    #                     json.dump(config_dict, f)

    return dfs, filenames


########################################################################################

save_path = os.path.abspath("/home/hpcfung/scratch/qmc_data/tmp_data")
# os.path.abspath("/home/hpcfung/scratch/qmc_data/data")

qmc_path = "/home/hpcfung/scratch/qmc_data/L=5"

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

########################################################################################

dfs, f = process_qmc_data(qmc_path, save_path=save_path)
sys.exit()

# below: probably observables plots from QMC data
########################################################################################

i = 6
print("Using dataset: {}".format(f[i]))

x = dfs[i].measurement
x = np.array(list(x)).astype(float)

plt.imshow(x[:10])

########################################################################################


L = 8
delta = []
x = []
for i, s in enumerate(f):
    m = re.findall(r"(\w+)=([+-]?[0-9]*[.]?[0-9]*)", s)

    if int(m[0][1]) != 8:
        continue
    else:
        delta.append(float(m[1][1]))
        x.append(np.array(list(dfs[i]["measurement"].to_numpy())))

delta = np.array(delta)
x = torch.from_numpy(np.array(x))

sigmas = (x - 0.5)[:, :, None, :]


idcs = np.indices((1, 8))
cb_A = idcs.sum(0) % 2
cb_B = (idcs.sum(0) + 1) % 2

stagm = torch.abs((sigmas * cb_A - sigmas * cb_B).mean((-1, -2)))


# plt.plot(delta, stagm.mean(-1))
# plt.fill_between(
#     delta,
#     stagm.mean(-1) + stagm.std(-1) / np.sqrt(stagm.shape[-1]),
#     stagm.mean(-1) - stagm.std(-1) / np.sqrt(stagm.shape[-1]),
#     alpha=0.5,
# )

stagm = x.sum(-1)

plt.plot(delta, stagm.mean(-1))
plt.fill_between(
    delta,
    stagm.mean(-1) + stagm.std(-1) / np.sqrt(stagm.shape[-1]),
    stagm.mean(-1) - stagm.std(-1) / np.sqrt(stagm.shape[-1]),
    alpha=0.5,
)
