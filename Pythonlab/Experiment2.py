
# EXPERIMENT NO. 2

# Objective: Write programs to understand the use of Python String, Tuple, List, Set, Dictionary, File 
# 	       Input / output.
# Program:


# 1. String :A string in Python is a sequence of characters.
# String
my_string = "Hello, Python!"
print(my_string)
print(my_string.upper())       # Convert to uppercase
print(my_string.lower())       # Convert to lowercase
print(my_string[0:5])          # Slice string
print(len(my_string))          # Length of string

# 2. Tuple :A tuple is an immutable sequence of items.

# Tuple
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple)
print(my_tuple[0])             # Access element
print(len(my_tuple))           # Length of tuple
# Tuples are immutable, so you cannot change their values


# 3. List :A list is a mutable sequence of items.

# List
my_list = [1, 2, 3, 4, 5]
print(my_list)
my_list.append(6)              # Add an element
print(my_list)
my_list[0] = 10                # Change an element
print(my_list)
print(len(my_list))            # Length of list

# 4. Set :A set is an unordered collection of unique items.

# Set
my_set = {1, 2, 3, 4, 5}
print(my_set)
my_set.add(6)                  # Add an element
print(my_set)
my_set.remove(3)               # Remove an element
print(my_set)
# Sets are unordered, so items may appear in any order

# 5. Dictionary : A dictionary is a collection of key-value pairs.

# Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)
print(my_dict["name"])         # Access value by key
my_dict["age"] = 26            # Change value
print(my_dict)
my_dict["country"] = "USA"     # Add key-value pair
print(my_dict)

 
# 6. File Input/Output
# Reading from and writing to files.

# File Input/Output
# Write to a file
with open("example.txt", "w") as file:
    file.write("Hello, file!")

# Read from a file
with open("example.txt", "r") as file:
    content = file.read()
    
