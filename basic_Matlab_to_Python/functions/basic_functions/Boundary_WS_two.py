from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



def boundary_ws_two(dex1,dex2, value, **kwargs):
    data1 = dex1[:, :3]
    data2 = dex2[:, :3]
    print(data1,data2)
    opt = {
        'color': {'r','b','g','off'},
    }
    opt.update(kwargs)

    hull1 = ConvexHull(data1)
    hull2 = ConvexHull(data2)
    print(hull1)
    print(hull2)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    if opt['color'] == 'r':
        ax.plot_trisurf(data1[:, 0], data1[:, 1], data1[:, 2], triangles=hull1.simplices, edgecolor='r', facecolor='r', alpha=value)
        ax.plot_trisurf(data2[:, 0], data2[:, 1], data2[:, 2], triangles=hull2.simplices, edgecolor='r', facecolor='r',
                        alpha=value)
    elif opt['color']== 'b':
        ax.plot_trisurf(data1[:, 0], data1[:, 1], data1[:, 2], triangles=hull1.simplices, edgecolor='b', facecolor='b', alpha=value)
        ax.plot_trisurf(data2[:, 0], data2[:, 1], data2[:, 2], triangles=hull2.simplices, edgecolor='b', facecolor='b',
                        alpha=value)
    elif opt['color'] == 'g':
        ax.plot_trisurf(data1[:, 0], data1[:, 1], data1[:, 2], triangles=hull1.simplices, edgecolor='g', facecolor='g', alpha=value)
        ax.plot_trisurf(data2[:, 0], data2[:, 1], data2[:, 2], triangles=hull2.simplices, edgecolor='g', facecolor='g',
                        alpha=value)






