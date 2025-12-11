import numpy as np
import pandas as pd

# sorts the array numerically
arr = np.array([4, 1, 7, 3, 6, 10,8, 5, 9, 2])
# Use a pandas Series (or DataFrame) and call its describe() method
df = pd.Series(arr).describe()
print(np.sort(arr))
print(df)

# sorts array alphabetically
arr = np.array(['elderberry', 'banana', 'fig', 'cherry', 'apple', 'date'])
print(np.sort(arr))

# sorts booleans
arr = np.array([True, False, True, False])
print(np.sort(arr))

# sorts a 2D array
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))