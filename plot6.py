import numpy as np
import matplotlib.pyplot as plt

x = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])
y = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])

font1 = {"family":"serif", "color":"green", "size":15}
font2 = {"family":"san-serif", "color":"darkred", "size":15}
plt.title("Betika Data", fontdict = font1, loc = "right")
plt.xlabel("Average bets", fontdict = font2)
plt.ylabel("Average loses", fontdict = font2)

plt.plot(x, y)

plt.grid(axis = "y")
plt.grid(axis = "x", color = "green", ls = ":", lw = 1.5)

plt.show()