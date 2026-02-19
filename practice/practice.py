s={1,2,3}
s.add(6)
print(s)
s.discard(5) # discard doesn't show error, if the value doesn't exist 
print(s)
# s.remove(5) # remove shows error if the value doesn't exist

s.update([7,9,45,67])
print(s)

s.remove(9)
print(s)

a={1,2,3,4}
b={3,4,5,6}
print(a & b) #Intersection
print(a | b) # union
print(a-b) # difference
print(a ^ b)# symmetric difference


