
Below is a **clear, exam-oriented explanation of UNIT-V: Data Visualization with Matplotlib**, written in **simple language**, with **definitions + examples** you can directly write in exams or use in practicals.

---

# **UNIT–V: Data Visualization with Matplotlib**

## **Introduction to Matplotlib**

Matplotlib is a **Python library** used to create **2D plots and charts**.
It works very well with **NumPy arrays** and is widely used for **data analysis and visualization**.

```python
import matplotlib.pyplot as plt
import numpy as np
```

---

## **1️⃣ A Simple Interactive Chart (Basic Plot)**

A simple chart is created using the `plot()` function.

### Example (Line Plot):

```python
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

plt.plot(x, y)
plt.show()
```

📌 Displays a basic line chart.

---

## **2️⃣ Setting the Properties of the Plot**

We can customize the plot using different properties.

### Example:

```python
plt.plot(x, y, color='red', linestyle='--', marker='o')
plt.title("Simple Line Chart")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.show()
```

### Common Properties:

* `color`
* `linestyle`
* `marker`
* `linewidth`
* `title`
* `xlabel`, `ylabel`

---

## **3️⃣ Matplotlib and NumPy**

Matplotlib works efficiently with NumPy arrays.

### Example:

```python
x = np.arange(0, 10)
y = x ** 2

plt.plot(x, y)
plt.show()
```

📌 NumPy generates data, Matplotlib visualizes it.

---

## **4️⃣ Working with Multiple Figures and Axes**

### Multiple Figures:

```python
plt.figure()
plt.plot(x, y)

plt.figure()
plt.plot(x, x**3)
plt.show()
```

### Multiple Axes (Subplots):

```python
plt.subplot(1, 2, 1)
plt.plot(x, y)

plt.subplot(1, 2, 2)
plt.plot(x, x**3)
plt.show()
```

---

## **5️⃣ Adding Text to the Plot**

Used to display custom text inside the graph.

### Example:

```python
plt.text(2, 10, "Sample Text")
plt.plot(x, y)
plt.show()
```

---

## **6️⃣ Adding a Grid**

Grid improves readability.

### Example:

```python
plt.plot(x, y)
plt.grid(True)
plt.show()
```

---

## **7️⃣ Adding a Legend**

Legend explains what each line represents.

### Example:

```python
plt.plot(x, y, label='y = x²')
plt.plot(x, x**3, label='y = x³')
plt.legend()
plt.show()
```

---

## **8️⃣ Saving the Charts**

Plots can be saved as image files.

### Example:

```python
plt.plot(x, y)
plt.savefig("my_plot.png")
plt.show()
```

📌 Supported formats: `.png`, `.jpg`, `.pdf`

---

# **Types of Charts**

---

## **9️⃣ Line Chart**

Used to show trends.

### Example:

```python
plt.plot(x, y)
plt.title("Line Chart")
plt.show()
```

---

## **🔟 Histogram**

Used to show data distribution.

### Example:

```python
data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5)
plt.title("Histogram")
plt.show()
```

---

## **1️⃣1️⃣ Bar Chart**

Used for categorical comparison.

### Example:

```python
names = ['A', 'B', 'C']
values = [10, 20, 15]

plt.bar(names, values)
plt.title("Bar Chart")
plt.show()
```

---

## **1️⃣2️⃣ Pie Chart**

Used to show percentage distribution.

### Example:

```python
sizes = [30, 40, 20, 10]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()
```

---

## **Quick Exam Summary**

| Feature    | Function        |
| ---------- | --------------- |
| Line chart | `plt.plot()`    |
| Histogram  | `plt.hist()`    |
| Bar chart  | `plt.bar()`     |
| Pie chart  | `plt.pie()`     |
| Grid       | `plt.grid()`    |
| Legend     | `plt.legend()`  |
| Save plot  | `plt.savefig()` |

---

## **Short Exam Answer (5–6 Lines)**

> Matplotlib is a Python library used for data visualization. It supports line charts, bar charts, histograms, and pie charts. It allows setting plot properties, adding text, grid, legend, multiple axes, and saving charts to files. Matplotlib works efficiently with NumPy arrays.

---
