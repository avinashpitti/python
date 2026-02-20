# Logical operators are used to combine conditional statements
# Logical operators are and, or, not


age=25
if age>=18 and age<=60:
    print("Adult")
else:
    print("Not Adult")


print(5<7 and 5>7)
print(5<7 or 5>7)
print(not 5<7)



# In python, any non zero number is considered as true
# 0 is considered as false
print("the value of 10 and 20 is",10 and 20)
# and rule: Returns the first falsy value, or the last value if all are truthy.
#or rule: Returns the first truthy value, or the last value if all are falsy.
print("the value of 20 and 10 is",20 and 10)
print("the value of 0 and 10 is",0 and 10)
print("the value of 0 and 0 is",0 and 0)


# or returns the first true value
print("the value of 10 or 20 is",10 or 20)
print('the value of 20 or 10 is',20 or 10)
print("the value of not 10 is",not 10)

