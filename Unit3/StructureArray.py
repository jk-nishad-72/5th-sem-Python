
# Structured Arrays : Structured arrays allow you to define and access different fields by names.
import numpy as np 

# Define a structured array with different data types
structured_arr = np.array([(1, 'Alice', 25.5), (2, 'Bob', 30.1)],dtype=[('ID', 'i4'), ('Name', 'U10'), ('Age', 'f4')])

print("Structured Array:") 
print(structured_arr)

# Accessing fields by name
print("Names:", structured_arr['Name'])
print("Ages:", structured_arr['Age'])

# Modifying an entry
structured_arr['Age'][0] = 26.5
print("Modified Structured Array:")
print(structured_arr)