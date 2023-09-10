import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def visualize_volume_data_all(boundary, v_group, volume_size, precision, index, **kwargs):
    # Default options
    opt = {
        'visual': 'Off'  # By default, no visualization
    }

    # Update with provided options
    opt.update(kwargs)

    robot_num = len(v_group)
    xminH, yminH, zminH = boundary[0,0], boundary[1,0], boundary[2,0]

    A, B, C = volume_size
    Total = A * B * C

    transfer_robot = {}
    v_dual_arm = np.zeros(volume_size)

    for P, v_left in v_group.items():
        num_lc = 0
        transfer = np.zeros((Total, 4))  # adjusted for potentially large size
        print(transfer)

        for i in range(A):
            for j in range(B):
                for k in range(C):
                    if v_left[i, j, k] != 0:
                        transfer[num_lc, 0] = xminH + precision * j
                        transfer[num_lc, 1] = yminH + precision * i
                        transfer[num_lc, 2] = zminH + precision * k
                        transfer[num_lc, 3] = v_left[i, j, k]
                        num_lc += 1

        v_dual_arm += v_left
        transfer_robot[P] = transfer[:num_lc]  # trim the array

    transfer_all = np.zeros((Total, 4))
    num_c = 0
    for i in range(A):
        for j in range(B):
            for k in range(C):
                if v_dual_arm[i, j, k] != 0:
                    transfer_all[num_c, 0] = xminH + precision * j
                    transfer_all[num_c, 1] = yminH + precision * i
                    transfer_all[num_c, 2] = zminH + precision * k
                    transfer_all[num_c, 3] = v_dual_arm[i, j, k]
                    num_c += 1
    transfer_all = transfer_all[:num_c]  # trim the array

    # Visualization
    if opt['visual'] == 'Seperate':
        for key, transfer in transfer_robot.items():
            plt.plot(transfer[:, 0], transfer[:, 1], transfer[:, 2], '*b')
    elif opt['visual'] == 'Bimanual':
        plt.plot(transfer_all[:, 0], transfer_all[:, 1], transfer_all[:, 2], '*y')
    elif opt['visual'] == 'Scatter':
        for key, transfer in transfer_robot.items():
            plt.scatter(transfer[:, 0], transfer[:, 1], transfer[:, 2], c=transfer[:, index-1], cmap=cm.viridis)
        plt.colorbar()

    plt.show()

    return transfer_robot, transfer_all
