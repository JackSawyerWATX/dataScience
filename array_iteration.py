import numpy as np

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# to iterate an array, use a for loop.
for x in arr:
  print(x)
  # to iterate each scalar element in the array, use a nesteted for loop.
  for y in x:
    print(y)
    for z in x:
      print(z)

# to iterate each scalar element in the array, use nditer()
for x in np.nditer(arr):
  print(x)

# to iterate each scalar element in a specific order, use the order parameter.
for x in np.nditer(arr, flags=["buffered"], op_dtypes=["S"]):
  print(x)

# to iterate through a slice of an array, use slicing syntax.
for x in np.nditer(arr[:, ::2]):
  print(x)

# ndenumerate() is used when requiring corresponding indexs of the element while iterating.
for idx, x in np.ndenumerate(arr):
  print(idx, x)

