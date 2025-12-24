for i in range(20,10,-1):
    print(i)


# groceries=['sugar','milk','dal']

# for item in range(len(groceries)):
#     print(item)


print("______________________")

text="Helloworld"
for char in text:
    print(char)
    print("----------------")

for char in text:
    print(char)
print("----------------")




for char in text[:5]:
    print(char,end=" ")
print()
    

print("----------------")

employee={
    "id":101,
    "name":"avinash",
    "dept":"IT Services"
}

for emp in employee:
    print(emp)

for value in employee.values():
    print(value)

for key,value in employee.items():
    print(key,":",value)

print(employee["name"])
print(employee["id"])
print(employee["dept"])


for emp in employee:
    print(emp,employee[emp])



esal=int(input("Enter Salary:"))
if esal>=40000:
    print("Eligible for credit card")
else:
    print("Not Eligible for credit card")

# print the mutliplication table of a number

num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"*",i,"=",num*i)

# print the sum of first n natural numbers
n=int(input("Enter a number:"))
sum=0
for i in range(1,n+1):
    sum+=i
print("Sum of first",n,"natural numbers is:",sum)

