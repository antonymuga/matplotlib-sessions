import numpy as np
import matplotlib.pyplot as myplt


# Define the matrix A
A = np.array([[2,3], [1, -1]])

# Define a range of x values
# x_values = linspace(x1, x2, n) generates n points. The spacing between points is ((10 -(-10))/100 -1)
# stands for linear spacing
x_values = np.linspace(-10, 10, 100)


# transforms the domain specified by vectors x1 and x2 into arrays x1 and x2 which
# will b eused to evaluate funtions of 2 variables and 3d mesh/surface plots
x1, x2 = np.meshgrid(x_values, x_values)

# Compute linera equation Ax (matrix A by x) refer to Maths for ML


# plot the 3D graph
result = A[0, 0] * x1 + A[0, 1] * x2, A[1, 0] * x1 + A[1, 1] * x2
fig = myplt.figure()

# fig is a reference to the figure object created
# add_subplot adds a subplot to the figure
# projection='3d' specifies the subplot should be 3d
ax = fig.add_subplot(projection='3d')

# result[0] is a 2d array, the z coordinates of the grid, representing result of Ax
# alpha: the transparency of th eplot surface, 1.0 is opaque while 0.0 transparent
# rstride: the row stride i.e. the step size
# cstride: the column stride i.e. the step size
# x1, x2 and result[0] define the grid points of x, y, z coordinates
ax.plot_surface(x1, x2, result[0], alpha=0.5, rstride=100, cstride=100)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Ax')
myplt.title('Graph  of the Linear Equation Ax')
myplt.show()

