import numpy as np
from scipy.spatial.transform import Rotation as R
from basic_Matlab_to_Python.functions.basic_functions.Draw_environment import draw_environment
from basic_Matlab_to_Python.functions.basic_functions.ReadFiles import read_files
from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.basic_functions.PlaceTwoRobot import PlaceTwoRobot


def multi_bimanual_construction(Type, Number):
    # Analysis Type: Dual-Arm robot
    if Number == 1:
        # Environment
        out = draw_environment('off')

    # Config
    #这边是有问题的
    file_dir, Configs = read_files(type='Placement')

    n = len(file_dir)
    Robot_Num = n

    Robot_Placement = []
    for j in range(Robot_Num):
        T = Configs[j+1]
        Euler = R.from_matrix(T[:3, :3]).as_euler('XYZ')
        Robot_Placement.append([T[0, 3], T[1, 3], T[2, 3], Euler[0], Euler[1], Euler[2]])

    # Dual-Arm Robot
    RightRobot,_ = BuildOneRobot(Type)
    LeftRobot,_ = BuildOneRobot(Type)
    baseright_initial=Robot_Placement[(Number * 2) - 1]
    baseleft_initial =Robot_Placement[(Number * 2) ]


    RightRobot, LeftRobot = PlaceTwoRobot(RightRobot, LeftRobot,Number, visual='Off', baseright=baseright_initial,
                                          baseleft=baseleft_initial)

    return RightRobot, LeftRobot, Robot_Placement
