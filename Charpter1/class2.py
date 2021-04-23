import numpy as np
import matplotlib.pyplot as plt
data = np.array([1, 2, 3, 4, 5])       # 准备数据
fig = plt.figure()                            # 创建画布
ax = fig.add_subplot(111)             # 添加绘图区域
ax.plot(data)                                  # 绘制图表
plt.title("first figure")
plt.show()                                      # 展示图表