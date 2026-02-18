info=[10,20,30,2.22,True,{},[1,2,3,4,5,6,7,8],()]
print(type(info))
print(info)
print(len(info))
print(info[-2][1:4])

for inform in info:
    print(inform)

enames=['rahul','sonia','priyanka','modi']
print(enames)
print(enames[2]) # priyanka
# print(enames[8]) # Index out of range

for ename in enames:
    print(ename)

enames[0]='amit'
print(enames)

del enames[2]
print(len(enames))
print(enames)

nums=[2,3,4,5,6]
print(3 in nums) 
print(8 in nums)

a=[1,2,3]
b=[4,5,6]
print(a+b)
print(a*4)
print(b*2)


