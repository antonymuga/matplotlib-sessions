import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([10, 30, 20, 40])

plt.barh(x, y, color = "#11abb0", height = 0.1)
plt.show()