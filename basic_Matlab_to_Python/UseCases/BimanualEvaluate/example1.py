"""
Load Existing Local indices distribution map and visualze
"""
import os
import sys
import numpy as np
import matplotlib.pyplot as plt #是python的专门的画图包3D
import scipy.io
from mpl_toolkits.mplot3d import Axes3D

current_folder = os.getcwd()
sys.path.append(current_folder)
parent_directory = os.path.dirname(current_folder)
pwd=parent_directory+'\Data_Dex'
print(pwd)

#pwd = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex'
os.chdir(pwd)
sys.path.append(pwd)

file_name= pwd+'\dVRK3375.csv'
#file_name = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex\dVRK3375.csv'
# file = np.load(file_name,allow_pickle=True)
with open(file_name, 'r') as file:
    lines = file.readlines()
data_list = []
for line in lines:
    values = line.strip().split(',')
    floats = [float(value) for value in values]
    data_list.append(floats)
dex_data = np.array(data_list)
dex = dex_data
dex_left = dex.copy()
dex_left[:, 1] += 0.2 #作为index的副本创建，第二列增加0.2

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d') #创建带有3D子图的图形。
ax.scatter(dex[:, 0], dex[:, 1], dex[:, 2], c=dex[:, 3], s=5, cmap='viridis')
ax.scatter(dex_left[:, 0], dex_left[:, 1], dex_left[:, 2], c=dex_left[:, 8], s=5)
ax.set_xlabel('X') #设定坐标轴的用法
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d(np.min(dex[:, 0]), np.max(dex[:, 0])) #根据限制进行绘图
ax.set_ylim3d(np.min(dex[:, 1]), np.max(dex[:, 1]))
ax.set_zlim3d(np.min(dex[:, 2]), np.max(dex[:, 2]))
print(np.min(dex[:,8]),np.max(dex[:,8]))
fig.colorbar(ax.get_children()[0], ax=ax)
# plt.plot([1,2,3])
# plt.show()




file_name= pwd+'\Spherical3375.csv'
#file_name = r'G:\United Kindom\毕设\pyqt_design\basic_Matlab_to_Python\UseCases\Data_Dex\Spherical3375.csv'
# file = np.load(file_name,allow_pickle=True)
with open(file_name, 'r') as file:
    lines = file.readlines()
data_list = []
for line in lines:
    values = line.strip().split(',')
    floats = [float(value) for value in values]
    data_list.append(floats)
dex_data = np.array(data_list)
print(dex_data)
dex = dex_data
dex_left = dex.copy()
dex_left[:, 1] += 0.2

fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.scatter(dex[:, 0], dex[:, 1], dex[:, 2], c=dex[:, 3], s=5, cmap='viridis')
ax.scatter(dex_left[:, 0], dex_left[:, 1], dex_left[:, 2], c=dex_left[:, 8], s=5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim3d(np.min(dex[:, 0]), np.max(dex[:, 0]))
ax.set_ylim3d(np.min(dex[:, 1]), np.max(dex[:, 1]))
ax.set_zlim3d(np.min(dex[:, 2]), np.max(dex[:, 2]))
print(np.min(dex[:,8]),np.max(dex[:,8]))
fig.colorbar(ax.get_children()[0], ax=ax)

plt.show()
