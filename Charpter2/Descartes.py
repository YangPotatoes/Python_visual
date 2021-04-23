import numpy as np
from matplotlib import pyplot as plt
import math
pi = math.pi
x = np.linspace(-3.3**0.5, 3.3**0.5, 6001).reshape(-1,1)
y = (x**2)**(1/3) + 0.9*np.sqrt(3.3 - x**2)*np.sin(40*pi*x)
plt.plot(x,y,color = 'r')
plt.xlim(-3,3)
plt.show()
