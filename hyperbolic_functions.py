import numpy as np

# finds the sinh value of pi/2
x = np.sinh(np.pi/2)
print(x)

# finds the sinh values for all values in arr
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sinh(arr)
print(x)

# finds the cosh value of pi/2
x = np.cosh(np.pi/2)
print(x)

# finds the tanh value of pi/2
x = np.tanh(np.pi/2)
print(x)

# finds the area hyperbolic sine of 1.0
x = np.arcsinh(1.0)
print(x)

# finds the area hyperbolic sine for all the sinh values in the array
arr = np.array([0.1, 0.2, 0.5])
x = np.arcsinh(arr)
print(x)