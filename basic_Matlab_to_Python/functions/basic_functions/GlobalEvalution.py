'''
% Input:
% Dex: Local Indices distribution map
%
% Output:
% Indices: number of indices
% Global_Indices: modified global indices
%
% Function:
% General form for Global Evaluation
%
% Example:
% [Indices,Global_Indices] = GlobalEvaluate(Dex);
'''
from typing import List
import argparse
import numpy as np
from basic_Matlab_to_Python.functions.basic_functions.local_indice_map import local_indice_map
from basic_Matlab_to_Python.functions.basic_functions.tb_optparse import tb_optparse


def global_evaluate(Dex, **kwargs):
    # parser=argparse.ArgumentParser(description='Global Evaluation Options')
    # parser.add_argument('--evaluate', default='General', choices=['General'], help='Evaluation type')
    # parser.add_argument('--indice', nargs='+', type=int, help='Indices for calculation')
    # args = parser.parse_args()

    opt = {
        'evaluate': 'General',
        'Indice':None,
    }
    opt.update(kwargs)
    print(opt)


    Dex = np.array(Dex)
    N, Ind = Dex.shape
    print(N,Ind)
    Indices = Ind - 3

    if opt['Indice'] is None:
        Global_Indices = np.zeros(Indices)
        if opt['evaluate'] == 'General':
            for i in range(Indices):
                Global_Indices[i] = np.sum(Dex[:, i+3]) / N
                Global_Indices[i] = np.real(Global_Indices[i])
                # Global_Indices[i+1] = np.min(Dex[:, 6]) / np.max(Dex[:, 9])
                Global_Indices[i ] = np.min(Dex[:, i]) / np.max(Dex[:, i])
    else:
        Indice_Group = opt['Indice']
        Num_Array = local_indice_map(Indice_Group)  # Implement Local_Indice_Map function accordingly
        _, Cal_Index = Num_Array.shape
        Global_Indices = np.zeros(Cal_Index)
        for K in range(Cal_Index):
            Global_Indices[K] = np.sum(Dex[:, Num_Array[0, K]]) / N

    return Indices, Global_Indices


