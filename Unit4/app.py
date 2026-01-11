
import numpy as np

array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
array_1d = np.array([10, 20, 30, 40, 50])

for row in array_2d:
    for element in row:
        print(element)


def reverse_array(arr):
    i = 0
    j = arr.size - 1 
    while (i<j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    return(arr)

print(reverse_array(array_1d))