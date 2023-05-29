import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([34, 56, 17, 89])
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])
plt.plot(ypoints, marker = 'h', lw = 1.5, ls = "-.", color = "#ffc107", ms = 20, mfc = "#11abb0", mec = "#ffc107")
plt.plot(x1, marker = 'h', lw = 1.5, ls = "-", color = "#ffc10b", ms = 20, mfc = "#11abb0", mec = "#fec107")
plt.plot(y1, marker = '*', lw = 1.5, ls = "-.", color = "#ffb107", ms = 20, mfc = "#11acb0", mec = "#ffc107")
plt.plot(x2, marker = 'o', lw = 1.5, ls = "-.", color = "#ffc107", ms = 20, mfc = "#21abb0", mec = "#afd107")
plt.plot(y2, marker = 'x', lw = 1.5, ls = "-.", color = "#fac107", ms = 20, mfc = "#11abb0", mec = "#ffc107")
plt.show()