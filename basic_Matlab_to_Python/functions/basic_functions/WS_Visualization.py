'''
% Input:
% Pop: index mode for visualization in the GUI
% Dex: local indices distribution map
% Volume_Info: volume data information
% Flag_Info: flag information
%
% Output:
% String_Out: the name of mode
%
% Function:
% Visualize the workspace by rendering in different modes
'''


import numpy as np
from matplotlib import collections
from mpl_toolkits.mplot3d import art3d
from scipy.spatial import ConvexHull, Delaunay
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS
from basic_Matlab_to_Python.functions.basic_functions.Visualize_SingleVolumeData import visualize_single_volume_data
from basic_Matlab_to_Python.functions.basic_functions.Visualize_VolumeData import visualize_volume_data
from basic_Matlab_to_Python.functions.basic_functions.Visual_Dex_Convhulln import visual_dex_convhulln
from basic_Matlab_to_Python.functions.basic_functions.Visual_Slice import Visual_Slice
from basic_Matlab_to_Python.functions.basic_functions.Visual_Isosurface import Visual_Isosurface
import matplotlib.pyplot as plt


def ws_visualization(pop, Dex, Volume_Info, Flag_Info):
    print(Flag_Info['Slice_Flag'])
    Slice_Flag=Flag_Info['Slice_Flag']
    Bimanual=Flag_Info['Bimanual']
    Evaluation_Index=Flag_Info['Evaluation_Index']
    Slice=Flag_Info['Slice']
    Index_Num=Flag_Info['Index_Num']
    Bimanual_Vector= Flag_Info['Bimanual_Vector']



    switcher = {
        1: lambda: ws_case_1(Evaluation_Index, Bimanual, Index_Num, Dex, Bimanual_Vector),
        2: lambda: ws_case_2(Evaluation_Index, Bimanual, Volume_Info),
        3: lambda: ws_case_3(Evaluation_Index,Dex),
        4: lambda: ws_case_4(Evaluation_Index, Dex, Volume_Info),
        5: lambda: ws_case_5(Evaluation_Index, Slice_Flag, Slice, Volume_Info),
        6: lambda: ws_case_6(Evaluation_Index, Dex, Slice),
        7: lambda: ws_case_7(Evaluation_Index, Dex, Slice),
        8: lambda: ws_case_8(Evaluation_Index, Bimanual, Dex, Bimanual_Vector),

    }

    String_Out = switcher.get(pop, lambda: 'Invalid value')()
    return String_Out


def ws_case_1(Evaluation_Index, Bimanual, Index_Num, Dex, Bimanual_Vector):
    String_Out = f"{Evaluation_Index}Scatter"
    if Bimanual == 0:
        if Index_Num == 10:
            VisualWS(Dex)
        else:
            VisualWS(Dex, Index=Index_Num+3, evaluate='Local_Indices')
    else:
        if Index_Num == 10:
            VisualWS(Dex,robotnum= 'Bimanual', vector=Bimanual_Vector)
        else:
            VisualWS(Dex, Index=Index_Num+3, evaluate='Local_Indices',robotnum= 'Bimanual', vector=Bimanual_Vector)
    return String_Out


def ws_case_2(Evaluation_Index, Bimanual, Volume_Info):
    String_Out = f"{Evaluation_Index}Volume Data"
    if Bimanual == 0:
        TransferSingle = visualize_single_volume_data(Volume_Info['Boundary_Robot'], Volume_Info['V'], Volume_Info['Volume_Size'], Volume_Info['Precision'])
    else:
        TransferRight, TransferLeft, TransferDual = visualize_volume_data(Volume_Info['Boundary_Robot'], Volume_Info['VLeft_Robot'], Volume_Info['VRight_Robot'], Volume_Info['Volume_Size_Robot'], Volume_Info['Precision'],opt_visual= 'Scatter')
    return String_Out

# You would define the rest of the ws_case_X functions similar to the ones above, matching the functionality of the corresponding MATLAB case.
# Also, the visual_ws, visualize_single_volume_data, and visualize_volume_data functions should be defined to perform the operations needed in the corresponding ws_case_X functions.
def ws_case_3(Evaluation_Index, Dex):
    String_Out = f"{Evaluation_Index}Convhulln"
    Volume_R, Volume_L = visual_dex_convhulln(Dex, Dex)
    return String_Out

def ws_case_4(Evaluation_Index, Dex, Volume_Info):
    String_Out = f"{Evaluation_Index}Isosurface"
    A = Visual_Isosurface(Dex, Volume_Info['Boundary_Robot'], Volume_Info['Precision'])
    return String_Out

def ws_case_5(Evaluation_Index, Slice_Flag, Slice, Volume_Info):
    String_Out = f"{Evaluation_Index}Slice"
    if Slice_Flag[0] == 1:
        out = Visual_Slice(Volume_Info['V'], Volume_Info['Boundary_Robot'], Volume_Info['Precision'], X=Slice[0])
    if Slice_Flag[1] == 1:
        out = Visual_Slice(Volume_Info['V'], Volume_Info['Boundary_Robot'], Volume_Info['Precision'], Y=Slice[1])
    if Slice_Flag[2] == 1:
        out = Visual_Slice(Volume_Info['V'], Volume_Info['Boundary_Robot'], Volume_Info['Precision'], Z=Slice[2])
    return String_Out

def ws_case_6(Evaluation_Index, Dex, Slice):
    String_Out = f"{Evaluation_Index}Boundary"
    OUT = boundary_ws(Dex, Slice[3])
    return String_Out

def ws_case_7(Evaluation_Index, Dex, Slice):
    String_Out = f'{Evaluation_Index}Alphashape'
    # Compute the Delaunay triangulation of the point set
    tri = Delaunay(Dex[:, :3])

    fig = plt.figure()
    ax = fig.add_subplot(111, projection="3d")

    # Plot the triangles
    ax.add_collection3d(art3d.Poly3DCollection(Dex[tri.simplices,:3]))

    ax.set_xlim([Dex[:, 0].min(), Dex[:, 0].max()])
    ax.set_ylim([Dex[:, 1].min(), Dex[:, 1].max()])
    ax.set_zlim([Dex[:, 2].min(), Dex[:, 2].max()])

    plt.gca().set_aspect('equal', adjustable='box')
    plt.show()
    return String_Out

def ws_case_8(Evaluation_Index, Bimanual, Dex, Bimanual_Vector):
    String_Out = f"{Evaluation_Index}Reachable"
    if Bimanual == 0:
        VisualWS(Dex, 'Reachable')
    else:
        Bimanual_Vector = [-10, 0, 40, 10, 0, 40]
        VisualWS(Dex, 'Reachable', 'Bimanual', 'vector', Bimanual_Vector)
    return String_Out