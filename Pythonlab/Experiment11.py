
# EXPERIMENT NO. 11

# Objective: Write programs to understand the use of Matplotlib for Working with Line Chart, Histogram, Bar Chart, Pie Charts.

# Program:
# Line Chart
# A line chart is used to display data points connected by straight lines.

import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a line chart
plt.figure()
plt.plot(x, y, label='sin(x)')
plt.title('Line Chart: Sine Function')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()
plt.grid(True)
plt.show()


# Histogram
# A histogram is used to represent the distribution of a dataset.

# Create some data
data = np.random.randn(1000)

# Create a histogram
plt.figure()
plt.hist(data, bins=30, alpha=0.7, color='blue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Bar Chart
# A bar chart is used to compare different categories of data.


# Create some data
categories = ['A', 'B', 'C', 'D']
values = [5, 7, 2, 4]

# Create a bar chart
plt.figure()
plt.bar(categories, values, color='green', alpha=0.7, edgecolor='black')
plt.title('Bar Chart')
plt.xlabel('Category')
plt.ylabel('Value')
plt.grid(True)
plt.show()

# Pie Chart
# A pie chart is used to represent the proportions of different categories.

# Create some data
labels = ['A', 'B', 'C', 'D']
sizes = [25, 35, 20, 20]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)  # explode the 1st slice

# Create a pie chart
plt.figure()
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Pie Chart')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

