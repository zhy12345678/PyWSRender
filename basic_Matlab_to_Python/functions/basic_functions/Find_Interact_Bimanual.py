from matplotlib import pyplot as plt
from matplotlib import cm
import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.Scatter_Volume_Convert import scatter_volume_convert
from basic_Matlab_to_Python.functions.basic_functions.Visualize_VolumeData import visualize_volume_data
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws



def find_interact_bimanual(dex_group, boundary, volume_size, precision, visual='Off', color=['r', 'b']):
    # Assuming dex_group is a dictionary with keys being indices
    reach_group = {}
    print(dex_group)
    for i in range(1, 3):  # 1 and 2
        reach = np.copy(dex_group[i-1][:, :3])
        reach = np.column_stack((reach, np.ones(reach.shape[0])))
        reach_group[i] = reach

    v_all_reach, v_group_reach = scatter_volume_convert(reach_group, precision, boundary, volume_size)
    print(v_group_reach)
    transfer_right1, transfer_left1, transfer_dual = visualize_volume_data(boundary, v_group_reach[1], v_group_reach[2],
                                                                           volume_size, precision)

    interact = [row for row in transfer_dual if row[3] == 2]

    value = 0.1
    volume_all = boundary_ws(transfer_dual, value,color= 'r')

    if len(interact) == 0:
        volume_interact = 0
    else:
        volume_interact = boundary_ws(np.array(interact), value,color= 'r')

    # Visualization
    if visual == 'Seperate':
        plt.plot(interact[:, 0], interact[:, 1], interact[:, 2], '*r')
    elif visual == 'Scatter':
        plt.scatter(interact[:, 0], interact[:, 1], interact[:, 2], c=interact[:, 3], cmap=cm.viridis)
        plt.colorbar()
        plt.clim(0, 1)
        plt.gca().set_facecolor('w')

    plt.show()

    return volume_all, volume_interact
