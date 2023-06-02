import matplotlib.pyplot as plt
import numpy as np

y = np.array([30, 28, 24, 21])
mylabels = ["Eva", "Antony", "Tom", "Mercy"]
myexplode = [0.2, 0, 0, 0]
mycolors = ["black", "grey", "#11abb0", "orange"]

plt.pie(y, labels = mylabels, colors = mycolors, shadow = True, explode = myexplode, startangle = 45)
plt.legend(title = "Muga K'Olale Children")
plt.show()