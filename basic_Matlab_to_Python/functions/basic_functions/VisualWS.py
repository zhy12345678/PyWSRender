'''
Input:
Dex: local indices distribution map

Option:
     opt.evaluate = {'Reachable','Local_Indices'};
     opt.robotnum = {'SingleArm','Bimanual'};
     opt.vector = [];
     opt.Index = [];
     opt.color = {'y','g','r','b'};
Output:
Out: default 1
Function:
Visualization and rendering of the workspace
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import griddata

from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial import ConvexHull
from matplotlib.patches import Polygon


def VisualWS(Dex, *args, **kwargs):
    opt = {
        'evaluate': ['Reachable', 'Local_Indices'],
        'robotnum': ['SingleArm', 'Bimanual'],
        'color': ['y', 'g', 'r', 'b'],
        'vector': [],
        'Index': []
    }
    opt.update(kwargs)
    out = 1
    print(opt)

    Vector = opt['vector'] \
        if len(opt['vector']) != 0 else [0, 0, 0, 0, 0, 0]

    #Vector = opt['vector'] if opt['vector'] else [0, 0, 0, 0, 0, 0]
    Num = opt['Index'] \
        if opt['Index'] else 4

    if opt['evaluate'] == 'Reachable':
        if opt['robotnum'] == 'SingleArm':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            print('到这了')
            ax.plot3D(Dex[:, 0], Dex[:, 1], Dex[:, 2], opt['color'],marker='*')
            # ax.scatter(Dex[:, 0], Dex[:, 1], Dex[:, 2], c='g', marker='*',label='single robot')
            # hull_right = ConvexHull(Dex)
            # for simplex in hull_right.simplices:
            #     simplex = np.append(simplex, simplex[0])  # Close the loop
            #     ax.plot3D(Dex[simplex, 0], Dex[simplex, 1], Dex[simplex, 2], 'b-', alpha=0.1)
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            Dex_Right = Dex[:, :3] + Vector[:3]
            Dex_Left = Dex[:, :3] + Vector[3:]

            hull_right = ConvexHull(Dex_Right)
            hull_left = ConvexHull(Dex_Left)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Plot the right side points
            ax.scatter(Dex_Right[:, 0], Dex_Right[:, 1], Dex_Right[:, 2], c=Dex_Right[:, 2], marker='*', label='Right Side')

            # Plot the left side points
            ax.scatter(Dex_Left[:, 0], Dex_Left[:, 1], Dex_Left[:, 2], c=Dex_Right[:, 2], marker='*', label='Left Side')

            # Plot the convex hull of the right side points
            for simplex in hull_right.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Right[simplex, 0], Dex_Right[simplex, 1], Dex_Right[simplex, 2], 'b-', alpha=0.1)

            # Plot the convex hull of the left side points
            for simplex in hull_left.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Left[simplex, 0], Dex_Left[simplex, 1], Dex_Left[simplex, 2], 'b-', alpha=0.1)

            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.legend()
            plt.show()

    elif opt['evaluate'] == 'Local_Indices':
        if opt['robotnum'] == 'SingleArm':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            print(Num)

            sc = ax.scatter(Dex[:, 0], Dex[:, 1], Dex[:, 2], c=Dex[:, Num+1], s=5, cmap='viridis')
            fig.colorbar(sc)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.grid(False)
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            sc1 = ax.scatter(Dex[:, 0] + Vector[0], Dex[:, 1] + Vector[1], Dex[:, 2] + Vector[5], c=Dex[:, Num], s=5,
                             cmap='viridis')
            sc2 = ax.scatter(Dex[:, 0] + Vector[3], Dex[:, 1] + Vector[4], Dex[:, 2] + Vector[5], c=Dex[:, Num], s=5,
                             cmap='viridis')
            fig.colorbar(sc1)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.grid(False)
            plt.show()

    return out
