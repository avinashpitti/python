#create
# ctr+d repeatedly to select same kind of characters like , ; etc.
# first you should select one of the character and then ctr+d

employees=[
    {"eid":101,"ename":"Avinash","salary":10000},
    {"eid":102,"ename":"Ajay","salary":20000},
    {"eid":103,"ename":"Anil","salary":30000},
    {"eid":104,"ename":"Arun","salary":40000},
    {"eid":105,"ename":"Amit","salary":50000}
]


#read
for employee in employees:
    print(employee)

#update
for employee in employees:
    if employee["eid"]==102:
        employee["salary"]=22222
        break
print(employees)

#delete
for employee in employees:
    if employee["eid"]==102:
        employees.remove(employee)
        break
print(employees)

