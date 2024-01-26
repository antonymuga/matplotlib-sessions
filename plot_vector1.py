import matplotlib.pyplot as myplt
import numpy as np

# Step 2: define the vectors
vector_one = np.array([2, 3])
vector_two = np.array([-1, 4])

# Step 3: plot the vectors
origin = np.zeros(2) #creates a 1-dimensional NumPy array with 2 elements
myplt.quiver(*origin, *vector_one, scale=1, scale_units='xy', angles='xy', color='r', label='vector 1')
myplt.quiver(*origin, *vector_two, scale=1, scale_units='xy', angles='xy', color='b', label='vector 2')
# *origin: unpacks the arguements in origin by taking the elements in the array [0,0] and passes them to myplt.quiver), thus equal to 0,0
# *vector_one: unpacks vector_one array and passes the args to myplt.quiver(), if vector_one is [2, 3], then it is equivalent to 2,3
# scale=1: controls the length of the arrow, in this case length of arrow is proportional to magnitude
# scale_units='xy': indicates the scale is applied to the x and y directions independently
# angles='xy': specifies that arrow angles are defined by the x and y coordinated of the vectors
# color='r', color='b': red and blue colors for the arrows respectively
# label='vector 1': names of the labels 

# Set plot limits
myplt.xlim(-5, 5)
myplt.ylim(-5, 5)

# Add labels and legend
myplt.xlabel('X-axis')
myplt.ylabel('Y-axis')
myplt.legend()

# Show the plot
myplt.grid(True)
myplt.axhline(0, color='black', linewidth=0.5) # Add black horizontal line to the plot
myplt.axvline(0, color='black', linewidth=0.5)
myplt.show()

