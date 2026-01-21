import json

fp1=open('emp1.json','r')
employees=json.load(fp1)

employees=json.load(fp1)

male_employees=[]

for emp in employees:
    if emp['gender']=='Male':
        male_employees.append(emp)

fp2=open('male_emp.json','w')
json.dump(male_employees,fp2)
print("New json file created")

fp1.close()
fp2.close()