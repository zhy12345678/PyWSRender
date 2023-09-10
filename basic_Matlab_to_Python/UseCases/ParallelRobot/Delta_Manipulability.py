import numpy as np
import math
import matplotlib.pyplot as plt

R = 150
r = 50
L = 300
La = 600

def Fanjie(x,y,z):
    A1 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) - 2 * x * (R - r)) / (2 * L)
    B1 = -(R - r - x)
    C1 = z
    A2 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) + (x - math.sqrt(3) * y) * (R - r)) / L
    B2 = -2 * (R - r) - (x - math.sqrt(3) * y)
    C2 = 2*z
    A3 = (x * x + y * y + z * z + L * L - La * La + (R - r) * (R - r) + (x + math.sqrt(3) * y) * (R - r)) / L
    B3 = -2 * (R - r)-(x + math.sqrt(3) * y)
    C3 = 2 * z
    K1 = A1 + B1
    U1 = 2 * C1
    V1 = A1 - B1
    K2 = A2 + B2
    U2 = 2 * C2
    V2 = A2 - B2
    K3 = A3 + B3
    U3 = 2 * C3
    V3 = A3 - B3
    theta1 = 2*math.degrees(math.atan((-U1- math.sqrt(U1*U1 - 4 * K1 * V1)) / (2 * K1)))
    theta2 = 2*math.degrees(math.atan((-U2 - math.sqrt(U2 * U2 - 4 * K2 * V2)) / (2 * K2)))
    theta3 = 2*math.degrees(math.atan((-U3 - math.sqrt(U3 * U3 - 4 * K3 * V3)) / (2 * K3)))
    print(theta1)
    print(theta2)
    print(theta3)
    return theta1,theta2,theta3

def calculate_jacobian(X, Y, Z):
    theta1,theta2,theta3=Fanjie(X,Y,Z)


    J = np.array([
        [-L * np.sin(theta1), -L * np.sin(theta2 + theta3), -L * np.sin(theta2 + theta3)],
        [L * np.cos(theta1), L * np.cos(theta2 + theta3), L * np.cos(theta2 + theta3)],
        [0, -L * np.cos(theta2 + theta3), -L * np.cos(theta2 + theta3)]
    ])

    return J


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


# theta1 = -22.6+109.7*np.random.rand(1, 400)#从-22.6到87.1，步长为5.485，生成数据
# theta2 = -22.6+109.7*np.random.rand(1, 400)
# theta3 = -22.6+109.7*np.random.rand(1, 400)

theta1 = np.arange(-22.6, 87.1, 5.485)
theta2 = np.arange(-22.6, 87.1, 5.485)
theta3 = np.arange(-22.6, 87.1, 5.485)
theta23, theta32 = np.meshgrid(theta2, theta3)
fig = plt.figure(1, figsize=(8, 7))
ax = fig.add_subplot(111, projection='3d')
manipulability_values = []  # Array to store manipulability values

X_values = []
Y_values = []
Z_values = []
for item in theta1:
    X_row = []
    Y_row = []
    Z_row = []
    manipulability_row = []
    for i in range(len(theta2)):
        manipulability_row.append([])
        for j in range(len(theta3)):
            X, Y, Z = Zhengjie(item, theta23[i, j], theta32[i, j])
            X_row.append(X)
            Y_row.append(Y)
            Z_row.append(Z)
            # Calculate the Jacobian matrix
            J = calculate_jacobian(X, Y, Z)
            # Calculate manipulability
            manipulability = np.sqrt(np.linalg.det(np.dot(J, J.T)))
            manipulability_row[i].append(manipulability)
    X_values.append(X_row)
    Y_values.append(Y_row)
    Z_values.append(Z_row)
    manipulability_values.append(manipulability_row)

manipulability_values = np.array(manipulability_values)

print(manipulability_values)
# Create a 3D scatter plot with color-coded manipulability
X=X_values
Y=Y_values
Z=Z_values
manipulability_values=manipulability_values.flatten()
print(X)
print(Y)
print(Z)
print(manipulability_values)
sc = ax.scatter(X, Y,Z, c=manipulability_values,s=5,cmap='viridis')
fig.colorbar(sc)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.grid(True)
# sc1 = ax.scatter(Dex[:, 0] + Vector[0], Dex[:, 1] + Vector[1], Dex[:, 2] + Vector[2], c=Dex[:, Num-2], s=5,
#                              cmap='viridis')

plt.show()