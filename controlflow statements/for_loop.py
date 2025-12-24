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

