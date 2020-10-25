import numpy as np
from numpy.random import randn

n = 10000
counter = 0
for i in randn(n):
    if -1 < i < 1:
        counter = counter + 1
print(counter/100)
