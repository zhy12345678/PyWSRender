import numpy as np
import matplotlib.pyplot as plt

# Define the joint angles range
theta1_range = np.linspace(0, 2*np.pi, 100)
theta2_range = np.linspace(0, 2*np.pi, 100)

# Initialize array to store Isotropic Index values
isotropic_values = np.zeros((len(theta1_range), len(theta2_range)))

# Define the Jacobian matrix for a 2-DOF planar manipulator
def jacobian(theta1, theta2):
    return np.array([
        [-np.sin(theta1) - np.sin(theta1 + theta2), -np.sin(theta1 + theta2)],
        [np.cos(theta1) + np.cos(theta1 + theta2), np.cos(theta1 + theta2)]
    ])

# Calculate the Isotropic Index for each joint configuration
for i, theta1 in enumerate(theta1_range):
    for j, theta2 in enumerate(theta2_range):
        J = jacobian(theta1, theta2)
        singular_values = np.linalg.svd(J, compute_uv=False)
        max_singular_value = np.max(singular_values)
        min_singular_value = np.min(singular_values)
        isotropic_values[i, j] = min_singular_value / max_singular_value

# Create a contour plot of the Isotropic Index workspace
plt.contourf(theta1_range, theta2_range, isotropic_values.T, levels=20, cmap='viridis')
plt.colorbar(label='Isotropic Index')
plt.xlabel('Joint Angle 1')
plt.ylabel('Joint Angle 2')
plt.title('Isotropic Index Workspace')
plt.show()
