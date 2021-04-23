import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])       # 准备数据
fig = plt.figure()                            # 创建画布
ax = fig.add_subplot(9,9,81)             # 添加绘图区域
ax.plot(data)                # 绘制图表
plt.title("My First Figure")
ax1 = fig.add_subplot(9,9,14)             # 添加绘图区域
ax1.plot(data)                # 绘制图表
plt.title("My Ninth Figure")
plt.show()   # 图表展示