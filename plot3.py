import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([3, 8, 17, 54])
ypoints = np.array([13, 9, 78, 23])

plt.plot(ypoints, "*-.g")
plt.plot(xpoints, "h:m")
plt.show()