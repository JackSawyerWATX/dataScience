import numpy as np

num1 = 5
num2 = 8

# finds the least common multiples of each number
x = np.lcm(num1, num2)
print(x)

# the reduce() method uses the lcm() function to reduce the array by one dimension.
arr = np.array([4, 8, 12])
x = np.lcm.reduce(arr)
print(x)


arr = np.arange(3, 9)
x = np.lcm.reduce(arr)
print(x)