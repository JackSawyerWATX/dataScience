import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_health_data = pd.read_csv("data.csv", header=0, sep=",")

print(full_health_data.shape)
print(full_health_data.isnull().sum())

# normalize column names (strip whitespace and lowercase)
full_health_data.columns = full_health_data.columns.str.strip().str.lower()
print(full_health_data.columns)

# Remove internal whitespace (e.g. "9 000") so numeric conversion can succeed
clean = full_health_data.replace(r"\s+", "", regex=True)
print(clean)

# Attempt to convert object columns to numeric where possible
for col in clean.select_dtypes(include="object").columns:
	clean[col] = pd.to_numeric(clean[col], errors="coerce")

# Compute correlation only on numeric columns
corr_matrix = clean.select_dtypes(include=["number"]).corr().round(2)
print(corr_matrix)

correlation_full_health = corr_matrix.corr()

axis_corr = sns.heatmap(
	correlation_full_health,
	vmin=-1,
	vmax=1,
	center=0,
	cmap=sns.diverging_palette(50, 500, n=500),
	square=True
)

plt.show()