import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([34, 56, 17, 89])
plt.plot(ypoints, marker = 'h', ls = "-.", ms = 20, mfc = "#11abb0", mec = "#ffc107")
plt.show()