import numpy as np

# to make a ufunc, define a function as you would with a normal function in Python,
# then add it to your NumPy function library with the frompyfunc() method.

def myadd(x, y):
  return x + y
myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))
print(type(np.concatenate))

# the frompyfunc() method takes the following arguments:
# function - the name of the function
# inputs - the number of input arguments (arrays)
# outputs - the number of output arrays

if type(np.add) == np.ufunc:
  print("add is ufunc")
else:
  print("add is not ufunc")

if type(np.concatenate) == np.ufunc:
  print("concatenate is not ufunc")
else:
  print("concatenate is ufunc")

# Note: A ufunc (universal function) is a function that performs element-wise operations