
# EXPERIMENT NO. 9

# Objective: Write programs to understand the use of Matplotlib for Simple Interactive Chart,
# Set the Properties of the Plot, matplotlib and NumPy.
# Program:
# Simple Interactive Chart
# Matplotlib allows for the creation of interactive charts that can be customized and manipulated.
# python

import matplotlib.pyplot as plt 
import numpy as np

# simple plot (line plot)

a = [1,2,3,4]
b = [10,20,30,50]

plt.plot(a , b)
plt.show()


# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x) 

# Create an interactive plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
line, = ax.plot(x, y)

# Update the plot in a loop
for phase in np.linspace(0, 10, 100):
    line.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()

plt.ioff()  # Turn off interactive mode
plt.show()

# Set the Properties of the Plot
# You can set various properties of the plot, such as title, labels, line style, and markers.
# python

# Create some data
x = np.linspace(0, 10, 100)
y = np.cos(x)

# Create a plot with customized properties
plt.figure()
plt.plot(x, y, label='cos(x)', color='red', linestyle='--', marker='o')
plt.title('Cosine Function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()

# Matplotlib and NumPy
# Matplotlib works seamlessly with NumPy, making it easy to plot NumPy arrays.
# python

# Create some data using NumPy
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)

# Create a plot with multiple lines
plt.figure()
plt.plot(x, y1, label='sin(x)')
plt.plot(x, y2, label='cos(x)')
plt.title('Sine and Cosine Functions')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.show()
