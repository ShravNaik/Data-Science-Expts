
# EXPT 8: IMPLEMENT K-MEANS ALGORITHM

# 1. Load Data from EXCEL
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


df = pd.read_excel("data.xlsx")

# 2. Standardize features:
standardscaler = StandardScaler()
df_standardized = standardscaler.fit_transform(df)

# 3. Apply K-Means:
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(df_standardized)

# 4. Visualize:
print(df.head())

plt.scatter(df["Column_1"], df["Column_2"], c=df["Cluster"], cmap="viridis", s=80)
plt.title("K-Means clustering")
plt.show()