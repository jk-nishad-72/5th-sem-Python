
# Objective: Write programs to understand the use of Numpy’s Structured Arrays, Reading and Writing Array Data on Files.
# Program:
# Structured Arrays : Structured arrays allow you to define and access different fields by names.

import numpy as np

# Define a structured array with different data types
structured_arr = np.array([(1, 'Alice', 25.5), (2, 'Bob', 30.1)],
                          dtype=[('ID', 'i4'), ('Name', 'U10'), ('Age', 'f4')])
print("Structured Array:")
print(structured_arr)

# Accessing fields by name
print("Names:", structured_arr['Name'])
print("Ages:", structured_arr['Age'])

# Modifying an entry 
structured_arr['Age'][0] = 26.5
print("Modified Structured Array:") 
print(structured_arr)

# Reading and Writing Array Data to Files
# Numpy provides functions to easily save and load arrays.
# Saving and Loading Binary Files

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Save the array to a binary file
np.save('my_array.npy', arr)

# Load the array from the binary file
loaded_arr = np.load('my_array.npy')
print("Loaded Array from Binary File:", loaded_arr)

# Saving and Loading Text Files

# Create a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])

# Save the array to a text file
np.savetxt('my_array.txt', arr, delimiter=',')

# Load the array from the text file
loaded_arr = np.loadtxt('my_array.txt', delimiter=',')
print("Loaded Array from Text File:\n", loaded_arr)

