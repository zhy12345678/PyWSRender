import numpy as np
import matplotlib.pyplot as plt


def compute_jacobian(theta1, theta2, l1=1, l2=1):
    """
    Compute the Jacobian for a simple 2-DOF planar robotic arm.
    """
    J = np.array([
        [-l1 * np.sin(theta1) - l2 * np.sin(theta1 + theta2), -l2 * np.sin(theta1 + theta2)],
        [l1 * np.cos(theta1) + l2 * np.cos(theta1 + theta2), l2 * np.cos(theta1 + theta2)]
    ])
    return J


theta1_range = np.linspace(0, np.pi, 100)  # Joint 1 angle range
theta2_range = np.linspace(0, np.pi, 100)  # Joint 2 angle range

manipulability_grid = np.zeros((100, 100))

for i, theta1 in enumerate(theta1_range):
    for j, theta2 in enumerate(theta2_range):
        # Compute the Jacobian at this configuration
        J = compute_jacobian(theta1, theta2)

        # Compute the manipulability measure (e.g., square root of determinant)
        manipulability = np.sqrt(np.linalg.det(J @ J.T))

        # Store in the grid
        manipulability_grid[i, j] = manipulability

plt.imshow(manipulability_grid, extent=[0, np.pi, 0, np.pi], origin='lower')
plt.colorbar(label='Manipulability')
plt.xlabel('Theta 1')
plt.ylabel('Theta 2')
plt.title('Manipulability Across Workspace')
plt.show()
