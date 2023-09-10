import os
import sys

import numpy as np
import scipy.io
from roboticstoolbox import  Link, SerialLink
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.basic_functions.Generate_Joint import generate_joint
from basic_Matlab_to_Python.functions.basic_functions.reachable_ws_indices import reachable_ws_indices
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws
from basic_Matlab_to_Python.functions.basic_functions.GlobalEvalution import global_evaluate
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS2 import boundary_ws2


current_folder = os.getcwd()
print(current_folder)
sys.path.append(current_folder)

def global_one_robot(flag, robot, robot_type, parameters, evaluate='Off'):
    opt = {'evaluate': evaluate}

    num = parameters['Joint_Num']
    couple_flag = parameters['Couple']
    if flag == 0:
        indice_group = parameters['Indice']
    else:
        indice_Group = []

    dex=[]
    count=0

    # Flag == 0: First time calculation
    # Flag == 1: Load Data


    if flag == 0:
        #length_Sum, Prismatic_Num, Precision=initial_precision(robot)
        #visual_robot(robot{2},robot{2},length_Sum,'On') 这边这个有点问题robot的用法
        qs, count = generate_joint(robot, couple_flag, JointNum=num, Path=robot_type)
        print(qs)
        # Robot Workspace Analysis
        print(indice_group)
        #reachable workplace + Local Evaluate
        #dex, path, o_volume, volume = reachable_ws_indices(robot, qs, flag, indices=indice_group, visualize=True, path=robot_type)
        dex, path,O_Volume,Volume= reachable_ws_indices(robot, qs, flag, indices=indice_group, visualize=True,path=robot_type)

        print(dex)
    if flag == 1:
        # Load QS data
        filename = robot_type
        folder = current_folder
        print(folder)
        path_joint = f"../Data_QS/{filename}{str(num)}.csv"
        #path_joint = folder +'UseCases\\' +'Data_QS\\' + filename + str(num)+'.csv'

        #path_joint = os.path.join(folder, 'Data', filename + str(num) + '.mat')
        # qs_data = scipy.io.loadmat(path_joint)
        #qs_data = np.load(path_joint,allow_pickle=True)
        # data = np.loadtxt(path_joint)
        # qs_data = np.array(data)
        with open(path_joint, 'r') as file:
            lines = file.readlines()

        data_list = []
        for line in lines:
            values = line.strip().split(',')
            floats = [float(value) for value in values]
            data_list.append(floats)

        # Convert the list to a NumPy array
        qs_data = np.array(data_list)


        # Access the 'QS' variable from the loaded data

        count, _ = qs_data.shape


        # Load Master Dex Data
        filename = robot_type
        #path_dex = folder +'UseCases\\'+ 'Data_Dex\\' + filename + str(count) + '.csv'
        path_dex = f"../Data_Dex/{filename}{str(count)}.csv"
        #path_dex = os.path.join(folder, 'Data', filename + str(count) + '.mat')
        #dex_data = scipy.io.loadmat(path_dex)
        # data = np.loadtxt(path_dex)
        # dex_data = np.array(data)
        with open(path_dex, 'r') as file:
            lines = file.readlines()

        data_list = []
        for line in lines:
            values = line.strip().split(',')
            floats = [float(value) for value in values]
            data_list.append(floats)

        # Convert the list to a NumPy array
        dex_data = np.array(data_list)

        # Access the 'Dex' variable from the loaded data
        dex = dex_data

    # General form for Global Evaluation
    print("这里",dex)
    indices, global_indices = global_evaluate(dex)
    print("global!!!")
    print(indices)
    print(global_indices)

    if opt['evaluate'] == 'r':
        v_robot = boundary_ws2(dex, 0.1, color='r')
    elif opt['evaluate'] == 'b':
        v_robot = boundary_ws2(dex, 0.1, color='b')
    elif opt['evaluate'] == 'g':
        v_robot = boundary_ws2(dex, 0.1, color='g')
    else:
        v_robot = boundary_ws2(dex, 0.1, color='off')

    return dex, v_robot, global_indices



# # Main script
# flag = 0
# robot = SerialLink([
#     Link([0, 0, 0, 0]),  # Joint 1
#     Link([0, 0, 0, -np.pi / 2]),  # Joint 2
#     Link([0, 0, 0, np.pi / 2]),  # Joint 3
#     Link([0.2794, 0, 0, -np.pi / 2]),  # Joint 4
#     Link([0, 0, 0, np.pi / 2]),  # Joint 5
#     Link([0.3048, 0, 0, 0])  # Joint 6
# ])
#
# parameters = {
#     'Joint_Num': 60,
#     'Couple': 1,
#     'Indice': ['Manipulability', 'Inverse ConditionNumber', 'Minimum Singular Value', 'Order-Independent Manipulability'],
# 'Precision': 0.02,
# 'Error': 0.0001
# }
#
# dex, v_robot, global_indices = global_one_robot(flag, robot, 'dVRK', parameters, evaluate='Off')
#
# import matplotlib.pyplot as plt
# fig = plt.figure(1)
# plt.scatter(dex[:, 0], dex[:, 1], c='blue')
# plt.scatter(v_robot[:, 0], v_robot[:, 1], c='red')
# plt.colorbar()
# plt.show()