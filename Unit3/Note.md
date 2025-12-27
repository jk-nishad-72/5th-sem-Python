
Here’s a **clear, exam-oriented explanation of UNIT–III: NumPy Library**, structured topic-wise. This is perfect for **theory exams + quick revision**.

---

## **UNIT–III: The NumPy Library**

### **1. NumPy and ndarray**

NumPy (Numerical Python) is a powerful library used for **numerical computing** in Python.

* The core object of NumPy is the **ndarray (N-dimensional array)**
* Stores **homogeneous data** (same data type)
* Faster and more memory-efficient than Python lists

**Example:**

```python
import numpy as np
a = np.array([1, 2, 3, 4])
```

---

### **2. Basic Operations**

Arithmetic operations are **element-wise**.

**Examples:**

```python
a + b
a - b
a * b
a / b
```

Other operations:

```python
a.sum()
a.min()
a.max()
a.mean()
```

---

### **3. Indexing**

Used to access specific elements.

* Indexing starts from **0**

**Examples:**

```python
a[0]      # first element
a[-1]     # last element
```

For 2D arrays:

```python
arr[1, 2]
```

---

### **4. Slicing**

Used to extract a portion of an array.

**Syntax:**

```python
array[start : end : step]
```

**Examples:**

```python
a[1:4]
a[::2]
```

2D slicing:

```python
arr[:, 1]
arr[1:3, :]
```

---

### **5. Iterating**

Used to traverse array elements.

**Examples:**

```python
for i in a:
    print(i)
```

For multidimensional arrays:

```python
for row in arr:
    print(row)
```

---

### **6. Conditions and Boolean Arrays**

Used to filter data.

**Example:**

```python
a > 5
a[a > 5]
```

Boolean indexing:

```python
a[(a > 2) & (a < 6)]
```

---

### **7. Shape Manipulation**

Used to change array shape **without changing data**.

**Attributes:**

```python
a.shape
a.ndim
a.size
```

**Reshaping:**

```python
a.reshape(2, 3)
a.flatten()
a.ravel()
```

---

### **8. Array Manipulation**

Functions to modify arrays.

* Joining arrays:

```python
np.concatenate()
np.vstack()
np.hstack()
```

* Splitting arrays:

```python
np.split()
np.hsplit()
np.vsplit()
```

---

### **9. Vectorization**

Vectorization means performing operations **without loops**.

* Faster than loops
* Improves performance

**Example:**

```python
a = np.array([1, 2, 3])
b = a * 2
```

---

### **10. Broadcasting**

Broadcasting allows NumPy to perform operations on arrays of **different shapes**.

**Example:**

```python
a = np.array([1, 2, 3])
b = 2
a + b
```

Rules:

1. Dimensions must match or
2. One of them must be 1

---

### **11. Structured Arrays**

Structured arrays store **heterogeneous data**.

**Example:**

```python
data = np.array([(1, 'Jay', 85.5)],
dtype=[('id', 'i4'), ('name', 'U10'), ('marks', 'f4')])
```

Accessing fields:

```python
data['name']
```

---

### **12. Reading and Writing Array Data on Files**

Used for data storage.

**Saving data:**

```python
np.save('data.npy', a)
np.savetxt('data.txt', a)
```

**Loading data:**

```python
np.load('data.npy')
np.loadtxt('data.txt')
```

---

## **Quick Exam Tips**

* `ndarray` is the **core data structure**
* NumPy operations are **vectorized**
* Boolean indexing is used for **filtering**
* Broadcasting improves performance
* Structured arrays handle **mixed data types**

---

If you want, Jay, I can also provide:

* **Short answers (2–3 marks)**
* **Numerical problems**
* **Previous-year exam questions**
* **One-page revision notes (PDF style)**

Just tell me 👍
