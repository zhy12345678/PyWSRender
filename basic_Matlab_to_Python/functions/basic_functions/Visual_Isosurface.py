import numpy as np
from scipy.interpolate import griddata
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from skimage.measure import marching_cubes


def Visual_Isosurface(Dex, Boundary, Precision):
    xmin, xmax = Boundary[0, 0], Boundary[0, 1]
    ymin, ymax = Boundary[1, 0], Boundary[1, 1]
    zmin, zmax = Boundary[2, 0], Boundary[2, 1]

    xx, yy, zz = np.meshgrid(np.arange(xmin, xmax + Precision, Precision),
                             np.arange(ymin, ymax + Precision, Precision),
                             np.arange(zmin, zmax + Precision, Precision))

    F = griddata(Dex[:, :3], Dex[:, 3], (xx, yy, zz), method='linear', fill_value=0)
    iso_surf3 = marching_cubes(F, 0.5, spacing=(Precision, Precision, Precision))
    verts, faces, _, _ = iso_surf3

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.add_collection3d(Poly3DCollection(verts[faces], alpha=0.2, facecolor='black', edgecolor='none'))
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

# Example usage:
# Assume Dex, Boundary, and Precision are defined
# Visual_Isosurface(Dex, Boundary, Precision)
