import numpy as np

arr = np.array([10, 15, 25, 6])

# subtracts each element from the next element in the array
# 15 -10 = 5, 25 - 15 = 10, 6 - 25 = -19 -> [  5  10 -19]
newarr = np.diff(arr)
print(newarr)

# runs throught the same process with the new array
newarr = np.diff(arr, n=2)
print(newarr)

# runs this process 3 times, and since I started with an array 
# with 4 elements, it returns one number
newarr = np.diff(arr, n=3)
print(newarr)

# returns an empty array
newarr = np.diff(arr, n=4)
print(newarr)

