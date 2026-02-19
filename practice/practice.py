# mutable vs immutable
# mutable : mutable means can be changed after creation
# If you modify it the memory address remains the same
# list,set,dict,bytearray are mutable datatypes.

# Immutable : Immutable means can't be changed after creation
# If you modify it, python creates a new object in memory
# Remaining all are immutable.


nums=[1,2,3]
print(id(nums))
print(nums)

nums.append(4)
print(id(nums))
print(nums)

x=10
print(id(x))
print(x)
x+=1
print(id(x))
print(x)

name='avinash '
print(id(name))
print(id)

name+='avi'
print(id(name))
print(name)


t=(1,2,[3,4,5])
print(id(t))
print(t)
t[2].append(9)
print(id(t))
print(t)

a=[1,2]
b=a
a=[5,6]
print(a)
print(b)

a=[1,2]
print(id(a))
b=a
print(id(b))
c=a.copy()
print(id(c))
a.append(3)
print(id(a))
print(a)
print(b)
print(c)

import copy

a = [[1, 2], [3, 4]]
print(id(a))
b = copy.deepcopy(a)
print(id(b))

a[0].append(99)
print(id(a))

print(a)
print(b)

d = {(1,2): "hello"}  # works
print(d)