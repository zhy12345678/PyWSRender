import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection, Line3DCollection
from basic_Matlab_to_Python.UseCases.ContinuumRobot.robot_independent_mapping import robot_independent_mapping
from basic_Matlab_to_Python.UseCases.ContinuumRobot.draw_ctcr import draw_ctcr

# Example parameters
kappa = [1/30e-3, 1/40e-3, 1/15e-3]
phi = [0, np.deg2rad(160), np.deg2rad(30)]
ell = [50e-3, 70e-3, 25e-3]
pts_per_seg = 30

g = robot_independent_mapping(kappa, phi, ell, pts_per_seg)
print(g)
draw_ctcr(g, [30, 60, 90], [2e-3, 1.5e-3, 1e-3], {})