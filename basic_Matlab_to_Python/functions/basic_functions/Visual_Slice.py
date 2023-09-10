import numpy as np
import matplotlib.pyplot as plt

def Visual_Slice(V, Boundary_Single, Precision, **kwargs):
    opt = {
        'X': None,
        'Y': None,
        'Z': None
    }
    opt.update(kwargs)

    xslice = opt['X'] if opt['X'] is not None else 0
    yslice = opt['Y']
    zslice = opt['Z']

    xminH, xmaxH = Boundary_Single[0, 0], Boundary_Single[0, 1]
    yminH, ymaxH = Boundary_Single[1, 0], Boundary_Single[1, 1]
    zminH, zmaxH = Boundary_Single[2, 0], Boundary_Single[2, 1]

    X, Y, Z = np.meshgrid(np.arange(xminH, xmaxH + Precision, Precision),
                          np.arange(yminH, ymaxH + Precision, Precision),
                          np.arange(zminH, zmaxH + Precision, Precision))

    plt.figure()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Slice Visualization')

    if xslice is not None:
        plt.subplot(131)
        plt.imshow(V[:, :, xslice], extent=[yminH, ymaxH, zminH, zmaxH], origin='lower', aspect='auto')
        plt.colorbar()
        plt.title('X Slice at X=' + str(X[0, 0, xslice]))

    if yslice is not None:
        plt.subplot(132)
        plt.imshow(V[:, yslice, :], extent=[xminH, xmaxH, zminH, zmaxH], origin='lower', aspect='auto')
        plt.colorbar()
        plt.title('Y Slice at Y=' + str(Y[0, yslice, 0]))

    if zslice is not None:
        plt.subplot(133)
        plt.imshow(V[zslice, :, :], extent=[xminH, xmaxH, yminH, ymaxH], origin='lower', aspect='auto')
        plt.colorbar()
        plt.title('Z Slice at Z=' + str(Z[zslice, 0, 0]))

    plt.show()

# Example usage:
# Assume V, Boundary_Single, and Precision are defined
# Visual_Slice(V, Boundary_Single, Precision, X=10, Y=20, Z=None)
