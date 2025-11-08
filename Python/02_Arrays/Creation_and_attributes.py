import numpy as np

d1 = np.array([1,2,3,4,5])

d2 = np.array([[1,2,3], [4,5,6]])

print(d1)
print(d2)

print()
print(d1.shape)
print(d1.ndim)
print(d1.size)
print(d1.dtype)

print()
zero = np.zeros((2,3), int)
print(zero)

print()
one = np.ones((3,2), int)
print(one)


print()
random = np.random.randint(10,size = (2,2))
print(random)

print()
random = np.random.rand(2,3)
print(random)

