import pybullet as p
import pybullet_data
import time

# Connect to the physics server
physicsClient = p.connect(p.GUI)

# Set Gravity (disabled for debugging)
p.setGravity(0, 0, 0)

# Add additional search paths
p.setAdditionalSearchPath(pybullet_data.getDataPath())



tableId = p.loadURDF("table/table.urdf")
p.resetBasePositionAndOrientation(tableId, [0, 0, 0], [0, 0, 0, 1])

# Load robot
robot_path = "G:\\United Kindom\\URDF\\ABB_Yumi.urdf"
robotId = p.loadURDF(robot_path, basePosition=[0, 0, 1])

# Set the camera view
p.resetDebugVisualizerCamera(cameraDistance=1.5, cameraYaw=0, cameraPitch=-40, cameraTargetPosition=[0,0,0.5])
while True:
    p.stepSimulation()
    time.sleep(1./240.)


