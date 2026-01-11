# Vectorization :Vectorization involves performing operations on entire arrays rather than individual elements, which can lead to more efficient code.
import numpy as np
# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([10, 20, 30, 40, 50, 60])

# Perform element-wise operation
squared_arr = np.square(arr)
print("Squared array:", squared_arr)

# Perform vectorized addition
arr_sum = arr + 10
print("Array after addition:", arr_sum)

# Perform vectorized multiplication
arr_product = arr * 2
print("Array after multiplication:", arr_product)

# broadcasting example
sum_arrays = arr + arr2
print("Sum of two arrays:", sum_arrays) 

