



if "salaman":
    print("Still Bachelor")
else:
    print("we dont know")

enames=["RG","SG","PG","Modi"]

for ename in enames:
    print(ename)


eids=(101,102,103,101,102,103)
for eid in eids:
    print(eid)

uids={101,101,102,103,True}

for uid in uids:
    print(uid)

employees=[
    {'eid':101,'ename':'Rahul','gender':'M'},
    {'eid':102,'ename':'Sonia','gender':'F'},
    {'eid':103,'ename':'Priyanka','gender':'F'},
    {'eid':104,'ename':'Modi','gender':'M'}
]

for emp in employees:
    print(emp['ename'])


