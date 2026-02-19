student={
    'name':'Avinash',
    'age':20,
    'grade':'A'
}

print(student['age'])
print(student.get('age'))

student['phone']=9898989898
print(student)

student['age']=23


print(student.items())
print(student.keys())
print(student.values())

for key in student:
    print(key)

for value in student.values():
    print(value)


print(student.get('age'))

#1
fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
fruits.remove('banana')
# fruits.pop(1)
print(fruits) # ['apple','cherry','orange']

#2
t = (1, 2, 3, 2, 1)
print(t.count(2)) #2
print(t.index(3)) #2

#3
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a & b) # {3,4}
print(a | b) # {1,2,3,4,5,6}
print(a - b) # {1,2}

#4
d = {"x": 10, "y": 20, "z": 30}
d["x"] = 99
d.pop("z")
print(d) # {'x :99,'y':20}

#5.
fruits = ["apple", "banana", "cherry"]
print(fruits[1:]) # ['banana','cherry']
print(fruits[:2]) # ['apple','banana']
print(fruits[-1]) # ['cherry']


#1
d = {"a": 1, "b": 2, "c": 3}
for key in d:
    print(key, d[key])

#2
lst = [1, 2, 3, 4, 5]
print(lst[::2])# [1,3,5]
print(lst[::-1])# [5,4,3,2,1]

#3
s = {1, 2, 3}
s.add(2) # Already exists (Duplicates are not allowed)
s.add(4) # It is added
print(s) # {1,2,3,4}

#4
t = (1, 2, 3)
lst = list(t) # [1,2,3]
lst.append(4) # [1,2,3,4]
t2 = tuple(lst) 
print(t2)# (1,2,3,4)

#5
d = {"name": "Alice", "age": 20}
print("name" in d) # 'Alice'
print("Alice" in d) # 