import numpy as np
import matplotlib.pyplot as plt

x = np.array(range(-10, 11))
y = x**2
x, y

plt.plot(x, y)
for i in x:
    plt.plot(i, i**2, 'ro')
    plt.pause(1)

plt.show()