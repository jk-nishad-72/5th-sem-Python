


import numpy as np

array_1d = np.array([1,2,3,4,5])
array_2d = np.array([ [1,2] , [3,4] , [5,6] ]) 
userList = input('Enter Array Elements sapareted with Space: ')

list1  = [ int(x) for x in userList.split()]

print(list1)
arrya_list = np.array(list1)
print(arrya_list[0:10:3])
# print(arrya_list)

for element in arrya_list:
    print(element)

print(array_1d.shape) 
print(array_1d.ndim)
print(array_1d.size)
# print(array_1d.max())
# print(array_1d.min())
# print(array_1d.sum())

print(np.zeros((3,3)))
print(np.ones((3,3)))
print(np.arange(0,10,2))
# print(np.linspace(5,5))

print(array_2d) 
print(array_2d.shape)

print(array_2d.ndim)
print(array_2d.size)
print(array_2d.dtype)

print(array_1d.shape)
print(array_1d.ndim)
print(array_1d.size)
print(array_1d.dtype)

print(array_2d.max())
print(array_2d.min())
print(array_2d.sum())


# Accessing elements in a 1D array
print(array_1d[0])  # First element

# Accessing elements in a 1D array multiple elements at once known as  Advanced Indexing
print(array_1d[[0,2,3]])

# conditional indexing and filtering
# condition 
condtion  = array_1d > 2 
print(condtion)
# flidtering 
print("Filtered elements:")
# print(array_1d[array_1d > 2])
print(array_1d[condtion])






