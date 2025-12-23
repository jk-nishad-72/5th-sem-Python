
## UNIT–IV: The Pandas Library

### 1. Introduction to Pandas

Pandas is a powerful Python library used for data manipulation and analysis. It provides fast, flexible, and expressive data structures.

---
### first need to install -> 

### 1) opern terminal as administator
### 2) run -> pip install pandas
---

---

## 2. Core Data Structures

### a) Series

* One-dimensional labeled array.
* Can hold any data type (int, float, string, etc.).
* labeled array means ->
* A labeled array is an array in which each data element is associated with an index or name(label) that identifies it uniquely.

**Example:**

```python
import pandas as pd
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
```

---

### b) DataFrame

* Two-dimensional labeled data structure (rows & columns).
* Similar to a table or spreadsheet.

**Example:**

```python
data = {'Name': ['Jay', 'Aman'], 'Age': [20, 21]}
df = pd.DataFrame(data)
```

---

### c) Index Objects

* Immutable array-like structure for labeling axes.
* Enables fast data alignment and selection.

```python
df.index
df.columns
```

---

## 3. Data Manipulation

### a) Reindexing

* Changes the order of rows/columns or adds new ones.

```python
df.reindex(['b', 'a'])
```

---

### b) Dropping

* Removes rows or columns.

```python
df.drop('Age', axis=1)
df.drop(0)
```

---

### c) Arithmetic and Data Alignment

* Pandas aligns data by labels automatically.

```python
df1 + df2
```

---

### d) Operations between DataFrame and Series

* Broadcasting applied automatically.

```python
df.sub(df['Age'], axis=0)
```

---

## 4. Applying Functions

### a) Functions by Element

* Apply to each element.

```python
df.applymap(lambda x: x*2)
```

---

### b) Functions by Row or Column

* `axis=0` → column-wise
* `axis=1` → row-wise

```python
df.apply(sum, axis=0)
```

---

## 5. Statistical Functions

* `sum()`
* `mean()`
* `min()`, `max()`
* `std()`
* `describe()`

```python
df.describe()
```

---

## 6. Sorting and Ranking

### Sorting

```python
df.sort_values(by='Age')
df.sort_index()
```

### Ranking

```python
df.rank()
```

---

## 7. Correlation and Covariance

* Measures relationship between variables.

```python
df.corr()
df.cov()
```

---

## 8. Handling Missing Data (NaN)

### Detecting NaN

```python
df.isna()
```

### Removing NaN

```python
df.dropna()
```

### Filling NaN

```python
df.fillna(0)
```

---

## 9. Reading and Writing Data

### a) CSV & Text Files

```python
pd.read_csv('data.csv')
df.to_csv('output.csv')
```

---

### b) HTML Files

```python
pd.read_html('table.html')
```

---

### c) XML Files

```python
pd.read_xml('data.xml')
```

---

### d) Microsoft Excel Files

```python
pd.read_excel('file.xlsx')
df.to_excel('output.xlsx')
```

---

## 10. Summary

* Pandas simplifies data analysis
* Automatic data alignment
* Strong support for missing data handling
* Easy file I/O operations

---

✔ **Exam Tip:** Focus on definitions, differences (Series vs DataFrame), and basic code examples.
