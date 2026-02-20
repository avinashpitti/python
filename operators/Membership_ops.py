#Membership operators check whether a value exists inside a sequence
#Membership operators are in, not in
#works with string,list,tuple,set,dictionary(keys only)


#list
eids=[101,102,104,107]
print(101 in eids)
print(103 in eids)
print(105 not in eids)

#tuple
enames=('avi','balu','mahesh')
print('cherry' not in enames)

#set
sizes={'s','m','l','xl'}
print('xxl' in sizes)

# string
ename='rahul'
print('a' in ename)
print('z' in ename)

b=bytes({10,20,40,67})
ba=bytearray({45,43,12,23}) # bytearray must be in range(0,256)
fz=frozenset({10,10,10})
print(20 in b)
print(45 in ba)
print("frozenset",10 not in fz)

numbers=range(100) 
print(99 in numbers)
print(100 in numbers)

print("--------------------------")

name = "avinash"

print("avi" in name)     # True
print("nash" in name)    # True
print("Avi" in name)     # False (case-sensitive)

print("--------------------------")

student = {
    "name": "avi",
    "age": 22
}

print("name" in student)     # True
print("avi" in student)      # False
print("avi" in student.values())  # True


a=0.1+0.2
print(a==0.3)

x=[1,2,3]
y=x[:]
z=x.copy()
print(id(z))



