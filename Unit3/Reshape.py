
import numpy as np   

array_2d = np.array([[10,20,30,40,50],
                     [60,70,80,90,100],]);  


print("2D Array Element at row 2 and column 5:", array_2d)  # Accessing element at row 1, column 2

# Shape Manipulation->
# Reshaping, Flattening, ravel 
# 
# Array Manipulation -> Concatenating, Stacking, and Splitting Arrays  

# Create a 1D array 
arr = np.array([1, 2, 3, 4, 5, 6]) 
print("Original array:", arr) 
 
# Reshape to 2D array (2 rows, 3 columns)  
reshaped_arr1d = np.reshape(array_2d, (5,2))
print("Reshaped 2D to 1D array:\n", reshaped_arr1d)
reshaped_arr = np.reshape(arr, (2, 3 )) 
reshaped_arr = np.reshape(arr, (2, 3 ,1)) 
print("Reshaped array:\n", reshaped_arr) 
 
# Flatten the array back to 1D 
flattened_arr = reshaped_arr.flatten() 
print("Flattened array:", flattened_arr)



# ravel the array

arr = np.array([[1, 2, 3], [4, 5, 6]])
raveled_arr = arr.ravel()
print("Raveled array:", raveled_arr) 


arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
arr3 = np.array([7, 8, 9]) 

# Concatenate arrays 
# Joining arrays:
# np.concatenate()
# np.vstack()
# np.hstack()

concatenated_arr = np.concatenate((arr1, arr2, arr3))  
print("Concatenated array:", concatenated_arr) 
 
# Stack arrays vertically  
stacked_arr = np.vstack((arr1, arr2, arr3)) 
print("Vertically stacked array:\n", stacked_arr) 
 
# Stack arrays horizontally  
hstacked_arr = np.hstack((arr1, arr2, arr3))
print("Horizontally stacked array:", hstacked_arr) 


# Split the concatenated array into three equal parts 
# Splitting arrays:
# np.split()
# np.hsplit()
# np.vsplit()

split_arr = np.array_split(concatenated_arr, 3) 
print("Split arrays:",split_arr) 



# Vertically split the stacked array into two parts
vsplit_arr = np.vsplit(stacked_arr, 3)
print("Vertically split arrays:", vsplit_arr)


# Horizontally split the stacked array into three parts
hsplit_arr = np.hsplit(stacked_arr, 3)
print("Horizontally split arrays:", hsplit_arr)




