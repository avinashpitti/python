course='python'
print(type(course)) #str

x=3
print(type(x)) # int

y=4.1
print(type(y)) # float

z=3+4j
print(type(z)) # complex

students=['avinash','shruti','ramesh']
print(type(students)) # list

nums=(1,2.77,8,True)
print(type(nums)) # tuple

student={
    'name' : 'avinash',
    'age' : 22,
    'city':'bengaluru'
}

print(type(student)) # dict

info={}
print(type(info)) # empty dict

inform=set()
print(type(inform)) # empty set

information={1,2,3,4,2,2,8}
print(type(information)) # set

isStudent= True
print(type(isStudent)) # bool

x=None
print(type(x)) # NoneType

r=range(5)
print(type(r)) # range

b=bytes()
print(type(b)) # bytes

bb=bytes([1,2,157]) # bytes must be in range(0,256) # Immutable
print(type(bb)) # bytes

ba=bytearray()
print(type(ba)) # bytearray

baa=bytearray((1,2,46)) # bytearray must be in range(0,256) # Mutable
print(type(baa)) # bytearray

print(baa)

fs=frozenset()
print(type(fs)) # fronzenset

fs=frozenset((1,23,53)) 
print(type(fs))  # fronzenset

fs=frozenset({4,3,90})
print(type(fs)) # frozenset

