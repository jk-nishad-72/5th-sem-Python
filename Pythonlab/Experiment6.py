
# Objective: Write programs to understand the use of Pandas Series, Data Frame, Index Objects,
# Reindexing, Dropping, Arithmetic and Data Alignment.

# Program:
# Pandas Series
# A Pandas Series is a one-dimensional array with axis labels. 
# python
import pandas as pd 
# Create a Series
s = pd.Series([1, 2, 3, 4, 5], index=['a', 'b', 'c', 'd', 'e'])
s2 = pd.Series(['apple', 'banana', 'cherry'], index=[1, 2, 3])
print("Series:\n", s)
print("Series 2:\n", s2)
# Accessing elements
print("Element with label 'c':", s['c'])
print('Element at position 1:', s2.iloc[0]) # Using iloc for positional indexing without label 
print('Element at position 1:', s2[1]) 



# DataFrame
# A DataFrame is a two-dimensional labeled data structure with columns of potentially different types.
# python
# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
'Age': [25, 30, 35],
'City': ['New York', 'San Francisco', 'Los Angeles']}
df = pd.DataFrame(data)
print("DataFrame:\n", df)
# Accessing columns
print("Age column:\n", df['Age'])


# Index Objects
# Index objects are immutable and hold the axis labels for pandas objects.
# python
# Create an Index
index = pd.Index(['a', 'b', 'c', 'd', 'e'])
print("Index:", index)

# Using Index with Series
si = pd.Series([1, 2, 3, 4, 5], index=index)
print("Series with Index:\n", si)


# Reindexing
# Reindexing allows you to change/add/delete the index on a specified axis.
# python
# Original Series
s3 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
print("Original Series:\n", s3)
# Reindex the Series
s_reindexed = s3.reindex(['a', 'b', 'c', 'd', 'e'])
print("Reindexed Series:\n", s_reindexed)

# Dropping
# Dropping allows you to remove specified labels from rows or columns.
# Original DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]}, index=['a', 'b', 'c'])
print("Original DataFrame:\n", df)

# Drop a row
df_dropped = df.drop('b')
print("DataFrame after dropping row 'b':\n", df_dropped)
# Drop a column
df_dropped = df.drop('B', axis=1)
print("DataFrame after dropping column 'B':\n", df_dropped)


# Arithmetic
# Performing element-wise operations on DataFrame or Series.
# Create two Series
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['a', 'b', 'c'])
# Element-wise addition
s_sum = s1 + s2
print("Sum of Series:\n", s_sum)

# Create two DataFrames

df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
df2 = pd.DataFrame({'A': [5, 6], 'B': [7, 8]})
# Element-wise multiplication
df_product = df1 * df2
print("Product of DataFrames:\n", df_product)

# Data Alignment
# Data alignment means automatically aligning the data by index labels.

# Create two Series with different indices
s1 = pd.Series([1, 2, 3], index=['a', 'b', 'c'])
s2 = pd.Series([4, 5, 6], index=['b', 'c', 'd'])

# Element-wise addition with alignment 
s_aligned_sum = s1 + s2
print("Sum with alignment:\n", s_aligned_sum)