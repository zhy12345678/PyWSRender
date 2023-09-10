import numpy as np
import matplotlib.pyplot as plt

def visualize_hr_volume(boundary, v_new, volume_size, precision, visual='Off'):
    xminH, yminH, zminH = boundary[0, 0], boundary[1, 0], boundary[2, 0]
    A, B, C = volume_size
    Pre = precision

    # Check Right
    numRC = 0
    transfer_right = np.zeros((A * B * C, 4))

    for i in range(A):
        for j in range(B):
            for k in range(C):
                if v_new[i, j, k] != 0:
                    transfer_right[numRC, 0] = xminH + Pre * (j - 1)
                    transfer_right[numRC, 1] = yminH + Pre * (i - 1)
                    transfer_right[numRC, 2] = zminH + Pre * (k - 1)
                    transfer_right[numRC, 3] = v_new[i, j, k]
                    numRC += 1
    print(transfer_right)


    if numRC != 0:
        origin_interact = transfer_right[:numRC]
        max_v = max(transfer_right[:numRC, 3])
        transfer_right[:numRC, 3] = transfer_right[:numRC, 3] / max_v
    else:
        print("error")
        transfer_right = np.zeros((1, 4))
        origin_interact = np.zeros((1, 4))

    # Check Transfer to Volume Data, Dual Arm
    if visual == 'Seperate':
        plt.plot(transfer_right[:numRC, 0], transfer_right[:numRC, 1], transfer_right[:numRC, 2], '*r')

    elif visual == 'Scatter':
        plt.scatter(transfer_right[:, 0], transfer_right[:, 1], transfer_right[:, 2], c=transfer_right[:, 3], s=5)
        plt.grid(False)
        plt.set_cmap('jet')
        plt.colorbar()
        plt.clim(0, 1)


    return transfer_right, origin_interact
