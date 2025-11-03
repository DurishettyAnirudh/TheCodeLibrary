import numpy as np

a = np.array([10,20,30,40,50])
print("first = ", a[0] )
print("last = ", a[-1])
print("first 3 elements = ", a[ :3 ])
print("reverse = ", a[::-1])


d2 = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(d2[1, :])
print(d2[:, 2])
print(d2[1,2])


