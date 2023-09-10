from scipy.spatial import ConvexHull, Delaunay
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


def visual_dex_convhulln(Right, Left, visual='Off'):
    if visual not in ['Single', 'Bimanual', 'Off']:
        raise ValueError("Invalid value for 'visual' option")

    # Left volume
    P = Left[:, :3]
    hull = ConvexHull(P)
    Volume_L = hull.volume

    if visual in ['Single', 'Bimanual']:
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.add_collection3d(
            Poly3DCollection(hull.points[hull.simplices], alpha=0.3, linewidths=1, edgecolors='r', facecolor='green'))
        plt.show()

    # Right volume
    P = Right[:, :3]
    hull = ConvexHull(P)
    Volume_R = hull.volume

    if visual == 'Bimanual':
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        ax.add_collection3d(
            Poly3DCollection(hull.points[hull.simplices], alpha=0.3, linewidths=1, edgecolors='r', facecolor='green'))
        plt.show()

    Flag_Determine = 0

    if Flag_Determine == 1:
        Length = 40
        NX = 10000
        Rx = np.random.rand(NX, 1)
        Ry = np.random.rand(NX, 1)
        Rz = np.random.rand(NX, 1)
        Count_Point = 0

        tri = Delaunay(P)
        for i in range(NX):
            inflag = tri.find_simplex([Rx[i], Ry[i], Rz[i]]) >= 0
            if inflag == 1:
                Count_Point = Count_Point + 1

    return Volume_R, Volume_L
