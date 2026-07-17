
# EXPT 5: DESCRIPTIVE STATISTICS

# 1. Load Data from EXCEL:
import pandas as pd
import numpy as np

df = pd.read_excel("data.xlsx")

# 2. Generate Descriptive Statistics:
print(df.mean())
print(df.median())
print(df.mode())
print(df.var())
print(df.std())

# Generate Group Statistics:
# Generate groups using pd.cut()
group_stats = df.groupby("Groups")["Column_Name"].agg(["min", "max", "mean", "median", "var", "std"])