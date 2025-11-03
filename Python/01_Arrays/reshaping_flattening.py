import numpy as np

a = np.arange(6)
a = a.reshape(2,3)
print(a)

b = a.flatten()
print(b)

a = a.ravel()
print(a)

c = np.arange(6)
c = c.reshape(2,3)
print(c.shape)

c = c.reshape((3,2))
print(c.shape)