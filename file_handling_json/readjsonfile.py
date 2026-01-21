import json 

fp=open('emp1.json','r')
employees=json.load(fp)

for emp in employees:
    print(emp['ename'])