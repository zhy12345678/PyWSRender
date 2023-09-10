#from Puma560 import Puma560
from ABB_Yumi import ABB_Yumi
from Articulated import Articulated
from Catersian import Catersian
from Cylindrical import Cylindrical
from DefineRobot1 import define_robot1
from DefineRobot2 import define_robot2
from dVRK import dVRK
from HamlynCRM import HamlynCRM
from MIS import MIS
from Omni import Omni
from Omni2 import Omni
from Puma560 import Puma560
from Redandant import Redandant
from SCARA import SCARA
from Spherical import Spherical
from Underactuated import Underactuated
#from basic_Matlab_to_Python.functions.basic_functions.Draw_environment import draw_environment
from basic_Matlab_to_Python.functions.basic_functions.Robot_map import robot_map



# Import the required modules
import roboticstoolbox as rtb

# Create an instance of the Puma560 robot

ABB_Yumi=ABB_Yumi()
Articulated=Articulated()
Catersian=Catersian()
Cylindrical=Cylindrical()
DefineRobot1=define_robot1()

dVRK=dVRK()
HamlynCRM=HamlynCRM()
MIS=MIS()
Omni2=Omni()
puma = Puma560()
Redandant=Redandant()
SCARA=SCARA()
Spherical=Spherical()
Underactuated=Underactuated()




qz = [0, 0, 0,0,0,0]

# Plot the robot
#ABB_Yumi.plot(q=qz,block=True)
MIS.plot(q=qz,block=True)
#print(rtb.dVRK)
# Env_Type='Desk_On'
# draw_environment(Env_Type)


# 'block=True' is optional, it keeps the plot window open until you close it manually
