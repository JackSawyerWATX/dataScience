from numpy import random

# generates a random number
x = random.randint(100)
print(x)

# generates a random float
x = random.rand()
print(x)

# generates a random 1D array of the number of integers specified as size=()
x = random.randint(100, size=(7))
print(x)

# generates a random 2D array of the shape specified as size=()
# In this example, it has 4 rows and 5 integers
x = random.randint(100, size=(4, 6))
print(x)

# generates a 1D array containing 5 random floats
x = random.rand(5)
print(x)

# generates a 2D array with 5 rows, and each row containing 9 random numbers
x = random.rand(5, 9)
print(x)

#generates a random number from an array of numbers
x = random.choice([1, 3, 5, 7, 9, 11])
print(x)

# generates a 2D array of values in any parameter
x = random.choice([1, 3, 5, 7, 9, 11], size=(5, 7))
print(x)