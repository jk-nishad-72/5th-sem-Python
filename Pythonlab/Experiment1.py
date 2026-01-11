# EXPERIMENT NO. 1

# Objective: Write programs to understand the use of Python Identifiers, Keywords, Indentations, and Comments in Python, Operators, Membership operator.

# Program : 

# 1. Identifiers :Identifiers are names given to variables, functions, classes, etc., in Python. They must start with a letter or an underscore (_) and can be followed by letters, digits, or underscores.

# Identifiers
name = "Alice"  # variable
def greet():
	print("Hello")

class Person:
	pass
greet()  # calling the function

# 2. Keywords :Keywords are reserved words in Python that have special meaning and cannot be used as identifiers.
# Keywords
# Here, "if" and "else" are keywords
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. Indentation :
# Indentation is used to define the scope of loops, functions, and conditional statements in Python. Proper indentation is essential.
# Indentation
def check_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
check_even(4)

# 4. Comments :Comments are used to explain code and are ignored by the interpreter. Single-line comments start with #,
# and multi-line comments are enclosed within triple quotes ''' or """.
# Single-line comment
x = 5  # This is a single-line comment

'''
This is a multi-line comment
spanning multiple lines
'''

"""
Another way to write
multi-line comments
"""
# 5. Operators :Operators are used to perform operations on variables and values. They include arithmetic, comparison, logical, assignment, bitwise, and more.
# Operators
a = 10
b = 3

# Arithmetic Operators
sum_ab = a + b
diff_ab = a - b
prod_ab = a * b
div_ab = a / b

# Comparison Operators
is_equal = (a == b)
is_greater = (a > b)

# Logical Operators
and_op = (a < 5) and (b < 5)
or_op = (a < 5) or (b < 5)
not_op = not(a >= 10 ) 

print(f"NOT Operation Result: {not_op}")
# print(f"Sum: {sum_ab}, Difference: {diff_ab}, Product: {prod_ab}, Division: {div_ab}")
# print(f"Is Equal: {is_equal}, Is Greater: {is_greater}")
# print(f"AND Operation: {and_op}, OR Operation: {or_op}")




# 6. Membership Operator
# Membership operators (in and not in) are used to test whether a value is a member of a sequence (like a list, tuple, or string).
# Membership Operators
my_list = [1, 2, 3, 4, 5]
my_string = "Hello, World!"

print(3 in my_list)        # True
print(6 not in my_list)    # True
print("Hello" in my_string)  # True
print("Python" not in my_string)  # True

