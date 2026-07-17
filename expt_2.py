
# EXPT 2: NORMALIZATION & STANDARDIZATION

# 1. Read Data from CSV:
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import numpy as np

df = pd.read_csv("data.csv")

# 2. Get Info about the data:
print(df.head())
print(df.describe())

# 3. Normalization using MinMaxScaler (0-1)
X = df.copy() # Copy DataFrame into X
minmax = MinMaxScaler() # Create a MinMax Variable

X_minmax = pd.DataFrame(minmax.fit_transform(X), columns=X.columns) # Fit X into range 0 to 1

# 4. Standardization using StandardScaler (Mean=0 & SD=1)
X = df.copy()
standardscaler = StandardScaler()

X_standard = pd.DataFrame(standardscaler.fit_transform(X), columns=X.columns)

# 5. Printing MIN-MAX Values:
print("Min-Max Values: ", X.agg(["min", "max"]))
print("Min-Max Values Normalized: ", X_minmax.agg(["min", "max"]))
print("Min-Max Values Standardized: ", X_standard.agg(["min", "max"]))

# 6. Printing MEAN-SD Values:
print("Mean-SD Values: ", X.agg(["mean", "std"]))
print("Mean-SD Values Normalized: ", X_minmax.agg(["mean", "std"]))
print("Mean-SD Values Standardized: ", X_standard.agg(["mean", "std"]))