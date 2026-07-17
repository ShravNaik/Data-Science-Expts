
# EXPT 3: HISTOGRAMS, BOXPLOT & SCATTERPLOT

# 1. Read data from CSV:
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

# 2. Histogram
plt.hist(df["Column_Name"], bins=20)
plt.title("Histogram")
plt.show()

# 3. Boxplot
plt.boxplot(df["Column_Name"])
plt.title("Box Plot")
plt.show()

# 4. Scatterplot
plt.scatter(df["Column_Name_1"], df["Column_Name_2"])
plt.xlabel("Colum_1")
plt.ylabel("Column_2")
plt.title("Scatter Plot")
plt.show()
