import pandas as pd
import numpy as np

health_data = pd.read_csv("data.csv", header=0, sep=",")

x = health_data["Average_Pulse"]
y = health_data["Calorie_Burnage"]
slope_intercept = np.polyfit(x,y,1)

print(slope_intercept)

def slope(x1, y1, x2, y2):
  s = (y2 - y1) / (x2 - x1)
  return s

print(slope(80, 240, 90, 260))


# Calculate the slope of the line passing through two points (x1, y1) 
# and (x2, y2).

# Args:
#     x1 (float): x-coordinate of the first point.
#     y1 (float): y-coordinate of the first point.
#     x2 (float): x-coordinate of the second point.
#     y2 (float): y-coordinate of the second point.

# Returns:
#     float: The slope of the line.

