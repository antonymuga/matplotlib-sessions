import numpy as np
import matplotlib.pyplot as myplt

# we want to plot a vector graph from 2 linear equations in matplotlib
# step 2: define the linear equations
# For Example, let's consider two equations: 2x + 1 = y and -3x + 4 = y

# define funtions to compute the equations

def equation1(x):
    return 2 * x + 1

def equation2(x):
    return -3 * x + 4

# Step 3: generate x - values
x_values = np.linspace(-5, 5, 100)

# step 4: calculate corresponding y-values using the equations
y_values_eq1 = equation1(x_values)
y_values_eq2 = equation2(x_values)

# step 5: Plot the vectors
myplt.plot(x_values, y_values_eq1, label='y = 2x + 1')
myplt.plot(x_values, y_values_eq2, label='y = -3x + 4')

# Add labels and legends
myplt.xlabel('x-axis')
myplt.ylabel('y-axis')
myplt.legend()

# display the plot
myplt.grid(True)
myplt.axhline(0, color='black', linewidth=0.5)
myplt.axhline(0, color='black', linewidth=0.5)
myplt.title("Vector graph of two linear equations")
myplt.show()
