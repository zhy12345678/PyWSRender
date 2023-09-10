from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def boundary_ws2(dex, value, **kwargs):
    nan_columns = np.any(np.isnan(dex), axis=0)
    dex_new = dex[:, ~nan_columns]
    _,count=dex_new.shape
    data = dex[:, :3]
    print("看这里",data)
    opt = {
        'color': {'r','b','g','off'},
    }
    opt.update(kwargs)
    # data = data[~np.isnan(data).any(axis=1)]
    hull = ConvexHull(data)
    print(hull)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if opt['color'] == 'r':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2],triangles=hull.simplices, edgecolor='r', facecolor='r', alpha=value)
    elif opt['color']== 'b':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2],triangles=hull.simplices, edgecolor='b', facecolor='b', alpha=value)
    elif opt['color'] == 'g':
        ax.plot_trisurf(data[:, 0], data[:, 1], data[:, 2],triangles=hull.simplices, edgecolor='g', facecolor='g', alpha=value)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')

    plt.show()

