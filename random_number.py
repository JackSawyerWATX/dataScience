import random

num =  random.randint(1, 1000000)
print(num)
count = 1

while num != 1000000:
  num = random.randint(1, 1000000)
  print(num)
  count += 1

print("You got one million.")
print(count)



def countdown(n):
  while n > 0:
    print(n)
    n -= 1
  print("Done!")



countdown(5000)