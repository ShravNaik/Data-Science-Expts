
# EXPT 6: ONE-HOT ENCODING & LABEL ENCODING

# 1. Load Data from CSV:
import pandas as pd

df = pd.read_csv("data.csv")

# 2. One-Hot Encoding:
one_hot_encoded = pd.get_dummies(df, columns=["Column_1", "Column_2"])

# 3. Label Encoding:
df["Column_Name_Encoded"] = df["Column_Name"].astype("category").cat.codes