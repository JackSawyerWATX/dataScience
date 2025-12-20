import numpy as np

# removes the decimals
arr = np.trunc([4.25, 2.06])
print(arr)

# another way of removing decimals
arr = np.fix([4.25, 2.06])
print(arr)

# rounding decimals
arr = np.around([2.81, 7.13])
print(arr)

# rounds down
arr = np.floor([2.81, 7.13])
print(arr)

# rounds up
arr = np.ceil([2.81, 7.13])
print(arr)

