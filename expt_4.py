
# EXPT 4: BINNING & DISCRETIZATION

# 1. Load Data from CSV:
import pandas as pd

df = pd.read_csv("data.csv")

# 2. Binning:
bins = [0, 10, 20, 30, 40, 50]
labels = ["Label 1", "Label 2", "Label 3", "Label 4", "Label 5"]

df["Column_Name"] = pd.cut(df["Column_Name"], bins=bins, labels=labels)

df["Column_Name"] = pd.qcut(df["Column_Name"], 4)