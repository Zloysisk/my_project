import random 

n = [random.randrange(1,5) for _ in range(10)]
a = random.randrange(1,10)
b = random.randrange(1,10)
n = n[:a] + n[b + 1:]
print(n)
