# Type Conversion(implicit): It's automatically done by python
a,b=1,2.0
sum=a+b
print("sum of a and b is",sum)
print(type(sum))


c,d=2,4.6
sum=c+d
print("sum of c and d is",sum)
print(type(sum))    

x,y="12","8"
sum=x+y
print("sum of x and y is",sum)
print(type(sum))

# p,q=4,"12"
# sum=p+q
# print("sum of p and q is",sum)
# print(type(sum)) # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("value of True+2 is",True+2)
print(type(True+2))
print("value of False+2 is",False+2)
print(type(False+2))


# Type Casting(explicit): It's manually done by programmer
a=1
b=2.0
sum=int(a+b)
print( "sum of a and b is",sum)
print(type(sum))

c,d=2,4.6
sum=int(c+d)
print("sum of c and d is",sum)
print(type(sum))

x,y="12","8"
sum=int(x)+int(y)
print("sum of x and y is",sum)
print(type(sum))

p,q=4,"12"
sum=p+int(q)
print("sum of p and q is",sum)
print(type(sum))

