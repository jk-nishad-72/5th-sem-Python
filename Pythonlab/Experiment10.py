# EXPERIMENT NO. 10

# Objective: Write programs to understand the use of Matplotlib for Working with Multiple Figures and Axes, Adding Text, Adding a Grid, Adding a Legend, Saving the Charts.
# Program:
# Working with Multiple Figures and Axes
# You can create multiple figures and axes to organize your plots.

import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the first figure
plt.figure(1)
plt.plot(x, y1)
plt.title('Sine Function')

# Create the second figure
plt.figure(2)
plt.plot(x, y2)
plt.title('Cosine Function')

plt.show()

# Adding Text
# You can add text annotations to your plots to provide additional information.

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.title('Sine Function')

# Add text annotation
plt.text(5, 0, 'Sine wave at x=5', fontsize=12, ha='center')

plt.show()

# Adding a Grid
# Adding a grid to your plot can make it easier to read and interpret.

# Create data
x = np.linspace(0, 10, 100)
y = np.cos(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.title('Cosine Function')

# Add a grid
plt.grid(True)

plt.show()

# Adding a Legend
# Legends are useful for identifying different lines or datasets in a plot.

# Create data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a plot with multiple lines
plt.figure()
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Sine and Cosine Functions')

# Add a legend
plt.legend()

plt.show()

# Saving the Charts
# You can save your charts to a file in various formats.

# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y)
plt.title('Sine Function')

# Save the plot as a PNG file
plt.savefig('sine_function.png')

# Save the plot as a PDF file
plt.savefig('sine_function.pdf')

plt.show()
