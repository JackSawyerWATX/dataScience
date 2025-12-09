import pandas as pd
import numpy as np

try:
  health_data = pd.read_csv("data.csv", header=0, sep=",")
  print("CSV loaded sucessfully.")
  print(health_data.head())

  x = health_data["Average_Pulse"]
  y = health_data["Calorie_Burnage"]
  slope_intercept = np.polyfit(x,y,1)

  print(slope_intercept)

  def slope(x1, y1, x2, y2):
    s = (y2 - y1) / (x2 - x1)
    return s

  print(slope(80, 240, 90, 260))

except FileNotFoundError:
  print("Error: File not found. Please check the file path.")
except KeyError as e:
  print(f"Error: Missing column {e}. Please check the CSV file.")
except Exception as e:
  print(f"An unexpected error occurred: {e}")


# Summary — what this script does
# 1) Imports Pandas and NumPy for data handling and numeric operations.
# 2) Attempts to read `data.csv` (expects columns `Average_Pulse` and `Calorie_Burnage`).
# 3) If CSV loads, prints a success message and shows the first rows with `head()`.
# 4) Extracts `x = Average_Pulse` and `y = Calorie_Burnage` and computes a linear
#    fit using `np.polyfit(x, y, 1)`, returning slope and intercept.
# 5) Defines a helper `slope(x1, y1, x2, y2)` that computes the slope between two
#    points and demonstrates it with a sample `print(slope(80, 240, 90, 260))`.
# 6) Handles common errors with user-friendly messages: `FileNotFoundError` when
#    `data.csv` is missing, `KeyError` if expected columns are absent, and a
#    generic `Exception` catch-all that prints the unexpected error.
#
# Recommendations:
# - Verify `data.csv` exists in the script directory and contains the expected
#   column names (case-sensitive).
# - If numeric columns contain thousands separators or non-numeric values
#   (e.g., '9 000' or 'AF'), preprocess them with `pd.to_numeric(..., errors='coerce')`
#   and drop or fill NaNs before calling `np.polyfit`.

