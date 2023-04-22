# What is a Random Number?
# Random number does NOT mean a different number every time.
# Random means something that can not be predicted logically.
from numpy import random

x = random.randint(100)
y = random.rand()  # floats
yy = random.rand(5)   # 5 random floats betweein 0 - 1
yyy = random.rand(3,2)
z = random.randint(100, size=(5))
zz = random.randint(100, size=(2, 3))
print(x, y, z)
print(zz)
print(yy)
print(yyy)


print(random.choice([2,55,66,55,22,55,24,4,25,12], size=(2, 5)))
