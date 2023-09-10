import os
import sys

import numpy as np
from pathlib import Path

from matplotlib import pyplot as plt

from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS
from basic_Matlab_to_Python.functions.basic_functions.VisualWS2 import VisualWS2
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
from basic_Matlab_to_Python.functions.extend_functions.global_two_robot_notshow import global_two_robot_notshow
from basic_Matlab_to_Python.functions.extend_functions.workspace_analysis import workspace_analysis


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
    "Precision": 0.02,
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
    dex_group1, dex_group2, v_robot1,v_robot2, global_indices_group1, global_indices_group2 = global_two_robot_notshow(flag, right_robot1,right_robot2, type_robot[0],type_robot[1], parameters, 'g')


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

# bimanual_vector1 = np.array(robot_placement1[1]) - np.array(robot_placement1[0])
# dex_group2 = dex_group1
# dex_group2[:, :3] =dex_group1[:,:3] +bimanual_vector1[:3]
#
# bimanual_vector2 = np.array(robot_placement2[3]) - np.array(robot_placement2[2])
# dex_group4 = dex_group2
# dex_group4[:, :3] =dex_group2[:,:3]+ bimanual_vector2[:3]
#Bimanual_Vector = [np.array(Robot_Placement[1])- np.array(Robot_Placement[0])]
#dex_group1, dex_group2, v_robot1,v_robot2, global_indices_group1, global_indices_group2
#right_robot1, left_robot1, robot_placement1
#right_robot2, left_robot2, robot_placement2
bimanual_Vector1 = [np.array(robot_placement1[1])- np.array(robot_placement1[0])]
bimanual_Vector2 = [np.array(robot_placement2[1])- np.array(robot_placement2[0])]

out = VisualWS2(dex_group1, dex_group2,evaluate='Reachable', robotnum='Bimanual', vector1=bimanual_Vector1[0],vector2=bimanual_Vector2[0])

combined_array = np.hstack((array1, array2))