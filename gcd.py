import numpy as np

num1 = 6
num2 = 9

# finds the greatest common divisor of the two numbers
x = np.gcd(num1, num2)
print(x)

#  the reduce() method uses the gcd() function to reduce the array by one dimension.
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)