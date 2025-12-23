
# Objective: 7. Write programs to understand the use of Pandas Functions by Element, Functions by Row or Column, Statistics Functions, Sorting and Ranking, Correlation and Covariance, “Not a Number” Data.
# Program:


#*Functions by Element
# Element-wise functions are applied to each element in a Series or DataFrame.

import pandas as pd
import numpy as np

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
print("Original DataFrame:\n", df)

# Apply a function element-wise
df_squared = df.applymap(np.square)
print("DataFrame with elements squared:\n", df_squared)


#*Functions by Row or Column

# Functions can be applied along rows or columns.


# Apply a function to each column
column_sum = df.apply(np.sum, axis=0)
print("Sum of each column:\n", column_sum)
# Apply a function to each row
row_sum = df.apply(np.sum, axis=1)
print("Sum of each row:\n", row_sum)

#*Statistical Functions

# Pandas provides a variety of statistical functions.
# Mean of each column
mean = df.mean()
print("Mean of each column:\n", mean)
# Standard deviation of each column
std_dev = df.std()
print("Standard deviation of each column:\n", std_dev)


#*Sorting and Ranking
# Sorting and ranking data based on values.

# Create a DataFrame
df = pd.DataFrame({'A': [3, 1, 2], 'B': [6, 5, 4]})
print("Original DataFrame:\n", df)
# Sort by column 'A'
sorted_df = df.sort_values(by='A')
print("DataFrame sorted by column 'A':\n", sorted_df)
# Rank the values in column 'A'
ranked_df = df['A'].rank()
print("Ranked values of column 'A':\n", ranked_df)

#* Correlation and Covariance
# Correlation and covariance between columns.

# Create a DataFrame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
# Correlation between columns
correlation = df.corr()
print("Correlation between columns:\n", correlation)
# Covariance between columns
covariance = df.cov()
print("Covariance between columns:\n", covariance)


#* "Not a Number" (NaN) Data
# Handling NaN values in your data.

# Create a DataFrame with NaN values
df = pd.DataFrame({'A': [1, np.nan, 3], 'B': [4, 5, np.nan]})
print("Original DataFrame with NaN values:\n", df)
# Check for NaN values
nan_check = df.isna()
print("Check for NaN values:\n", nan_check)
# Fill NaN values with a specified value

filled_df = df.fillna(0)
print("DataFrame with NaN values filled with 0:\n", filled_df)
# Drop rows with NaN values
dropped_df = df.dropna()
print("DataFrame with rows containing NaN values dropped:\n", dropped_df) 