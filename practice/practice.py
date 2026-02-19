# swapping variables
a,b,c=10,5,7
a,b,c=b,c,a
print(a,b,c)

# Global vs Local variable
x=10
def fun():
    global x
    x=20
    print(x)
fun()
print(x)

# # deleting a variable
y=66
del y
# print(y)

# Type checking

z=2.22
print(isinstance(z,float))
a=34
print(isinstance(a,float))
print(isinstance(a,int))

#1
a,b=1,2
a,b=b,a
print(a,b) # output:2 1

#2
x=5
def func():
    global x
    x=12
    print(x)
func() #output: 12

#3
x = [1, 2]
y = x
y += [3]
print(x) #output: [1,2,3]

#4
total=23
total = total + 5 # It fails becomes we have not defined it
print(total)


#1
x = 10
def func():
    x = 20
    return x

print(func())
print(x)

#2
a = 5
b = a
a = a + 3
print(a, b)# output: 8 5

#3
def func():
    x = 10

func()
print(x)

#4
x = 1
x += 5
x *= 2
x -= 3
print(x) # output : 9

x = [1, 2, 3]
y = x.copy()
y.append(4)
print(x)
print(y)

print(bool(""))