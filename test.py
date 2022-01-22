import pandas
import numpy as np

a = np.array([1,2,3,4])
print(a)

import time 

a = np.random.rand(1000000)
b = np.random.rand(1000000)

c = np.dot(a,b)

a = np.random.randn(4,3)
b = np.random.randn(3,2)
c = a*b
c.shape