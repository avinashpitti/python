a = [1,2,3]
b=a.copy()
a.append(4)
print(b)

c=[1,2,3]
d=c
c.append(4)
print(d)
c.remove(2)
print(d)

a = [[1,2], [3,4]]
b = a.copy()

a[0][0] = 100

print(a)
print(b)

c=[2,[3,4]]
d=c.copy()
c[0]=777
print(c)
print(d)

e=[2,[3,4]]
f=e.copy()
e[1]=5
print(e)
print(f)

g=[2,[3,4]]
h=g.copy()
g[1][0]=999
print(g)
print(h)

x = [[10]]
y = x.copy()

x[0] = [99]

print(x)
print(y)

import copy
p=[[1,2]]
q=copy.deepcopy(p)
p[0][0]=100
print(p)
print(q)

nums = [5, 6, 7]
nums.insert(-1, 99)
print(nums)

nums = [1,2,3]
nums.insert(len(nums), 50)
print(nums) # [1,2,3,50]

