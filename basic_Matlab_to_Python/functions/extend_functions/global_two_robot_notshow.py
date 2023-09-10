import os
import sys

import numpy as np
import scipy.io
from roboticstoolbox import  Link, SerialLink
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.basic_functions.Generate_Joint import generate_joint
from basic_Matlab_to_Python.functions.basic_functions.reachable_ws_indices import reachable_ws_indices
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS_two import boundary_ws_two
from basic_Matlab_to_Python.functions.basic_functions.GlobalEvalution import global_evaluate

current_folder = os.getcwd()
print(current_folder)
sys.path.append(current_folder)
def global_two_robot_notshow(flag, robot1,robot2, robot_type1,robot_type2, parameters, evaluate='Off'):
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
        qs1, count1 = generate_joint(robot1, couple_flag, JointNum=num, Path=robot_type1)
        qs2, count2 = generate_joint(robot2, couple_flag, JointNum=num, Path=robot_type2)
        print(qs1)
        print(qs2)
        # Robot Workspace Analysis
        #reachable workplace + Local Evaluate
        #dex, path, o_volume, volume = reachable_ws_indices(robot, qs, flag, indices=indice_group, visualize=True, path=robot_type)
        dex1, path1= reachable_ws_indices(robot1, qs1, flag, indices=indice_group, visualize=True,path=robot_type1)
        dex2, path2 = reachable_ws_indices(robot2, qs1, flag, indices=indice_group, visualize=True, path=robot_type2)
        print(dex1)
        print(dex2)
    if flag == 1:
        # Load QS data1
        filename = robot_type1
        print(current_folder)
        folder = os.path.dirname(current_folder)
        path_joint1 = folder +'\\' +'Data_QS\\' + filename + str(num)+'.csv'
        # Load QS data1
        filename = robot_type2
        folder = os.path.dirname(current_folder)
        path_joint2 = folder +'\\' + 'Data_QS\\' + filename + str(num) + '.csv'


        with open(path_joint1, 'r') as file:
            lines = file.readlines()

        data_list = []
        for line in lines:
            values = line.strip().split(',')
            floats = [float(value) for value in values]
            data_list.append(floats)

        # Convert the list to a NumPy array
        qs_data1 = np.array(data_list)

        with open(path_joint2, 'r') as file:
            lines = file.readlines()

        data_list = []
        for line in lines:
            values = line.strip().split(',')
            floats = [float(value) for value in values]
            data_list.append(floats)

        # Convert the list to a NumPy array
        qs_data2 = np.array(data_list)

        # Access the 'QS' variable from the loaded data

        count1, _ = qs_data1.shape
        count2, _ = qs_data2.shape


        # Load Master Dex Data
        filename = robot_type1
        folder = os.path.dirname(current_folder)
        path_dex = folder +'\\'+ 'Data_Dex\\' + filename + str(count1) + '.csv'
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
        dex_data1 = np.array(data_list)

        # Access the 'Dex' variable from the loaded data
        dex1 = dex_data1

        # Load Master Dex Data
        filename = robot_type2
        folder = os.path.dirname(current_folder)
        path_dex = folder + '\\' + 'Data_Dex\\' + filename + str(count2) + '.csv'
        # path_dex = os.path.join(folder, 'Data', filename + str(count) + '.mat')
        # dex_data = scipy.io.loadmat(path_dex)
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
        dex_data2 = np.array(data_list)

        # Access the 'Dex' variable from the loaded data
        dex2 = dex_data2

    # General form for Global Evaluation
    indices1, global_indices1 = global_evaluate(dex1)
    indices2, global_indices2 = global_evaluate(dex2)

    if opt['evaluate'] == 'r':
        v_robot = boundary_ws_two(dex1,dex2, 0.1, color='r')
    elif opt['evaluate'] == 'b':
        v_robot = boundary_ws_two(dex1,dex2, 0.1, color='b')
    elif opt['evaluate'] == 'g':
        v_robot = boundary_ws_two(dex1,dex2, 0.1, color='g')
    else:
        v_robot = boundary_ws_two(dex1,dex2, 0.1, color='off')
    v_robot1=v_robot
    v_robot2=v_robot
    return dex1,dex2, v_robot1,v_robot2, global_indices1,global_indices2