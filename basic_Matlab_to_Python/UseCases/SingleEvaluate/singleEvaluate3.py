'''
Example for robot evaluation using user-defined robot
1. 注意flag
2. 注意joint_Num
3. 注意type和define
4. 注意r ,g, 变化
'''

import os
import sys
import roboticstoolbox as rtb

from basic_Matlab_to_Python.functions.basic_functions.BuildRobot import BuildRobot
from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
from pathlib import Path

from math import pi
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH, RevoluteMDH, PrismaticMDH





# Set the current folder as the working directory
current_folder = os.getcwd()
print(current_folder)
sys.path.append(current_folder)

Flag = 0
# Use Default Parameters in script mode
Parameters = {
    'Couple': 1,
    'Joint_Limit': 0,
    'Monte_Carlo': 0,
    'Iteration': 0,
    'Joint_Num': 40,
    'Precision': 0.02,
    'Error': 0.0001,
    'Indice': ["Manipulability", "Inverse Condition Number", "Minimum Singular Value", "Order-Independent Manipulability"]
}
# Define the robot parameters 这个type原本我是用的dVRK但是因为我还不知道这些文件是从哪生成的所以我就改了一个文件里有的机器人类型，这个也是之后要弄懂的问题
#这个robottype 好像是可以一次建立一个robot或者一次建立两个
robot_type = 'Define'
robot_name = 'example1.3'
# Create a Robot object
Robot,N_Dof = BuildOneRobot(robot_type)
Dex, V_Robot, Global_Indices =global_one_robot(Flag, Robot, robot_type, Parameters, 'r')