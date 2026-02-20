x=5
y=5.0
print(id(x))
print(id(y))
print(x ==y)
print(x is y)

print(10 and 20 and 30)
print(0 and 10)
print(0 and 0)
print(10 or 20)
print(20 or 10)
print(0 or 10)

a=0.1+0.2
print(a==0.3)

x=[1,2,3]
y=x[:]
print(x)
print(y)
print(x==y)
print(x is y)

student={
    'name':'avi',
    'sub':'python'
}

print('name' in student)
print('avi' in student.values())
print('sub' not in student)
print('python' in student.values())

