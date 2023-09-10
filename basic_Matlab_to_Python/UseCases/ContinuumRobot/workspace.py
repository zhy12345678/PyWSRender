import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 参数
N = 40000
length = 400  # 弯曲单元长度
points_segment1 = []
points_segment2 = []
points_segment3 = []

# 前向运动学转换
def forward_kinematics(theta, alpha, segments=3):
    coords = [(0, 0, 0)]
    for i in range(segments):
        x = coords[-1][0] + length * np.sin(theta[i]) * np.cos(alpha[i])
        y = coords[-1][1] + length * np.sin(theta[i]) * np.sin(alpha[i])
        z = coords[-1][2] + length * np.cos(theta[i])
        coords.append((x, y, z))
    return coords

# 随机采样并转换为笛卡尔坐标
for _ in range(N):
    theta = np.random.uniform(0, np.pi/2, 3)  # 三段弯曲角
    alpha = np.random.uniform(0, 2*np.pi, 3)  # 三段旋转角
    coords = forward_kinematics(theta, alpha)
    points_segment1.append(coords[1])
    points_segment2.append(coords[2])
    points_segment3.append(coords[3])

# 绘制
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# ax.scatter(*zip(*points_segment1), s=1, c='r', label='Segment 1')
# ax.scatter(*zip(*points_segment2), s=1, c='g', label='Segment 2')
# ax.scatter(*zip(*points_segment3), s=1, c='b', label='Segment 3')

s1 = ax.scatter(*zip(*points_segment1), s=1, c=[p[2] for p in points_segment1], cmap='viridis', label='Segment 1')
s2 = ax.scatter(*zip(*points_segment2), s=1, c=[p[2] for p in points_segment2], cmap='viridis', label='Segment 2')
s3 = ax.scatter(*zip(*points_segment3), s=1, c=[p[2] for p in points_segment3], cmap='viridis', label='Segment 3')
cbar = fig.colorbar(s3, ax=ax)
cbar.set_label('Z-value')

# fig, ax = plt.subplots()

# 使用X和Z坐标绘制点
# ax.scatter([p[0] for p in points_segment1], [p[2] for p in points_segment1], s=1, c='r', label='Segment 1')
# ax.scatter([p[0] for p in points_segment2], [p[2] for p in points_segment2], s=1, c='g', label='Segment 2')
# ax.scatter([p[0] for p in points_segment3], [p[2] for p in points_segment3], s=1, c='b', label='Segment 3')


ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_ylabel('Z')
ax.legend()
ax.grid(False)
ax.set_facecolor('white')
plt.show()
