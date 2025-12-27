
This is a **core UNIT–III / UNIT–IV–type question** and very common in exams 👍
I’ll explain it **clearly, category-wise**, with **simple examples** you can write in exams.

---

# **Linear Algebra Functions Available in NumPy**

NumPy provides a powerful module called **`numpy.linalg`** that contains functions for **linear algebra operations** such as matrix multiplication, inverse, determinant, eigenvalues, etc.

---

## **1️⃣ Matrix Multiplication**

### 🔹 Function

```python
np.dot()
# or
np.matmul()
```

### ✅ Example

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

C = np.dot(A, B)
print(C)
```

### 📌 Output

```
[[19 22]
 [43 50]]
```

---

## **2️⃣ Transpose of a Matrix**

### 🔹 Function

```python
np.transpose()
# or
A.T
```

### ✅ Example

```python
print(A.T)
```

### 📌 Output

```
[[1 3]
 [2 4]]
```

---

## **3️⃣ Determinant of a Matrix**

### 🔹 Function

```python
np.linalg.det()
```

### ✅ Example

```python
detA = np.linalg.det(A)
print(detA)
```

### 📌 Output

```
-2.0
```

---

## **4️⃣ Inverse of a Matrix**

### 🔹 Function

```python
np.linalg.inv()
```

### ✅ Example

```python
invA = np.linalg.inv(A)
print(invA)
```

### 📌 Output

```
[[-2.   1. ]
 [ 1.5 -0.5]]
```

---

## **5️⃣ Rank of a Matrix**

### 🔹 Function

```python
np.linalg.matrix_rank()
```

### ✅ Example

```python
rank = np.linalg.matrix_rank(A)
print(rank)
```

### 📌 Output

```
2
```

---

## **6️⃣ Eigenvalues and Eigenvectors**

### 🔹 Function

```python
np.linalg.eig()
```

### ✅ Example

```python
values, vectors = np.linalg.eig(A)
print("Eigenvalues:", values)
print("Eigenvectors:\n", vectors)
```

---

## **7️⃣ Solving Linear Equations**

### 🔹 Function

```python
np.linalg.solve()
```

Solves:
[
AX = B
]

### ✅ Example

```python
B = np.array([5, 11])
X = np.linalg.solve(A, B)
print(X)
```

---

## **8️⃣ Norm of a Vector or Matrix**

### 🔹 Function

```python
np.linalg.norm()
```

### ✅ Example

```python
v = np.array([3, 4])
print(np.linalg.norm(v))
```

### 📌 Output

```
5.0
```

---

## **9️⃣ Trace of a Matrix**

### 🔹 Function

```python
np.trace()
```

### ✅ Example

```python
print(np.trace(A))
```

### 📌 Output

```
5
```

---

## **10️⃣ Singular Value Decomposition (SVD)**

### 🔹 Function

```python
np.linalg.svd()
```

### ✅ Example

```python
U, S, V = np.linalg.svd(A)
```

---

## **Summary Table (Best for Exams)**

| Function                  | Purpose               |
| ------------------------- | --------------------- |
| `np.dot()`                | Matrix multiplication |
| `A.T`                     | Transpose             |
| `np.linalg.det()`         | Determinant           |
| `np.linalg.inv()`         | Inverse               |
| `np.linalg.matrix_rank()` | Rank                  |
| `np.linalg.eig()`         | Eigenvalues & vectors |
| `np.linalg.solve()`       | Solve equations       |
| `np.linalg.norm()`        | Vector/matrix length  |
| `np.trace()`              | Sum of diagonal       |
| `np.linalg.svd()`         | Matrix decomposition  |

---

## **Short Exam Answer (5–6 Lines)**

> NumPy provides various linear algebra functions through the `numpy.linalg` module. These include matrix multiplication, transpose, determinant, inverse, eigenvalues, rank, and solving linear equations. These functions are widely used in scientific computing and data analysis.

---