import numpy as np

a = np.array([1,2,3])
b = a.view()
c = a.copy()

a[0] = 4

print(a)
print(b)
print(c)
