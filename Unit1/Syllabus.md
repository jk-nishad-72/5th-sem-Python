
Below is a **clear, structured, exam-oriented explanation of Python – UNIT-I (Introduction & Key Concepts)**. This is suitable for **college exams, viva, and quick revision**.

---

# **UNIT-I: Introduction to Python – Key Concepts**

## 1. Introduction to Python

Python is a **high-level, interpreted, object-oriented programming language** known for its **simplicity and readability**.
It is widely used in **web development, data analysis, AI/ML, automation, and scripting**.

### Features of Python:

* Easy to learn and use
* Interpreted language
* Platform independent
* Large standard library
* Supports OOP and functional programming

---

## 2. Python Identifiers

**Identifiers** are the names used to identify variables, functions, classes, or objects.

### Rules:

* Can contain letters, digits, and underscore (_)
* Must start with a letter or underscore
* Cannot start with a digit
* Case-sensitive
* Cannot be a keyword

### Examples:

```python
name = "Jay"
_total = 100
marks1 = 90
```

---

## 3. Keywords in Python

**Keywords** are reserved words with special meaning in Python.

### Examples:

`if`, `else`, `while`, `for`, `break`, `continue`, `True`, `False`, `None`, `class`, `def`, `return`, `import`

> Keywords cannot be used as identifiers.

---

## 4. Indentation in Python

Python uses **indentation instead of braces `{}`** to define blocks of code.

### Example:

```python
if x > 0:
    print("Positive number")
```

* Standard indentation: **4 spaces**
* Improper indentation causes `IndentationError`

---

## 5. Comments in Python

Comments are used to **explain code** and are ignored by the interpreter.

### Types:

1. **Single-line comment**

```python
# This is a comment
```

2. **Multi-line comment**

```python
"""
This is
a multi-line
comment
"""
```

---

## 6. Operators in Python

Operators are symbols used to perform operations on variables and values.

### Types of Operators:

1. **Arithmetic Operators**
   `+  -  *  /  %  //  **`

2. **Relational (Comparison) Operators**
   `==  !=  >  <  >=  <=`

3. **Logical Operators**
   `and  or  not`

4. **Assignment Operators**
   `=  +=  -=  *=  /=`

5. **Bitwise Operators**
   `&  |  ^  ~  <<  >>`

---

## 7. Membership Operators

Membership operators are used to **test whether a value exists in a sequence**.

### Operators:

* `in`
* `not in`

### Example:

```python
list1 = [1, 2, 3]
print(2 in list1)      # True
print(5 not in list1) # True
```

---

## 8. Bit Manipulation

Bit manipulation works at the **binary level**.

### Common Bitwise Operations:

| Operator | Meaning     |    |
| -------- | ----------- | -- |
| `&`      | AND         |    |
| `        | `           | OR |
| `^`      | XOR         |    |
| `~`      | NOT         |    |
| `<<`     | Left shift  |    |
| `>>`     | Right shift |    |

### Example:

```python
a = 5   # 0101
b = 3   # 0011
print(a & b)  # 1
```

---

## 9. String

A **string** is a sequence of characters enclosed in quotes.

### Example:

```python
name = "Python"
```

### Properties:

* Immutable
* Indexed
* Supports slicing

### Example:

```python
print(name[0])      # P
print(name[1:4])    # yth
```

---

## 10. Tuple

A **tuple** is an ordered, immutable collection.

### Example:

```python
t = (10, 20, 30)
```

### Features:

* Immutable
* Faster than list
* Allows duplicate values

---

## 11. List

A **list** is an ordered, mutable collection.

### Example:

```python
list1 = [1, 2, 3, "Python"]
```

### Features:

* Mutable
* Allows duplicates
* Supports indexing and slicing

---

## 12. Set

A **set** is an unordered collection of unique elements.

### Example:

```python
s = {1, 2, 3, 3}
print(s)  # {1, 2, 3}
```

### Features:

* No duplicates
* Unordered
* Used for set operations

---

## 13. Dictionary

A **dictionary** stores data in **key-value pairs**.

### Example:

```python
student = {
    "name": "Jay",
    "age": 20
}
```

### Features:

* Keys must be unique
* Fast lookup
* Mutable

---

## 14. File Input/Output (I/O)

File I/O allows reading from and writing to files.

### Open a File:

```python
file = open("data.txt", "r")
```

### Read from File:

```python
content = file.read()
```

### Write to File:

```python
file = open("data.txt", "w")
file.write("Hello Python")
file.close()
```

### File Modes:

| Mode | Meaning      |
| ---- | ------------ |
| `r`  | Read         |
| `w`  | Write        |
| `a`  | Append       |
| `r+` | Read & Write |

---

## 15. Conclusion

Python provides **simple syntax, powerful data structures, and efficient file handling**, making it ideal for beginners and professionals.

---