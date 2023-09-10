import numpy as np


def scatter_volume_convert(dex_group, pre, boundary, volume_size, **kwargs):
    # Default options
    opt = {
        'mode': ['General', 'Manipulability', 'ICN', 'MSV']
    }

    # Update with provided options
    opt.update(kwargs)
    robot_num = len(dex_group)
    print(volume_size)

    a, b, c = volume_size
    v_all = np.zeros(volume_size)
    xminH, yminH, zminH = boundary[0, 0], boundary[1, 0], boundary[2, 0]

    v_group = {}

    for k in dex_group.keys():
        dex = dex_group[k]
        count = dex.shape[0]  # Assuming Dex is a 2D numpy array

        v_data = np.zeros(volume_size)
        aa, bb, cc = np.zeros(count), np.zeros(count), np.zeros(count)

        for i in range(count):
            aa[i] = round((dex[i, 0] - xminH) / pre)
            bb[i] = round((dex[i, 1] - yminH) / pre)
            cc[i] = round((dex[i, 2] - zminH) / pre)

            cc[i] = max(min(cc[i], c - 1), 0)  # clamping to [0, c-1]
            bb[i] = max(min(bb[i], a - 1), 0)  # clamping to [0, a-1]
            aa[i] = max(min(aa[i], b - 1), 0)  # clamping to [0, b-1]

            v_data[int(bb[i]), int(aa[i]), int(cc[i])] = dex[i, 3]

        v_group[k] = v_data
        v_all += v_data

    return v_all, v_group
