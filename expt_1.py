
# EXPT 1: HANDLING MISSING DATA & DUPLICATES

# 1. Read Data from CSV:
import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

# 2. Get Info about the data: (OPTIONAL)
print(df.head()) # returns first 5 rows of data
print(df.describe()) # returns basic statistics about data
print(df.info()) # returns comprehensive information about data
print(df.shape) # returns a tuple containing dimensions of data
print(df.tail()) # returns last 5 rows of data
print(df.iloc[:, [0, 1, 4]]) # Integer location (all rows, 0th 1st 4th column)

# 3. Detect missing values:
missing_values = df.isnull() # Returns True is value is missing, False otherwise
    # OR
missing_values1 = df.isna() # Returns True is value is missing, False otherwise

non_missing_values = df.notnull() # Returns False is value is missing, True otherwise
    # OR
non_missing_values1 = df.notna() # Returns False is value is missing, True otherwise

# 4. Handle missing values:

# A. Dropping Columns or Rows:
df_cleaned_rows = df.dropna(how="all") # Drops rows containing all missing values
df_cleaned_columns = df.dropna(axis=1 ,how="all") # Drops columns containing all missing values

# B. Filling missing values:
df["Column_Name"] = df["Column_Name"].fillna(method="ffill") # Fills missing values will previous valid values
df["Column_Name"] = df["Column_Name"].fillna(method="bfill", limit=1) # Fills missing values will next valid value with limit of 1
df["Column_Name"] = df["Column_Name"].fillna(0) # Fills missing value with constant 0
df["Column_Name"] = df["Column_Name"].fillna(df["Column_Name"].mean()) # Fills missing values with mean of the column

# 5. Detecting Duplicates:
print(df.duplicated()) # Returns True if there are duplicates present, False otherwise

# 6. Handling Duplicates:
df_cleaned_subset_duplicates = df.drop_duplicates(subset=["Column_1"]) # Drops duplicates in specified column
df_cleaned_duplicates = df.drop_duplicates(["Column_1", "Column_2"], keep="first") # Drops duplicates across multiple columns; keeps first occurrence
