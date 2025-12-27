
# EXPERIMENT NO. 3

# Objective: Write programs to understand the use of Numpy’s Ndarray, Basic Operations, Indexing, Slicing, and Iterating, Conditions and Boolean Arrays.
# Program:
# 1. Ndarray :An Ndarray is the central data structure of the NumPy library, which represents a multidimensional array.

import numpy as np

# Creating an Ndarray
array = np.array([1, 2, 3, 4, 5])
print(array)
print(type(array))

# 2. Basic Operations :Performing basic mathematical operations on arrays.


# Basic Operations
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([5, 4, 3, 2, 1])

# Element-wise addition
sum_array = array1 + array2
print("Sum:", sum_array)

# Element-wise subtraction
diff_array = array1 - array2
print("Difference:", diff_array)

# Element-wise multiplication
prod_array = array1 * array2
print("Product:", prod_array)

# Element-wise division
div_array = array1 / array2
print("Division:", div_array)

# 3. Indexing :Accessing elements in an array.


# Indexing
array = np.array([10, 20, 30, 40, 50])
print("First element:", array[0])
print("Last element:", array[-1])

# 4. Slicing :Extracting a subarray from an array.

# Slicing
array = np.array([10, 20, 30, 40, 50])
print("First three elements:", array[:3])
print("Last two elements:", array[-2:])
print("advance slicing ->",array[0:4:2])

# 5. Iterating :Looping through elements in an array.

# Iterating
array = np.array([10, 20, 30, 40, 50])
for element in array:
    print(element)
    
for elem in array:
    print(elem) 
    
#6. Conditions and Boolean Arrays :Using conditions to create boolean arrays and filter elements.

# Conditions and Boolean Arrays 
array = np.array([10, 20, 30, 40, 50]) 

# Condition
condition = array > 25
print("Condition (array > 25):", condition)

# Filtering elements

filtered_array = array[condition]
print("Filtered array:", filtered_array) 


