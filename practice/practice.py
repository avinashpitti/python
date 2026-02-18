student={
    'name':'Avinash',
    'age' :22,
    'course':'python',
    'gender':'Male'
}

print(type(student))
print(student['name'])
print(student['age'])
print(student)

for key in student:
    print(key)

for key,value in student.items():
    print(key,value)

print(student.keys())
print(student.values())

del student['age']
print(student)

student['city']='Bangalore'
print(student)

student['age']='65'
print(student)

# print(student('xyz')) # keyerror
print(student.get('xyz')) # None

print('Here we go')


for key,value in student.items():
    print(key,value)

print(student.keys())
print(student.values())
print(student.items())


for key in student:
    print(key)

print("**********************")
for value in student:
    print(value)

print("**********************")

for value in student.values():
    print(value)

print("**********************")


for value in student.items() :
    print(value)

print("**********************")

d={'x':10}
d.update({'x':50,'y':100})
print(d)