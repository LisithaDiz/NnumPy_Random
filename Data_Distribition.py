# data distribution is all possible values how often each value occurs
from numpy import random

x = random.choice([3, 5, 7, 9], p=[0.333, 0.333, 0.333, 0.001], size=(100))
z = 0
print(x)
for i in x:
    if i == 7:
        z += 1
print(z/100)

