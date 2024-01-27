import numpy as np
import matplotlib.pyplot as myplt
from mpl_toolkits.mplot3d import Axes3D

# Define the linear equations
# for example, 2x + 3y = z and 1.5x + 2y = z

def equation1(x, y):
    return 2 * x + 3 * y

def equation2(x, y):
    return -1.5 * x + 2 * y

# create data points
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
x, y = np.meshgrid(x, y)

# calculate the z values based on the linear equations
z1 = equation1(x, y)
z2 = equation2(x, y)

# Create a 3d plot
fig = myplt.figure()

# 111 represents the number of rows, the number of columns and the index of the subplot in a grid
# in this case it creates a single subplot in a 1 x 1 grid and the subplot is at index 1
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z1, alpha=0.5, rstride=100, cstride=100, color='b', label='2x + 3y = z')
ax.plot_surface(x, y, z2, alpha=0.5, rstride=100, cstride=100, color= 'g', label='-1.5x + 2y')

# add labels and legends
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.legend()

# show the plot
myplt.show()

