
import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

# writing array to a binary file in NumPy .npy format (saving array)
np.save('array_data.npy',arr)

# reading array from a binary file in NumPy .npy format (loading array)

loaded_arr = np.load('array_data.npy')

print("Loaded array from file:\n", loaded_arr) 

# Creating a 2D array
array_2d = np.array([[10,20,30,40,50], [60,70,80,90,100],])

np.savetxt('2darray_data.txt', array_2d, delimiter=',') 

loadTextarr = np.loadtxt('2darray_data.txt', delimiter=',') 

print("Loaded 2D array from text file:\n", loadTextarr)
                            
