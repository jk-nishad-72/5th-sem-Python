
# EXPERIMENT NO. 4

# Objective: Write programs to understand the use of Numpy’s Shape Manipulation, Array Manipulation,
#  	       Vectorization.
# Program:
# Shape Manipulation: Shape manipulation allows you to change the shape of an array without changing its data.

import numpy as np

# Create a 1D array

arr = np.array([1, 2, 3, 4, 5, 6])
print("Original array:", arr)

# Reshape to 2D array (2 rows, 3 columns)
reshaped_arr = np.reshape(arr, (2, 3))
print("Reshaped array:\n", reshaped_arr)

# Flatten the array back to 1D
flattened_arr = reshaped_arr.flatten()
print("Flattened array:", flattened_arr) 

# Array Manipulation : Array manipulation includes various operations like joining, splitting, and modifying arrays.


# Create two 1D arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenate arrays
concatenated_arr = np.concatenate((arr1, arr2))
print("Concatenated array:", concatenated_arr)

# Stack arrays vertically
stacked_arr = np.vstack((arr1, arr2))
print("Vertically stacked array:\n", stacked_arr) 

# Split the concatenated array into three equal parts
split_arr = np.array_split(concatenated_arr, 3)
print("Split arrays:", split_arr)


# Vectorization :Vectorization involves performing operations 
# on entire arrays rather than individual elements, which can  lead to more efficient code.


# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Perform element-wise operation 

squared_arr = np.square(arr)
print("Squared array:", squared_arr)

# Perform vectorized addition
arr_sum = arr + 10
print("Array after addition:", arr_sum)

# Perform vectorized multiplication
arr_product = arr * 2
print("Array after multiplication:", arr_product)
