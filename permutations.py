from numpy import random
import numpy as np

x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

random.shuffle(x)  # method makes changes to the original array.
print(x)

y = random.permutation(x)  # method returns a re-arranged array
                           # (and leaves the original array un-changed).
print(y)

z = (y == x)
print(z)
