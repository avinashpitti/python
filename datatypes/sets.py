#A set is a built-in Python data type used to store multiple unique values in a single variable.
# Set = unordered + mutable + unique elements

#set is mutable
#Elements in set are immutable

set1={} # empty dictionary
print(type(set1))
set2=set() # empty set
print(type(set2))

set3={1,2,3,4,5}
print(set3)
print(type(set3))

set4={"avi",45,"avi",45} #set doesn't take duplicate values
#duplicate values are automatically removed
#set4[0]=10 # TypeError: 'set' object does not support item assignment
print(set4)


#set methods
set5={1,2,3,4,5}
set6={4,5,6,7,8}
print(set5.union(set6)) #union of two sets
print(set5.intersection(set6)) #intersection of two sets
print(set5.difference(set6)) #difference of two sets
print(set5.symmetric_difference(set6)) #symmetric difference of two sets

set6.add(9)
print(set6)

set6.remove(6)
print(set6)

set6.discard(9)
print(set6)

set6.pop()
print(set6)
set6.pop()
print(set6)

# set6.clear()
# print(set6)


#Data types allowed in set
    # Immutable types only allowed
    # Because sets use hashing,mutable objects can change
s = {10, 3.5, "avi", True, (1, 2)}
print(s)

#Accessing elements
#     # Indexing is not allowed
# print(s[0])   # TypeError: 'set' object is not subscriptable

for i in s:
    print(i)


#Add and remove
s={1,3,4}
s.add(7)
print(s)

s.remove(4)
print(s)

s.discard(7)
print(s)

s.pop()
print(s)
# s.clear()
# print(s)

s.add(10)
print(s)

s.update([11,12,13]) #multiple values allowed
print(s)

s.update([7,8],[9,5]) #multiple values allowed
print(s)


#subset and superset
a={1,2}
b={1,2,3,4,5}
print(a.issubset(b)) #subset
print(b.issuperset(a)) #superset

sc = {x*x for x in range(1, 6)}
print(sc)   # {1,4,9,16,25}




