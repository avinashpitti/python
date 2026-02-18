s={}
print(type(set))

se=set()
print(type(se))

a={1,2,3,2,2,1,6}
print(a)
a.add(7)
print(a)
a.remove(3) # throws error if not present
print(a)

a.discard(5) # Doesn't show error if not present
print(a)

a.pop()
print(a) # since set is unordered pop removes random element

a.clear()
print(a)

x={1,2,3,4}
y={3,4,5,6,7}

print(x | y) # union
print(x & y) # intersection
print(x - y)
print(x ^ y) # symmetric difference

z={1,2,3}
z.update([3,4,5])
print(z)

v={1,2,3}
v.update([4])
print(v)