import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from mayavi import mlab
import plotly.graph_objects as go

def scatter_to_volume(Dex, Pre, BaseRight, BaseLeft, **kwargs):
    opt = {
        'save': ['Save', 'UnSave'],
        'visual': ['Visual_Off', 'Visual_On'],
        'bimanual': 'BimanualRobot'
    }
    opt.update(kwargs)

    bimanual = opt['bimanual']
    if bimanual == 'BimanualArm':
        Left = [Dex[:, 0] - 0.20, Dex[:, 1], Dex[:, 2], Dex[:, 3]]
        Right = [Dex[:, 0], Dex[:, 1], Dex[:, 2], Dex[:, 3]]
    elif bimanual == 'BimanualRobot':
        Left = [Dex[:, 0] + BaseLeft[0], Dex[:, 1] + BaseLeft[1], Dex[:, 2] + BaseLeft[2], Dex[:, 3]]
        Right = [Dex[:, 0] + BaseRight[0], Dex[:, 1] + BaseRight[1], Dex[:, 2] + BaseRight[2], Dex[:, 3]]
    Left=np.array(Left).T
    Right=np.array(Right).T
    count, _ = Right.shape
    Boundary = np.zeros((3, 2))

    xminH, xmaxH = np.min(Left[:, 0]), np.max(Right[:, 0])
    yminH, ymaxH = np.min(Left[:, 1]), np.max(Left[:, 1])
    zminH, zmaxH = np.min(Left[:, 2]), np.max(Left[:, 2])

    Boundary[0, 0] = xminH
    Boundary[0, 1] = xmaxH
    Boundary[1, 0] = yminH
    Boundary[1, 1] = ymaxH
    Boundary[2, 0] = zminH
    Boundary[2, 1] = zmaxH

    xxH, yyH, zzH = np.meshgrid(np.arange(xminH, xmaxH , Pre),
                                np.arange(yminH, ymaxH , Pre),
                                np.arange(zminH, zmaxH , Pre))

    A, B, C = xxH.shape
    Volume_Size = [A, B, C]
    print(A,B,C)

    VLeft = np.zeros(xxH.shape)
    VRight = np.zeros(xxH.shape)




    for i in range(count):

        aa = np.round((Left[i, 0] - xminH) / Pre).astype(int)
        aaR = np.round((Right[i, 0] - xminH) / Pre).astype(int)
        bb = np.round((Left[i, 1] - yminH) / Pre).astype(int)
        cc = np.round((Left[i, 2] - zminH) / Pre).astype(int)



        cc = np.clip(cc, 1, C)
        bb = np.clip(bb, 1, A)
        aaR = np.clip(aaR, 1, B)
        aa = np.clip(aa, 1, B)
        print("Sizes:", VLeft.shape, bb.shape, aa.shape, cc.shape)
        print("Indices:", bb, aa, cc)

        VLeft[bb-1, aa-1, cc-1] = Left[i, 3]
        VRight[bb-1, aaR-1, cc-1] = Right[i, 3]
        k=VLeft.size
        j=VRight.size

    VDualArm = VLeft + VRight



    visual = opt['visual']
    if visual == 'Visual_Off':
        out = 'Visual Off'
    elif visual == 'Visual_On':
        iso_val = 0.5
        # iso_surface_left = go.Isosurface(
        #     x=xxH.flatten(),
        #     y=yyH.flatten(),
        #     z=zzH.flatten(),
        #     value=VLeft.flatten(),
        #     isomin=iso_val,
        #     isomax=iso_val,
        #     opacity=0.3,
        #     surface_count=1,
        #     colorbar=dict(title='VLeft'),
        #     colorscale='Greens'
        # )
        #
        # # Create the isosurface for VRight
        # iso_surface_right = go.Isosurface(
        #     x=xxH.flatten(),
        #     y=yyH.flatten(),
        #     z=zzH.flatten(),
        #     value=VRight.flatten(),
        #     isomin=iso_val,
        #     isomax=iso_val,
        #     opacity=0.3,
        #     surface_count=1,
        #     colorbar=dict(title='VRight'),
        #     colorscale='Greens'
        # )
        #
        # # Create the figure and add the isosurfaces
        # fig = go.Figure()
        # fig.add_trace(iso_surface_left)
        # fig.add_trace(iso_surface_right)
        #
        # fig.show()

    return VDualArm,VLeft,VRight,Boundary,Volume_Size
