# Vectorization :Vectorization involves performing operations on entire arrays rather than individual elements, which can lead to more efficient code.
import numpy as np
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


