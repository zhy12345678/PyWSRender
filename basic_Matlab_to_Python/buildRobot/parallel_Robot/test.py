import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Line3DCollection

# Base attachment points in hexagonal arrangement
base_points = np.array([
    [1, 0, 0],
    [0.5, np.sqrt(3)/2, 0],
    [-0.5, np.sqrt(3)/2, 0],
    [-1, 0, 0],
    [-0.5, -np.sqrt(3)/2, 0],
    [0.5, -np.sqrt(3)/2, 0]
])

# Platform attachment points (smaller hexagon)
platform_points = base_points / 2

# Initial cable lengths
cable_lengths = np.array([1.5, 1.5, 1.5, 1.5, 1.5, 1.5])

# Platform position and orientation
platform_pose = np.array([0, 0, 1.5])

def update_platform_points(platform_pose):
    return platform_points + platform_pose


def visualize(base_points, platform_points, platform_pose):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Plot base points
    ax.scatter(base_points[:, 0], base_points[:, 1], base_points[:, 2], c='b')

    # Plot platform points
    platform_points_moved = update_platform_points(platform_pose)
    ax.scatter(platform_points_moved[:, 0], platform_points_moved[:, 1], platform_points_moved[:, 2], c='r')

    # Connect cables
    for i in range(6):
        x_vals = [base_points[i, 0], platform_points_moved[i, 0]]
        y_vals = [base_points[i, 1], platform_points_moved[i, 1]]
        z_vals = [base_points[i, 2], platform_points_moved[i, 2]]
        ax.add_collection3d(Line3DCollection([list(zip(x_vals, y_vals, z_vals))], colors='k'))

    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    ax.set_zlim(0, 2)
    plt.show()



# Loop through different platform heights
for z in np.linspace(1.5, 0.5, 100):
    platform_pose[2] = z
    visualize(base_points, platform_points, platform_pose)



