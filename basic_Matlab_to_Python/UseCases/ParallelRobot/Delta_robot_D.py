import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
R=150
r=50
L=300
La=600

def Zhengjie( theta1,theta2,theta3):
    theta1 = np.pi * theta1 / 180
    theta2 = np.pi * theta2 / 180
    theta3 = np.pi * theta3 / 180
    A1 = R + L * np.cos(theta1) - r
    B1 = 1
    C1 = L * np.sin(theta1)
    A2 = -(1 / 2) * (R + L * np.cos(theta2) - r)
    B2 = (np.sqrt(3) / 2) * (R + L * np.cos(theta2) - r)
    C2 = L * np.sin(theta2)
    A3 = -(1 / 2) * (R + L * np.cos(theta3) - r)
    B3 = -(np.sqrt(3) / 2) * (R + L * np.cos(theta3) - r)
    C3 = L * np.sin(theta3)
    D1 = (1 / 2) * (A2 * A2 - A1 * A1 + C2 * C2 - C1 * C1 + B2 * B2)
    A21 = A2 - A1
    C21 = C2 - C1
    D2 = (1 / 2) * (A3 * A3 - A1 * A1 + C3 * C3 - C1 * C1 + B3 * B3)
    A31 = A3 - A1
    C31 = C3 - C1
    E1 = (B3 * C21 - B2 * C31) / (A21 * B3 - A31 * B2)
    F1 = (B3 * D1 - B2 * D2) / (A21 * B3 - A31 * B2)
    E2 = (A31 * C21 - A21 * C31) / (A31 * B2 - A21 * B3)
    F2 = (A31 * D1 - A21 * D2) / (A31 * B2 - A21 * B3)
    a = E1 * E1 + E2 * E2 + 1
    b = 2 * E2 * F2 + 2 * C1 - 2 * E1 * (A1 - F1)
    c = (A1 - F1) * (A1 - F1) + F2 * F2 + C1 * C1 - La * La
    Z = (-b - np.sqrt(b * b - 4 * a * c)) / (2 * a)
    X = E1 * Z + F1
    Y = E2 * Z + F2
    return X,Y,Z

theta1 = np.arange(-22.6,87.1,5.485)
theta2 = np.arange(-22.6,87.1,5.485)
theta3 = np.arange(-22.6,87.1,5.485)

theta23, theta32 = np.meshgrid(theta2, theta3)  # 数据网格化

fig = plt.figure(1, figsize=(8,7))#画布大小
ax = fig.add_subplot()#生成子图
for item in theta1:
    X,Y,Z = Zhengjie(item,theta23,theta32)
    plt.scatter(X, Z, s=10, alpha=0.5)
    plt.xlabel('X')
    plt.ylabel('Z')
    ax.grid(True)
plt.show()


