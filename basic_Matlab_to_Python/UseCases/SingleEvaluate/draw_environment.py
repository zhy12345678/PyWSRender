import numpy as np
import matplotlib.pyplot as plt
from basic_Matlab_to_Python.buildRobot.dVRK import dVRK
import roboticstoolbox as rtb

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# Visualize the robot model
# qz = [0, 0, 0, 0, 0, 0]
# robot = dVRK()# Your robot model
# robot.plot(q=qz, block=False)
# print(rtb.robot)
# Add a frame
Desk_Length, Desk_Width, Desk_Height=0.6,0.4,0.5
frame_length = 0.2
Frame_Width= 0.4
Frame_Height=0.4
delta = Desk_Length / 10 #0.06

ax.plot([-Frame_Width / 2, Frame_Width / 2], [0, 0], [Frame_Height, Frame_Height], 'r', linewidth=3)
ax.plot([-Frame_Width / 2, Frame_Width / 2], [0, 0], [0, 0], 'r', linewidth=3)
ax.plot([-(Frame_Width / 2 - delta), -(Frame_Width / 2 - delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)
ax.plot([(Frame_Width / 2 - delta), (Frame_Width / 2 - delta)], [0, 0], [0, Frame_Height], 'r', linewidth=3)

# Add a table
ax.plot([Desk_Length/2, Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3,label='Table')
ax.plot([-Desk_Length/2, -Desk_Length/2], [Desk_Width, Desk_Width], [-Desk_Height, 0], 'k', linewidth=3)
ax.plot([-Desk_Length/2, -Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)
ax.plot([Desk_Length/2, Desk_Length/2], [0, 0], [-Desk_Height, 0], 'k', linewidth=3)

X = np.arange(0, Desk_Width, 0.01)
Y = np.arange(-Desk_Length/2, Desk_Length/2, 0.01)
X, Y = np.meshgrid(Y, X)
Z = X * 0
ax.plot_surface(X, Y, Z, color='blue', alpha=0.3,label='Table Surface')

# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
# Add legend
#ax.legend()
# Show the plot
plt.show()