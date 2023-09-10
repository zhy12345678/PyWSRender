import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection

def draw_ctcr(g, tube_end, r_tube, options):
    print(g)
    print(max(tube_end),np.shape(g)[0],np.shape(tube_end)[0],np.shape(r_tube)[0])
    if np.max(tube_end) > np.shape(g)[0] or np.shape(tube_end)[0] != np.shape(r_tube)[0]:
        raise ValueError("Dimension mismatch")

    curvelength = np.sum(np.linalg.norm(g[1:, 12:15] - g[:-1, 12:15], axis=1))
    numtubes = np.shape(tube_end)[0]
    print(type(numtubes))

    fig = plt.figure()
    fig.set_size_inches(12, 9)
    ax = fig.add_subplot(111, projection='3d')

    clearance = 0.03
    axis_lim = max(np.max(np.abs(g[:, 12])) + clearance, np.max(np.abs(g[:, 13])) + clearance, curvelength + clearance)
    ax.set_xlim([-axis_lim, axis_lim])
    ax.set_ylim([-axis_lim, axis_lim])
    ax.set_zlim([0, axis_lim])

    ax.set_xlabel('x (m)')
    ax.set_ylabel('y (m)')
    ax.set_zlabel('z (m)')
    ax.grid(True)
    ax.view_init(elev=30, azim=45)
    ax.set_box_aspect([1, 1, 1])

    radial_pts = 16
    tcirc = np.linspace(0, 2 * np.pi, radial_pts)
    col = np.linspace(0.2, 0.8, numtubes)
    alpha = 1

    for j in range(numtubes):
        if j == 0:
            starttube = 0
        else:
            starttube = tube_end[j - 1]

        endtube = tube_end[j]
        color = col[j] * np.array([1, 1, 1])

        basecirc = np.array([r_tube[j] * np.sin(tcirc), r_tube[j] * np.cos(tcirc), np.zeros(radial_pts), np.ones(radial_pts)])

        for i in range(starttube, endtube):
            basecirc_trans = np.reshape(g[i, :], (4, 4)).dot(basecirc)
            vertices = []
            for k in range(radial_pts):
                vertices.append([basecirc_trans[0, k], basecirc_trans[1, k], basecirc_trans[2, k]])
            vertices = np.array(vertices)
            vertices = np.vstack([vertices, vertices[0]])  # Close the loop
            ax.add_collection3d(Poly3DCollection([vertices], facecolors=[color], edgecolors='none', alpha=alpha))

    plt.show()

# Example usage
# g = np.random.rand(100, 16)  # Example data, replace with your actual data
# tube_end = np.array([20, 50, 80])  # Example data, replace with your actual data
# r_tube = np.array([0.02, 0.03, 0.02])  # Example data, replace with your actual data
# options = {'tipframe': True, 'baseframe': False, 'projections': False, 'baseplate': True}
# draw_ctcr(g, tube_end, r_tube, options)
