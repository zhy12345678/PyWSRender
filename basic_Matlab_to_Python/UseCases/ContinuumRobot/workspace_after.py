import numpy as np
import matplotlib.pyplot as plt

# 参数
N = 20000
length = 200
points_segment1 = []
points_segment2 = []
points_segment3 = []


def forward_kinematics(theta, alpha, segments=3):
    coords = [(0, 0, 0)]
    for i in range(segments):
        x = coords[-1][0] + length * np.sin(theta[i]) * np.cos(alpha[i])
        y = coords[-1][1] + length * np.sin(theta[i]) * np.sin(alpha[i])
        z = coords[-1][2] + length * np.cos(theta[i])
        coords.append((x, y, z))
    return coords


# 使用蒙特卡洛方法获取随机点
def monte_carlo_sampling(N):
    points = []
    for _ in range(N):
        theta = np.random.uniform(0, np.pi / 2, 3)
        alpha = np.random.uniform(0, 2 * np.pi, 3)
        coords = forward_kinematics(theta, alpha)
        points.append(coords)
    return points


# 使用正态分布获取随机点
def normal_distribution_sampling(N, theta_mean, alpha_mean, variance):
    points = []
    for _ in range(N):
        theta = np.random.normal(theta_mean, variance, 3)
        theta = np.clip(theta, 0, np.pi / 2)

        alpha = np.random.normal(alpha_mean, variance, 3)
        alpha = np.clip(alpha, 0, 2 * np.pi)

        coords = forward_kinematics(theta, alpha)
        points.append(coords)
    return points


points_monte_carlo = monte_carlo_sampling(N)
points_normal_dist = normal_distribution_sampling(N, np.pi / 4, np.pi, 0.5)

points = points_monte_carlo + points_normal_dist

for coords in points:
    points_segment1.append(coords[1])
    points_segment2.append(coords[2])
    points_segment3.append(coords[3])

# 2D投影绘制
fig, ax = plt.subplots()
ax.scatter([p[0] for p in points_segment1], [p[2] for p in points_segment1], s=1, c='r', label='Segment 1')
ax.scatter([p[0] for p in points_segment2], [p[2] for p in points_segment2], s=1, c='g', label='Segment 2')
ax.scatter([p[0] for p in points_segment3], [p[2] for p in points_segment3], s=1, c='b', label='Segment 3')

ax.set_xlabel('X')
ax.set_ylabel('Z')
ax.legend()
plt.show()
