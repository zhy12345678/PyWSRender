import numpy as np
import matplotlib.pyplot as plt
import sys

from pathlib import Path

from basic_Matlab_to_Python.functions.basic_functions.BuildOneRobot import BuildOneRobot
from basic_Matlab_to_Python.functions.basic_functions.Initial_Precision import initial_precision
from basic_Matlab_to_Python.functions.extend_functions.multi_bimanual_construction import multi_bimanual_construction
from basic_Matlab_to_Python.functions.extend_functions.global_two_robot_notshow import global_two_robot_notshow
from basic_Matlab_to_Python.functions.extend_functions.global_one_robot import global_one_robot
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

# Initial Parameters
Flag = 1
Parameters = {
    'Couple': 0,
    'Joint_Limit': 0,
    'Monte_Carlo': 0,
    'Iteration': 0,
    'Joint_Num': 45,
    'Precision': 0.01,
    'Error': 0.0001,
    'Indice':  ["Manipulability", "Inverse Condition Number","Minimum Singular Value","Order-Independent Manipulability","Harmonic Mean Manipulability Index","Isotropic Index"]
}

Type="Omni"
right_robot1,_= BuildOneRobot(Type)
length_sum, prismatic_num, precision,error = initial_precision(right_robot1)



# Load data
if Flag == 1:
    Type = 'Articulated'
    RightRobot1, LeftRobot1, Robot_Placement1 = multi_bimanual_construction(Type, 1)
    Dex_Group, V_Robot, Global_Indices_Group = {}, {}, {}
    Dex_Group[1], V_Robot, Global_Indices_Group[2] = global_one_robot(Flag, RightRobot1, Type, Parameters, 'g')

    Type = 'Spherical'
    RightRobot2, LeftRobot2, Robot_Placement2 = multi_bimanual_construction(Type, 1)
    Dex_Group[2], V_Robot, Global_Indices_Group[2] = global_one_robot(Flag, RightRobot2, Type, Parameters, 'g')

# ...

elif Flag == 0:
    Type = 'Articulated'
    RightRobot1, LeftRobot1, _ = multi_bimanual_construction(Type, 1)
    print(Parameters)
    Global_Indices_Group, Dex_Group = {}, {}
    Global_Indices_Group[1], Dex_Group[1] = workspace_analysis(RightRobot1, Parameters, Type)
    Global_Indices_Group[2] = Global_Indices_Group[1]

    Type = 'Spherical'
    RightRobot2, LeftRobot2, Robot_Placement = multi_bimanual_construction(Type, 2)
    Global_Indices_Group[3], Dex_Group[3] = workspace_analysis(RightRobot2, Parameters, Type)
    Global_Indices_Group[4] = Global_Indices_Group[3]

Bimanual_Vector = {}
Bimanual_Vector[1] = np.subtract(Robot_Placement1[2], Robot_Placement1[1])
Dex_Group[3] = Dex_Group[1]
Dex_Group[3][:, 0:3] = np.add(Dex_Group[1][:, 0:3], Bimanual_Vector[1][0:3])

Bimanual_Vector[2] = np.subtract(Robot_Placement2[2], Robot_Placement2[1])
Dex_Group[4] = Dex_Group[2]
Dex_Group[4][:, 0:3] = np.add(Dex_Group[2][:, 0:3], Bimanual_Vector[2][0:3])

# Assuming Define_Volume and Scatter_Volume_Convert are implemented in Python
Precision = 0.01
Dex_Group_Temp = Dex_Group

Dex_Group_Temp[3][:, 3] = 1
Dex_Group_Temp[4][:, 3] = 1
print(Dex_Group_Temp,Dex_Group)

Boundary, Volume_Size = define_volume(Dex_Group_Temp, Precision)
print(Boundary,Volume_Size)
V_All, V_Group = scatter_volume_convert(Dex_Group_Temp, Precision, Boundary, Volume_Size)

# For visualization using matplotlib
V_Bimanual = {1: V_Group[1], 2: V_Group[2]}
V_Bimanual_B = {1: V_Group[3], 2: V_Group[4]}
Index = 4


# Index_Name = 'Indices'  # Placeholder, you might need to adjust this
# Num_Array = Local_Indice_Map(Index_Name)  # Assuming Local_Indice_Map function is translated

# Bimanual A
plt.figure()
Transfer_Robot, TransferAll = visualize_volume_data_all(Boundary, V_Bimanual, Volume_Size, Precision, Index, visual= 'Bimanual')
plt.axis('off')
print("step1")

Dex_A = [Dex_Group[1], Dex_Group[2]]
Volume_All_A, Volume_Interact_A = find_interact_bimanual(Dex_A, Boundary, Volume_Size, Precision,visual= 'Off')
print("step2")
# Bimanual B
plt.figure()
Transfer_Robot_B, TransferAll_B = visualize_volume_data_all(Boundary, V_Bimanual_B, Volume_Size, Precision, Index, visual='Scatter')
plt.axis('off')
print("step3")
Dex_B = [Dex_Group_Temp[3], Dex_Group_Temp[4]]
Volume_All_B, Volume_Interact_B = find_interact_bimanual(Dex_B, Boundary, Volume_Size, Precision,visual= 'Off')
print("step4")
print(TransferAll,TransferAll_B)
# Bimanual A + B
plt.figure()
#Transfer_Group = [TransferAll, TransferAll_B]
Transfer_Group={}
Transfer_Group[1] =TransferAll
Transfer_Group[2] =TransferAll_B
print("step0")
Volume_All, Volume_Interact, Transfer_New = final_interact(Transfer_Group, Boundary, Volume_Size, Precision, 'Local_Indices', 'Scatter')
print("step5")
plt.show()


# Visualization in Python (example for scatter plot)
fig, ax = plt.subplots()
# ax.scatter(x_data, y_data) # Replace with your data
plt.show()
