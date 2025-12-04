import pandas as pd
import numpy as np

# Read `data.csv` using `thousands=' '` and `skipinitialspace=True`,
# and treat common empty/NA tokens as missing values.
health_data = pd.read_csv(
	"data.csv",
	header=0,
	sep=",",
	thousands=" ",
	skipinitialspace=True,
	na_values=["", "NA", "N/A", "n/a", "NULL"],
)

# Remove internal whitespace from every cell (e.g. convert `'9 000'` -> 
# `'9000'`) and coerce each column to numeric with `pd.to_numeric(..., 
# errors='coerce')` so non-numeric # tokens become `NaN`.
for col in health_data.columns:
	health_data[col] = pd.to_numeric(
		health_data[col].astype(str).str.replace(r"\s+", "", regex=True),
		errors="coerce",
	)

# Drop rows that contain any remaining `NaN` values (these came from 
# missing or non-numeric fields after coercion).
health_data = health_data.dropna(axis=0)

# Compute per-column variance with `DataFrame.var(axis=0)` (pandas 
# default `ddof=1`).
variance_series = health_data.var(axis=0)

# Print the resulting `variance_series`. To change the variance 
# formula, pass `ddof=` to `.var()` or modify the code.
print(variance_series)


