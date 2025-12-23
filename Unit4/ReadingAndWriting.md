
Below is the **corrected version of your code** followed by a **clear explanation of each part**, written in an **exam-oriented + practical way**.

---

## ✅ Corrected Code (Proper & Safe)

```python
import pandas as pd

# Sample DataFrame (needed for XML & Excel operations)
data = {
    'Country': ['India', 'USA', 'China'],
    'Population': [1400, 331, 1440]
}
df = pd.DataFrame(data)

# -------------------------------
# Reading and Writing HTML Files
# -------------------------------

# Reading DataFrame from an HTML page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
tables = pd.read_html(url)

# Wikipedia page contains multiple tables
df_html = tables[0]   # First table
print("DataFrame read from HTML file:\n", df_html.head())

# Writing DataFrame to an HTML file
df_html.to_html('data.html', index=False)

# -------------------------------
# Reading and Writing XML Files
# -------------------------------

# Writing DataFrame to an XML file
df.to_xml('data.xml', index=False)

# Reading DataFrame from an XML file
df_xml = pd.read_xml('data.xml')
print("DataFrame read from XML file:\n", df_xml)

# -------------------------------
# Reading and Writing Excel Files
# -------------------------------

# Writing DataFrame to an Excel file
df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')

# Reading DataFrame from an Excel file
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print("DataFrame read from Excel file:\n", df_excel)
```

---

## 📌 Explanation (Topic-wise)

---

## 1️⃣ Reading and Writing HTML Files

### Reading HTML

```python
tables = pd.read_html(url)
```

* `read_html()` reads **all tables** from a web page
* Returns a **list of DataFrames**
* Each table on the webpage becomes one DataFrame

```python
df_html = tables[0]
```

* Selects the **first table** from the list

### Writing HTML

```python
df_html.to_html('data.html')
```

* Saves the DataFrame as an **HTML table**
* Used for web reports or dashboards

---

## 2️⃣ Reading and Writing XML Files

### Writing XML

```python
df.to_xml('data.xml')
```

* Converts DataFrame into **XML structured format**
* Useful for **data exchange between systems**

### Reading XML

```python
df_xml = pd.read_xml('data.xml')
```

* Reads XML data back into a DataFrame

---

## 3️⃣ Reading and Writing Microsoft Excel Files

### Writing Excel

```python
df.to_excel('data.xlsx', sheet_name='Sheet1')
```

* Saves DataFrame into an **Excel (.xlsx) file**
* `sheet_name` specifies the worksheet name

### Reading Excel

```python
pd.read_excel('data.xlsx')
```

* Reads Excel file into a DataFrame
* Commonly used in **business & data analysis**

---

## 📝 Exam Points to Remember

✔ `read_html()` → returns **list of DataFrames**
✔ `to_html()` → saves DataFrame as web table
✔ `to_xml()` / `read_xml()` → structured data exchange
✔ `read_excel()` / `to_excel()` → Excel file handling

---

## ✍️ Short Exam Answer (5 Marks)

> Pandas provides functions to read and write data in HTML, XML, and Excel formats. The `read_html()` function reads tables from web pages, `read_xml()` handles structured XML data, and `read_excel()` is used for Excel files. Corresponding `to_*` functions are used to write DataFrames into these file formats.

If you want, I can also give:

* **Output screenshots**
* **Differences: CSV vs Excel vs XML**
* **Viva questions from this topic**

Just tell me 👍
