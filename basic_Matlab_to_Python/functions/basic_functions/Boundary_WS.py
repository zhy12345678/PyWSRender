from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def boundary_ws(dex, value, **kwargs):
    data = dex[:, :3]
    print(data)
    opt = {
        'color': {'r','b','g','off'},
    }
    opt.update(kwargs)

    hull = ConvexHull(data)
    print(hull)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if opt['color'] == 'r':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='r', facecolor='r', alpha=value)
    elif opt['color']== 'b':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='b', facecolor='b', alpha=value)
    elif opt['color'] == 'g':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2], triangles=hull.simplices, edgecolor='g', facecolor='g', alpha=value)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

