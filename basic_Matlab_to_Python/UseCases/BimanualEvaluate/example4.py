'''
 Load Self-defined robot local indices distribution map and visualize
'''
import os
import sys

import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.VisualWS import VisualWS
# folder = "G:\\United Kindom\\毕设\\pyqt_design\\basic_Matlab_to_Python\\functions\\basic_functions"
# file_name = '\\ws_data.txt'
# path = folder + file_name

#path="G:\\United Kindom\\毕设\\pyqt_design\\basic_Matlab_to_Python\\UseCases\\define_robot\\ws_data.txt"
current_folder = os.getcwd()
sys.path.append(current_folder)
parent_directory = os.path.dirname(current_folder)
path=parent_directory+'\define_robot\ws_data.txt'
print(path)

# Initialize an empty list to store the numeric values
# data_list = []
#
# # Open the file and read its content line by line
# with open(path, 'r') as file:
#     for line in file:
#         # Assuming the numbers are space-separated
#         numbers = line.strip().split()
#         # Convert each element to a float and add it to the list
#         for num in numbers:
#             data_list.append(float(num))
#
# # Convert the list to a NumPy array if needed
# data_list = np.array(data_list)
data_array = np.loadtxt(path)
# Now you can use the 'data_array' variable to work with the numeric data
print(data_array)

def plot_3d_data(data, index):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], c='b')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    if index != 1:
        data[:, :3] *= 100
        VisualWS(data, index, 'Local_Indices')
# Index value (change accordingly)
Index = 4

# Plot 3D data based on the value of Index
if Index == 1:
    plot_3d_data(data_array, Index)
else:
    plot_3d_data(data_array, Index)

plt.show()