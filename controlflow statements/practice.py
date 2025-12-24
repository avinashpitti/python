score = 890

if score >= 90 and score <=100:
  print("Grade: A")
elif score >= 80 and score <90:
  print("Grade: B")
elif score >= 70 and score <80:
  print("Grade: C")
elif score >= 55 and score <70:
  print("Grade: D")
elif score >=40 and score <55:
  print("Grade: E")
elif score <40 and score >=0:
  print("Grade: F-Fail")
else:
  print("Invalid score")


user="avinasha"
if len(user)<8:
  print("Invalid user name")
else:
  print(f"{user} a Valid user name")

num=int(input("Enter a number:"))
if num%2==0:
  print("Even")
else:
  print("Odd")

# Given number is 3 digit or not
num=int(input("Enter a number:"))
if num>=100 and num<=999:
  print("3 digit number")
else:
  print("Not a 3 digit number")

enames=['sg','pg','rg','modi']
for ename in enames:
    print(ename)

print("----------------")

i=0
while i<len(enames):
    print(enames[i])
    i+=1

