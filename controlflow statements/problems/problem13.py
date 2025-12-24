

user="avinasha"
if len(user)<8:
  print("Invalid user name")
else:
  print(f"{user} a Valid user name")


enames=['sg','pg','rg','modi']
for ename in enames:
    print(ename)

print("----------------")

i=0
while i<len(enames):
    print(enames[i])
    i+=1
#Note: remember to increment i, or else the loop will continue forever.


# print the given user input is even or odd using ternary operator
n=int(input("Enter a number: "))

print("Even") if n%2==0 else print("odd")  


