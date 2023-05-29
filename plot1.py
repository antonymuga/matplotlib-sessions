import matplotlib
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([10, 68])
ypoints = np.array([-1, 5])

#plot() draws points which are known as markers in
#matplotlib parlance
plt.plot(xpoints, ypoints)

plt.show()