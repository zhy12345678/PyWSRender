import roboticstoolbox as rtb
from spatialmath import SE3
import matplotlib.pyplot as plt
import numpy as np
from ABB_Yumi import ABB_Yumi
from Articulated import Articulated
from Catersian import  Catersian
from Cylindrical import Cylindrical
from DefineRobot1 import define_robot1
from dVRK import dVRK
from HamlynCRM import HamlynCRM
from MIS import MIS
from Omni import Omni
from Puma560 import Puma560
from Redandant import Redandant
from SCARA import SCARA
from Spherical import Spherical
from Underactuated import Underactuated


from dVRK import dVRK
#dVRK=dVRK()
Robot= Spherical()
print(Robot.revolutejoints)
#print(puma)
#q= [np.pi, np.pi/4, np.pi/3, np.pi]#4
#q= [np.pi, np.pi/4, np.pi/3, np.pi,np.pi/2]#5
q= [0, 0, 0, 0, 0, 0]#6
#q= [np.pi, np.pi/4, np.pi/3, np.pi, np.pi/2, 0, 0]#7
#Te = puma.plot(q)  # forward kinematics
De = Robot.plot(q)

Tep = SE3.Trans(0.6, -0.3, 0.1) * SE3.OA([0, 1, 0], [0, 0, -1])
sol = Robot.ikine_LM(Tep)
print(sol)
q_pickup = sol[0]
print(Robot.fkine(q_pickup))
qt = rtb.jtraj(q, q_pickup, 50)
Robot.plot(qt.q, backend='pyplot', movie='panda1.gif')

input()









