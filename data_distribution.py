from numpy import random

# Generate a random integer between 0 and 100
# p sets the probability to each number in the array
# the sum of all probability number has to equal 1
x = random.choice([1, 3, 5, 7, 9, 11], p=[0.1, 0.2, 0.2, 0.1, 0.3, 0.1], size=(100))
print(x)


# almost same example as above, but with a 2D array
x = random.choice([1, 3, 5, 7, 9, 11], p=[0.1, 0.2, 0.2, 0.1, 0.3, 0.1], size=(16, 19))
print(x)