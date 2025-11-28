import sys
import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import pandas as pd

health_data = pd.read_csv(
    "health_data.csv",
    delim_whitespace=True,
    engine="python"
)

import re

# Step 1: Read entire file
with open("health_data.csv", "r") as f:
    raw = f.read()

# Step 2: Fix numbers with spaces inside them: 9 000 → 9000
raw = re.sub(r'(\d)\s+(\d{3})', r'\1\2', raw)

# Step 3: Replace AF or any non-numeric pulse with NaN
raw = re.sub(r'\bAF\b', 'NaN', raw)

# Step 4: Save cleaned file
with open("health_data_cleaned.csv", "w") as f:
    f.write(raw)

# Step 5: Load cleaned file
import pandas as pd
health_data = pd.read_csv("health_data_cleaned.csv", sep=r"\s+")


health_data = pd.read_csv("health_data.csv", sep =r"\s+")

print("\nCOLUMNS FOUND:")
for col in health_data.columns:
  print(f"- {repr(col)}")

health_data.plot(x='Average_Pulse', y = 'Calorie_Burnage', kind = 'line')
plt.ylim(ymin = 0)
plt.xlim(xmin = 0)

plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()



# def slope(x1, y1, x2, y2):
#   s = (y2 - y1) / (x2 - x1)
#   return s

# print(slope(5, 3, 7, 2))


    # Calculate the slope of the line passing through two points (x1, y1) and (x2, y2).

    # Args:
    #     x1 (float): x-coordinate of the first point.
    #     y1 (float): y-coordinate of the first point.
    #     x2 (float): x-coordinate of the second point.
    #     y2 (float): y-coordinate of the second point.

    # Returns:
    #     float: The slope of the line.