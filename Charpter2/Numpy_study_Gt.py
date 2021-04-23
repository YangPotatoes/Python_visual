'''
Hello EveryBody, Today is Woman's Day.
'''
'''
import numpy as np

A = [1,2,3,4,5]
B = [2,4,6,8,10]
X = []
# A^2 +B  len(A)
for i in range(0,A.__len__()):
    X.append(A[i]*A[i]+B[i])
print(X)
A1 = np.array([1,2,3,4,5])
B1 = np.array([2,4,6,8,10])
print(A1*A1 + B1)
'''
'''
import numpy as np
arr2 = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 655]])
print(arr2.shape) #矩阵的行列
arr2.shape = 4,3  #修改矩阵行列，注意：元素个数要和原来保持一致
print(arr2)
'''
'''
import numpy as np

np_array = np.arange(0,101,10)
print(np_array)
'''
'''
import numpy as np
import matplotlib.pyplot as plt
#print(np.logspace(0,1,100))
#print(np.zeros((4,3)))# 创建0矩阵，注意传进去的参数为元组类型
#print(np.eye(5))
x = np.arange(8, 15)#9-16
y_max = np.array([15,15,15,14,15,19,24])
y_min = np.array([10, 11, 11,12,13,14,12])
plt.plot(x, y_max)
plt.plot(x, y_min)
plt.title("ChengDu Weather")
plt.show()
'''
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(2015,2020)
CD = np.array([10801.16,12170.23,13889.39,15342.77,17012.65])
CQ = np.array([15717,17741,19425,20363,23604])
bar_width = 0.3
# 根据多组数据绘制柱形图
plt.bar(x, CD,  width=bar_width)
plt.bar(x+bar_width, CQ,width=bar_width)
plt.legend(["ChengDu","ChongQing"])
plt.title("CD and CQ GDP")
plt.show()

