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


def VisualWS2(Dex1,Dex2, *args, **kwargs):
    opt = {
        'evaluate': ['Reachable', 'Local_Indices'],
        'robotnum': ['SingleArm', 'Bimanual'],
        'color': ['y', 'g', 'r', 'b'],
        'vector1': [],
        'vector2':[],
        'Index': []
    }
    opt.update(kwargs)
    out = 1
    print(opt)

    Vector1 = opt['vector1'] \
        if len(opt['vector1']) != 0 else [0, 0, 0, 0, 0, 0]
    Vector2 = opt['vector2'] \
        if len(opt['vector2']) != 0 else [0, 0, 0, 0, 0, 0]

    #Vector = opt['vector'] if opt['vector'] else [0, 0, 0, 0, 0, 0]
    Num = opt['Index'] \
        if opt['Index'] else 4

    if opt['evaluate'] == 'Reachable':
        if opt['robotnum'] == 'SingleArm':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            print('到这了')
            ax.plot3D(Dex1[:, 0], Dex1[:, 1], Dex1[:, 2], opt['color'],marker='*')
            ax.plot3D(Dex2[:, 0], Dex2[:, 1], Dex2[:, 2], opt['color'], marker='*')
            # ax.scatter(Dex[:, 0], Dex[:, 1], Dex[:, 2], c='g', marker='*',label='single robot')
            # hull_right = ConvexHull(Dex)
            # for simplex in hull_right.simplices:
            #     simplex = np.append(simplex, simplex[0])  # Close the loop
            #     ax.plot3D(Dex[simplex, 0], Dex[simplex, 1], Dex[simplex, 2], 'b-', alpha=0.1)
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            Dex_Right1 = Dex1[:, :3] + Vector1[:3]
            Dex_Left1 = Dex1[:, :3] + Vector1[3:]
            Dex_Right2 = Dex2[:, :3] + Vector2[:3]
            Dex_Left2 = Dex2[:, :3] + Vector2[3:]

            hull_right1 = ConvexHull(Dex_Right1)
            hull_left1 = ConvexHull(Dex_Left1)
            hull_right2 = ConvexHull(Dex_Right2)
            hull_left2 = ConvexHull(Dex_Left2)

            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')

            # Plot the right side points
            ax.scatter(Dex_Right1[:, 0], Dex_Right1[:, 1], Dex_Right1[:, 2], c='g', marker='*', label='Right Side')
            ax.scatter(Dex_Right2[:, 0], Dex_Right2[:, 1], Dex_Right2[:, 2], c='r', marker='*', label='Right Side')

            # Plot the left side points
            ax.scatter(Dex_Left1[:, 0], Dex_Left1[:, 1], Dex_Left1[:, 2], c='g', marker='*', label='Left Side')
            ax.scatter(Dex_Left2[:, 0], Dex_Left2[:, 1], Dex_Left2[:, 2], c='r', marker='*', label='Left Side')

            # Plot the convex hull of the right side points
            for simplex in hull_right1.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Right1[simplex, 0], Dex_Right1[simplex, 1], Dex_Right1[simplex, 2], 'b-', alpha=0.1)
            for simplex in hull_right2.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Right2[simplex, 0], Dex_Right2[simplex, 1], Dex_Right2[simplex, 2], 'b-', alpha=0.1)
            # Plot the convex hull of the left side points
            for simplex in hull_left1.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Left1[simplex, 0], Dex_Left1[simplex, 1], Dex_Left1[simplex, 2], 'b-', alpha=0.1)
            for simplex in hull_left2.simplices:
                simplex = np.append(simplex, simplex[0])  # Close the loop
                ax.plot3D(Dex_Left2[simplex, 0], Dex_Left2[simplex, 1], Dex_Left2[simplex, 2], 'b-', alpha=0.1)

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

            sc = ax.scatter(Dex1[:, 0], Dex1[:, 1], Dex1[:, 2], c=Dex1[:, Num+1], s=5, cmap='viridis')
            sc = ax.scatter(Dex2[:, 0], Dex2[:, 1], Dex2[:, 2], c=Dex2[:, Num + 1], s=5, cmap='viridis')
            fig.colorbar(sc)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.grid(False)
            plt.show()
        elif opt['robotnum'] == 'Bimanual':
            fig = plt.figure()
            ax = fig.add_subplot(111, projection='3d')
            sc1 = ax.scatter(Dex1[:, 0] + Vector1[0], Dex1[:, 1] + Vector1[1], Dex1[:, 2] + Vector1[5], c=Dex1[:, Num], s=5,
                             cmap='viridis')
            sc2 = ax.scatter(Dex1[:, 0] + Vector1[3], Dex1[:, 1] + Vector1[4], Dex1[:, 2] + Vector1[5], c=Dex1[:, Num], s=5,
                             cmap='viridis')
            sc1 = ax.scatter(Dex2[:, 0] + Vector2[0], Dex2[:, 1] + Vector2[1], Dex2[:, 2] + Vector2[5], c=Dex2[:, Num], s=5,
                             cmap='viridis')
            sc2 = ax.scatter(Dex2[:, 0] + Vector2[3], Dex2[:, 1] + Vector2[4], Dex2[:, 2] + Vector2[5], c=Dex2[:, Num], s=5,
                             cmap='viridis')
            fig.colorbar(sc1)
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            ax.grid(False)
            plt.show()

    return out
