#1
x = 10
print(x > 5 and x < 20)# True and True --> True
print(x > 5 and x < 8)# True and False --> False
print(x > 5 or x < 8)# True or False --> True

#2
lst = [1, 2, 3, 4, 5]
print(3 in lst) # True
print(6 not in lst) # True
print(6 in lst) # False

#3
print(not True) # False
print(not False) # True
print(not 0) # True
print(not 1) # False

#4
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a is b) # True(same memory location)
print(a is c) # False (different memory location)
print(a == c) # True (equality operator just looks for values)

#5
x = 5
y = 10
z = 15
print(x < y and y < z) # True and True --> True
print(x > y or y < z) # False or True --> True
print(not(x > y)) # True

#6
d = {"name": "Avinash", "age": 20}
print("name" in d) # True
print("Avinash" in d) # False
print("age" not in d) # False