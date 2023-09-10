'''
Change visualization modes and parameters
'''
import os
import sys
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
from basic_Matlab_to_Python.functions.basic_functions.ScatterToVolume import scatter_to_volume
from basic_Matlab_to_Python.functions.basic_functions.WS_Visualization import ws_visualization
# sys.path.append(os.getcwd())
import numpy as np
current_folder = os.getcwd()
sys.path.append(current_folder)
parent_directory = os.path.dirname(current_folder)
pwd=parent_directory+'\Data_Dex'
print(pwd)
#pwd = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex'


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

Flag=1
Type = 'dVRK'
RightRobot1, LeftRobot1, Robot_Placement = multi_bimanual_construction(Type, 1)
Dex_B, V_Robot, Global_Indices_Group = global_one_robot(Flag, RightRobot1, Type, Parameters, 'g')

Bimanual_Vector = [np.array(Robot_Placement[1])- np.array(Robot_Placement[0])]
VDual_Robot, VLeft_Robot, VRight_Robot, Boundary_Robot, Volume_Size_Robot = scatter_to_volume(Dex_B, Parameters['Precision'], Robot_Placement[0], Robot_Placement[1], bimanual='BimanualRobot',visual= 'Visual_On')
Volume_Info = {}
Volume_Info['V'] = VDual_Robot
Volume_Info['VDual_Robot'] = VDual_Robot
Volume_Info['VLeft_Robot'] = VLeft_Robot
Volume_Info['VRight_Robot'] = VRight_Robot
Volume_Info['Boundary_Robot'] = Boundary_Robot
Volume_Info['Volume_Size_Robot'] = Volume_Size_Robot
Volume_Info['Precision'] = Parameters['Precision']
print(Volume_Info)

Slice_Flag = [1, 0, 0, 0.1, 0.3]
Bimanual = 1
Evaluation_Index = 'Inverse Condition Number'
Index_Num = 5
Slice = [0, 0, 0, 0.1, 0.3]
print(Bimanual_Vector[0])
Flag_Info = {'Slice_Flag': Slice_Flag, 'Bimanual': Bimanual, 'Evaluation_Index': Evaluation_Index, 'Slice': Slice,
             'Index_Num': Index_Num, 'Bimanual_Vector': Bimanual_Vector[0]}

#plt.rcParams['axes.grid'] = False

# pop = 1  # % Scatter
# # fig=plt.figure()
# String_Out= ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 2  # Volume mode
# # fig=plt.figure()
# String_Out = ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 3  # 'Convhulln'
# # fig = plt.figure()
# String_Out= ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 4  #'Isosurface'
# # fig = plt.figure()
# String_Out= ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 5  # 'Slice'
# # fig = plt.figure()
# String_Out = ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 6  # 'Boundary', 0.1
# # fig = plt.figure()
# String_Out = ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

pop = 7  # Alphashape
# fig = plt.figure()
String_Out= ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)

# pop = 8  # Reachable
# # fig = plt.figure()
# String_Out = ws_visualization(pop, Dex_B, Volume_Info, Flag_Info)
