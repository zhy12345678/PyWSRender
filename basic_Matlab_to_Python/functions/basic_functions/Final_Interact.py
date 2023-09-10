from matplotlib import pyplot as plt
from basic_Matlab_to_Python.functions.basic_functions.Scatter_Volume_Convert import scatter_volume_convert
from basic_Matlab_to_Python.functions.basic_functions.Boundary_WS import boundary_ws
from basic_Matlab_to_Python.functions.basic_functions.Visualize_HR_Volume import visualize_hr_volume
import numpy as np
from mayavi import mlab
import plotly.express as px



def final_interact(dex_group, boundary, volume_size, precision, mode='General', visual='None'):
    # Default options
    options = {
        'mode': 'General',  # Default mode is 'General'
        'visual': 'None'  # Default visual mode is 'None'
    }

    # Parse provided options
    options['mode'] = mode
    options['visual'] = visual

    # Reach group assignment
    reach_group = dex_group
    print(dex_group)
    _, v_group_reach = scatter_volume_convert(reach_group, precision, boundary, volume_size)

    # Assuming that v_group_reach is a dictionary, let's get the data
    new_v = v_group_reach[1] * v_group_reach[2]

    transfer_new, origin_interact = visualize_hr_volume(boundary, new_v, volume_size, precision)
    print(transfer_new,origin_interact)
    with open('output.txt', 'w') as f:
        for item in transfer_new:
            f.write("%s\n" % item)
    with open('output1.txt', 'w') as f:
        for item in origin_interact:
            f.write("%s\n" % item)

    value = 0.1

    # Depending on the mode option
    if options['mode'] == 'General':
        volume_all = boundary_ws(transfer_new, value, 'off')
    elif options['mode'] == 'Local_Indices':
        volume_all = np.mean(transfer_new[:, 3])

    # Visualization
    if options['visual'] == 'Scatter':
        # mlab.points3d(transfer_new[:, 0], transfer_new[:, 1], transfer_new[:, 2], transfer_new[:, 3])
        # mlab.show()
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')  # Create a 3D subplot
        scatter = ax.scatter(transfer_new[:, 0], transfer_new[:, 1], transfer_new[:, 2], c=transfer_new[:, 3])
        plt.colorbar(scatter)  # Show colorbar
        # plt.scatter(transfer_new[:, 0], transfer_new[:, 1], transfer_new[:, 2], c=transfer_new[:, 3])
        # plt.colorbar()
    elif options['visual'] == 'Show':
        # Assuming boundary_ws creates some kind of visualization
        boundary_ws(transfer_new, value, 'g')

    plt.show()

    return volume_all, new_v, transfer_new
