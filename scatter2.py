import matplotlib.pyplot as plt
import numpy as np

x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])

colors = np.array(["red", "gray", "green", "blue", "yellow", "pink", "black", "orange", "magenta", "cyan", "beige", "brown", "purple"])

plt.scatter(x, y, c = colors)
plt.show()