import os
import sys

import numpy as np
from pathlib import Path

from matplotlib import pyplot as plt

from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
from basic_Matlab_to_Python.functions.extend_functions.global_two_robot_notshow import global_two_robot_notshow
from basic_Matlab_to_Python.functions.extend_functions.workspace_analysis import workspace_analysis
from basic_Matlab_to_Python.functions.basic_functions.Define_Volume import define_volume
from basic_Matlab_to_Python.functions.basic_functions.Scatter_Volume_Convert import scatter_volume_convert
from basic_Matlab_to_Python.functions.basic_functions.Visualize_VolumeDataAll import visualize_volume_data_all
from basic_Matlab_to_Python.functions.basic_functions.Find_Interact_Bimanual import find_interact_bimanual
from basic_Matlab_to_Python.functions.basic_functions.Final_Interact import final_interact
# Set current directory as working path
current_folder = Path.cwd()
# Add current directory to Python path
sys.path.append(str(current_folder))

# Analysis Type: Multi robot
# Load an existing robot data for evaluation
flag = 1
#还没测试flag=0的时候会怎么样

parameters = {
    "Couple": 0,
    "Joint_Limit": 0,
    "Monte_Carlo": 0,
    "Iteration": 0,
    "Joint_Num": 15,
    "Precision": 0.01,
    "Error": 0.0001,
    "Indice": ["Manipulability", "Inverse Condition Number", "Minimum Singular Value"]
}

Type="Spherical"
# Initial parameters
right_robot1,_= BuildOneRobot(Type)
length_sum, prismatic_num, precision,error = initial_precision(right_robot1)

qs = {}

# Load data
dex_group = {}
global_indices_group = {}
bimanual_vector = {}
robot_placement = {}

if flag == 1:
    type_robot=['Articulated','Spherical']
    # type_robot = 'Articulated'
    # type_robot = 'Spherical'
    right_robot1, left_robot1, robot_placement1 = multi_bimanual_construction(type_robot[0], 1)
    right_robot2, left_robot2, robot_placement2 = multi_bimanual_construction(type_robot[1], 1)
    dex_group[1], dex_group[2], v_robot1,v_robot2, global_indices_group1, global_indices_group2 = global_two_robot_notshow(flag, right_robot1,right_robot2, type_robot[0],type_robot[1], parameters, 'g')


    plt.title('Combined Plot')
    plt.show()

if flag == 0:
    type_robot = 'Articulated'
    right_robot1, left_robot1, robot_placement1 = multi_bimanual_construction(type_robot, 1)
    global_indices_group1, dex_group1 = workspace_analysis(right_robot1, parameters, type_robot)
    global_indices_group2 = global_indices_group1

    type_robot = 'Spherical'
    right_robot2, left_robot2, robot_placement2 = multi_bimanual_construction(type_robot, 2)
    global_indices_group3, dex_group3 = workspace_analysis(right_robot2, parameters, type_robot)
    global_indices_group4 = global_indices_group3
bimanual_vector= {}
bimanual_vector[1] = np.subtract(robot_placement1[2], robot_placement1[1])
dex_group[3] = dex_group[1]
dex_group[3][:, 0:3] =np.add(dex_group[1][:,0:3] ,bimanual_vector[1][:3])

bimanual_vector2 = np.subtract(robot_placement2[2] ,robot_placement2[1])
dex_group[4] = dex_group[2]
dex_group[4][:, 0:3] =np.add(dex_group[2][:,0:3], bimanual_vector[2][0:3])


####################################

Precision=parameters['Precision']
Dex_Group_Temp1=dex_group2
Dex_Group_Temp2=dex_group4
Dex_Group_Temp1[:,4]=1
Dex_Group_Temp2[:,4]=1
Dex_Group_Temp=[Dex_Group_Temp1,Dex_Group_Temp2]

Boundary,Volume_Size = define_volume(Dex_Group_Temp,Precision);
V_All,V_Group = scatter_volume_convert(Dex_Group_Temp,Precision,Boundary,Volume_Size);

# Assuming V_Group is a list containing the volume data
v_bimanual = [None] * 2
v_bimanual_b = [None] * 2

v_bimanual[0] = V_Group[0]
v_bimanual[1] = V_Group[1]
v_bimanual_b[0] = V_Group[0]
v_bimanual_b[1] = V_Group[1]
index = 4

################################

# Bimanual A
plt.figure()
transfer_robot, transfer_all = visualize_volume_data_all(Boundary, v_bimanual, Volume_Size, precision, index, visual='Scatter')
plt.axis('off')

dex_a = [dex_group1, dex_group2]

volume_all_a, volume_interact_a = find_interact_bimanual(dex_a, Boundary, Volume_Size, precision, visual='Off')

# Bimanual B
plt.figure()
transfer_robot_b, transfer_all_b = visualize_volume_data_all(Boundary, v_bimanual_b, Volume_Size, precision, index, visual='Scatter')
plt.axis('off')

dex_b = [Dex_Group_Temp[0], Dex_Group_Temp[1]]
volume_all_b, volume_interact_b = find_interact_bimanual(dex_b, Boundary, Volume_Size, precision, visual='Off')

# Bimanual A + B
plt.figure()
transfer_group = [transfer_all, transfer_all_b]
volume_all, volume_interact, transfer_new = final_interact(transfer_group, Boundary, Volume_Size, precision, visual='Scatter')


