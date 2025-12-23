
#* Objective: Write programs to understand the use of Pandas for Reading and Writing Data using CSV and Textual Files, HTML Files, XML, Microsoft Excel Files..
# Program:

# Reading and Writing CSV Files
# CSV (Comma Separated Values) files are widely used for storing tabular data.
import pandas as pd
# Writing DataFrame to a CSV file
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)
# Reading DataFrame from a CSV file
df_csv = pd.read_csv('data.csv')
print("DataFrame read from CSV file:\n", df_csv)

# Reading and Writing Textual Files
# Textual files can be read and written similarly to CSV files, but with custom delimiters.
# Writing DataFrame to a text file with custom delimiter
df.to_csv('data.txt', sep='|', index=False)
# Reading DataFrame from a text file with custom delimiter
df_txt = pd.read_csv('data.txt', delimiter='|')
print("DataFrame read from text file:\n", df_txt)


# Reading and Writing HTML Files
# Pandas can read tables directly from HTML files.
# Reading DataFrame from an HTML file
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_population_(United_Nations)'
tables = pd.read_html(url)
df_html = tables[0] # Assuming the first table is the one we want
print("DataFrame read from HTML file:\n", df_html.head())
# Writing DataFrame to an HTML file
df_html.to_html('data.html')

# Reading and Writing XML Files
# Pandas can also handle XML files for structured data.
# Writing DataFrame to an XML file
df.to_xml('data.xml')
# Reading DataFrame from an XML file
df_xml = pd.read_xml('data.xml')
print("DataFrame read from XML file:\n", df_xml)


# Reading and Writing Microsoft Excel Files
# Excel files are commonly used in business environments for data storage.

# Writing DataFrame to an Excel file
df.to_excel('data.xlsx', index=False, sheet_name='Sheet1')
# Reading DataFrame from an Excel file
df_excel = pd.read_excel('data.xlsx', sheet_name='Sheet1')
print("DataFrame read from Excel file:\n", df_excel) 