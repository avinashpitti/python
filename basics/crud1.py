#create
eid=[101,102,103,104,105]
ename=["Avinash","Ajay","Anil","Arun","Amit"]
salary=[10000,20000,30000,40000,50000]

#read
print(eid)
print(ename)
print(salary)

#update
eid[3]=111
print(eid)
ename[2]="Anju"
print(ename)
salary[4]=33333
print(salary)

#delete
# del ename
# print(ename) #NameError: name 'ename' is not defined
del ename[3]
print(ename)