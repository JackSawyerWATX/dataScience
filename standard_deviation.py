import pandas as pd
import numpy as np

full_health_data = pd.read_csv("data.csv", header=0, sep=",", thousands=' ')

numeric = full_health_data.select_dtypes(include=[np.number])

std = numeric.std(axis=0)
print(std)


mean = numeric.mean(axis=0)
cv = std / mean

print("\nCoefficient of variation (std / mean):")
print(cv)


# 1. Read `data.csv` using spaces as thousands separators (`thousands=' '`).
# 2. Keep numeric columns only (`select_dtypes(include=[np.number])`).
# 3. Compute and print standard deviation per numeric column (`std(axis=0)`).
