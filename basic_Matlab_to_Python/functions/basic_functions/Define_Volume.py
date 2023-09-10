import numpy as np


def define_volume(dex_group, pre):
    robot_num = len(dex_group)

    boundary = np.zeros((3, 2))
    xmin, xmax = [], []
    ymin, ymax = [], []
    zmin, zmax = [], []

    # Loop through each numpy array in the dex_group dictionary
    for key in dex_group:
        dex = dex_group[key]

        xmin.append(np.min(dex[:, 0]))
        xmax.append(np.max(dex[:, 0]))

        ymin.append(np.min(dex[:, 1]))
        ymax.append(np.max(dex[:, 1]))

        zmin.append(np.min(dex[:, 2]))
        zmax.append(np.max(dex[:, 2]))

    x_min, x_max = min(xmin), max(xmax)
    y_min, y_max = min(ymin), max(ymax)
    z_min, z_max = min(zmin), max(zmax)

    boundary[0] = [x_min, x_max]
    boundary[1] = [y_min, y_max]
    boundary[2] = [z_min, z_max]

    x_mesh, y_mesh, z_mesh = np.meshgrid(np.arange(x_min, x_max, pre),
                                         np.arange(y_min, y_max, pre),
                                         np.arange(z_min, z_max, pre))

    volume_size = x_mesh.shape  # since x_mesh, y_mesh, and z_mesh have the same shape

    return boundary, volume_size

