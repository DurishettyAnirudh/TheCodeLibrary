lis = [x**2 for x in range(1,6) ]
print(lis)


lis = [x for x in range(1,11) if x % 2 == 0]
print(lis)

lis1 = ['abc', 'def', 'ghi']
lis2 = [x.upper() for x in lis1]
print(lis2)

lis = [x**3 for x in range(1,11) if x % 2 == 1]
print(lis)