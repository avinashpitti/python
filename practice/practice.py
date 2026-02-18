student={
    'name':'Avinash',
    'age':22,
    'address':{
        'city':'Bangalore',
        'state':'Karnataka',
        'zipcode':500037
    }
}

print(student)
print(type(student))
print(student['address'])
print(student['address']['city'])
print(student['address']['zipcode'])

student['address']['city']='Mysore'
print(student['address'])

print("********************")

for key,value in student.items():
    print(key,value)

for key,value in student['address'].items():
    print(key,value)


employees = {
    101: {"name": "Rahul", "age": 30},
    102: {"name": "Sonia", "age": 28},
    103: {"name": "Priya", "age": 25}
}

print(employees[102]['name'])
employees[103]["age"]=26
print(employees[103]["age"])

employees[104]={"name":"modi","age":45}

print(employees[104])
print(employees)

# printing the employees who is greater than 28

for emp in employees.values():
    if emp["age"] > 28 :
        print(emp['name'])


for emp in employees.values():
    if emp["name"].lower().startswith("p"):
        print(emp)

nums=[1,2,3,4]
squares={n*n for n in nums}
print(squares)

numbers=[1,2,3,4,5,6]
sqrs={n:n*n for n in numbers}
print(sqrs)

even_sqrs={n:n*n for n in numbers if n % 2==0}
print(even_sqrs)

students={
    'Rahul':85,
    "Sonia":92,
    'priyanka':78,
    'Modi':87
}

# students with marks >80

top_students={name:marks for name ,marks in students.items() if marks > 80}
print(top_students)

updating={name:marks+5 for name,marks in students.items()}
print(updating)

employees = {
    101: {"name": "Rahul", "age": 30},
    102: {"name": "Sonia", "age": 28},
    103: {"name": "Priya", "age": 25}
}

# for emp in employees.values() :
#     if emp["age"]>26:
#         print(emp)

filtered={
    emp_id:emp
    for emp_id,emp in employees.items()
    if emp['age']>25
}
print(filtered)