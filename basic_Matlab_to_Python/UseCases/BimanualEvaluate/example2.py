'''
2) Example for WSRender Use Case 2 in paper: Articulated Bimanual
'''
import os
import sys
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
# sys.path.append(os.getcwd())
import numpy as np

current_folder = os.getcwd()
sys.path.append(current_folder)
parent_directory = os.path.dirname(current_folder)
pwd=parent_directory+'\Data_Dex'
print(pwd)
#pwd = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex'

os.chdir(pwd)
sys.path.append(pwd)

# Set the parameters
Parameters = {
    'Couple': 1,
    'Joint_Limit': 0,
    'Monte_Carlo': 0,
    'Iteration': 0,
    'Joint_Num': 15,
    'Precision': 0.02,
    'Error': 0.0001
}

# Load an existing robot data for evaluation
Flag = 1

if Flag == 1:
    Type = 'Articulated'
    RightRobot1, LeftRobot1, Robot_Placement = multi_bimanual_construction(Type, 1)
    Dex_A, V_Robot, Global_Indices_Group = global_one_robot(Flag, RightRobot1, Type, Parameters, 'g')

# Build a new robot
if Flag == 0:
    # Use default parameters
    Parameters['Couple'] = 0
    Parameters['Joint_Limit'] = 0
    Parameters['Monte_Carlo'] = 0
    Parameters['Iteration'] = 0
    Parameters['Joint_Num'] = 15
    Parameters['Precision'] = 0.02
    Parameters['Error'] = 0.0003

    Indice_Group = ['Order-Independent Manipulability', 'Harmonic Mean Manipulability Index', 'Isotropic Index']
    Parameters['Indice'] = Indice_Group

    RobotType = 'Cylindrical'
    Number = 1
    RightRobot, LeftRobot, Robot_Placement = multi_bimanual_construction(RobotType, Number)
    Dex_A, V_Robot, Global_Indices = global_one_robot(Flag, RightRobot, RobotType, Parameters, 'g')


Bimanual_Vector = [np.array(Robot_Placement[1])- np.array(Robot_Placement[0])]
out = VisualWS(Dex_A,evaluate='Reachable', robotnum='Bimanual', vector=Bimanual_Vector[0])


