import numpy as np

x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
z = []

# using Python's build in .zip()
for i, j in zip(x, y):
  z.append(i + j)
print(z)

# using NumPy's ufuncs
x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 8])
z = np.add(x, y)

print(z)