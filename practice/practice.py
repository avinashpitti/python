#1
a = "5"
b = 3
print(a * b) # "555"(here b is converted into str)
print(int(a) + b) # 8(here we are converting a into int)
# print(a + b) # we can't concatenate str+int,so typerror

#2
a = [1, 2, 3]
b = a # b=a means both are referring to same object memory
b.append(4) # so appending one equal to appending both
print(a) # [1,2,3,4]
print(b) # [1,2,3,4]

c = a.copy() # Here c is a copy of a (it will have different memory)
c.append(5) # The append value is only added to c
print(a) # [1,2,3,4]
print(c) # [1,2,3,4,5]
# Note : Explain this problem clearly and also about
# aliasing vs copy vs shallow copy vs deep copy and hashable vs unhashable with examples

#3
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print(s1 & s2)# {3,4}(and returns common values in both the sets)
print(s1 | s2)# {1,2,3,4,5,6}(or returns all the values in sets by removing duplicates)
print(s1 - s2)# {1,2}(it prints values in s1 which are not in s2)
print(s1 ^ s2)#{1,2,5,6}(It's opposite to and)

#4
t = (1, 2, 3, 2, 1)# tuple allows heterogeneous elements
print(t.count(2))# count(2) is 2
print(t.index(3))# index of 3 is 2
# t[0] = 10 # tuple values are immutable (typeerror)

#5
d1 = {"a": 1, "b": 2}
d2 = {"b": 99, "c": 3}
merged = {**d1, **d2}
print(merged) 
