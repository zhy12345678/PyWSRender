'''

Example for WSRender Use Case 2 in paper: Spherical Bimanual
Manipulator distribution map visualization
'''
import os
import sys
import numpy as np

from matplotlib import pyplot as plt

# Load an existing robot data for evaluation
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS

current_folder = os.getcwd()
sys.path.append(current_folder)
parent_directory = os.path.dirname(current_folder)
pwd=parent_directory+'\Data_Dex'
print(pwd)
os.chdir(pwd)
sys.path.append(pwd)
#pwd = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex'




Parameters = {
    'Couple': 0,
    'Joint_Limit': 0,
    'Monte_Carlo': 0,
    'Iteration': 0,
    'Joint_Num': 15,
    'Precision': 0.01,
    'Error': 0.0001
}
Flag = 1
# Set the parameters


if Flag == 1:
    Type = 'Spherical'
    RightRobot2, LeftRobot2, Robot_Placement = multi_bimanual_construction(Type, 1)
    Dex_B, V_Robot, Global_Indices_Group = global_one_robot(Flag, RightRobot2, Type,Parameters, 'g')

# Build a new robot
if Flag == 0:
    # Use Default Parameters in script mode
    Parameters.Couple = 0
    Parameters.Joint_Limit = 0
    Parameters.Monte_Carlo = 0
    Parameters.Iteration = 0
    Parameters.Joint_Num = 60
    Parameters.Precision = 0.01
    Parameters.Error = 0.0001
    Indice_Group = ['Manipulability', 'Inverse Condition Number', 'Minimum Singular Value']
    Parameters.Indice = Indice_Group

    RobotType = 'Spherical'
    Number=1
    RightRobot, LeftRobot, Robot_Placement = multi_bimanual_construction(RobotType, Number)
    plt.figure()
    Dex_B, V_Robot, Global_Indices = global_one_robot(Flag, RightRobot, RobotType, Parameters, 'g')


Bimanual_Vector = [np.array(Robot_Placement[1])- np.array(Robot_Placement[0])]
out = VisualWS(Dex_B, evaluate='Local_Indices', robotnum='Bimanual', vector=Bimanual_Vector[0])

