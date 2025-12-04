import numpy as np
import pandas as pd

# Read CSV, handle thousands-separators and surrounding spaces
health_data = pd.read_csv(
	"data.csv",
	header=0,
	sep=",",
	thousands=" ",
	skipinitialspace=True,
	na_values=["", "NA", "N/A", "n/a", "NULL"],
)

# Coerce all columns to numeric where possible.
# Remove internal whitespace (e.g. '9 000' -> '9000') before coercion so thousands
# formatted with spaces are parsed as numbers. Non-numeric tokens become NaN.
for col in health_data.columns:
	health_data[col] = pd.to_numeric(
		health_data[col].astype(str).str.replace(r"\s+", "", regex=True),
		errors="coerce",
	)

# Drop rows that still contain NaNs (these came from originally-missing or non-numeric fields)
health_data.dropna(axis=0, inplace=True)

print(health_data)

# Use pandas to compute per-column standard deviation and mean
std = health_data.std(axis=0)
mean = health_data.mean(axis=0)
cv = std / mean

print("\nStandard deviation per column:\n", std)
print("\nMean per column:\n", mean)
print("\nCoefficient of Variation (std/mean) per column:\n", cv)