import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])# 准备数据
fig = plt.figure(111)                            # 创建画布
ax = fig.add_subplot()             # 添加绘图区域
ax.plot(data)                                  # 绘制图表
plt.show()