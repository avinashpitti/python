#A tuple is a built-in Python data type used to store multiple values in a single variable.
#parathenses are not mandatory for tuple
#comma is what creates a tuple
#tuple is immutable(read only)
a,b=10,20 
#If values match variables → unpacking → basic data types
#If many values go to one variable → tuple
c=30,40
d=(50,60)

e=(70) # int
f=(80,) # tuple 
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("type of a is",type(a))
print("type of b is",type(b))
print("type of c is",type(c))
print("type of d is",type(d))
print("type of e is",type(e))
print("type of f is",type(f))


#tuple methods
g=(2,1,3,1,4,5,1)
print("count of 1 is",g.count(1)) #counts the number of times 1 appears in the tuple
print("index of 2 is",g.index(2)) 
print("index of 1 is",g.index(1)) #returns the index of 1st appearance of 1


# Tuple with different datatypes
tup1=(1,2.9,"hello",True)
for value in tup1:
    print(value)
    
tup2=("avi",45,False,6.7)
for value in tup2:
    print(value,end=" ")


#Accessing tuple elements
print(tup2[0])
print(tup2[1])
print(tup2[2])
print(tup2[3])


#slicing
tup3=(1,2,3,4,5,6,7,8,9,10)
print(tup3[1:5])
print(tup3[1:8:2])
print(tup3[1:5:-1])


# Immutable:Adding/removing/updates are not allowed
# tup4=(1,2,3,4,5)
# tup4[0]=10 # TypeError: 'tuple' object does not support item assignment


# Tuple with loop
tup5=(11,12,13,14,15)
for value in tup5:
    print(value)


# Tuple packing and unpacking
#packing
t=10,20,30

#unpacking
a,b,c=t
print(a,b,c)
print(type(t)) #tuple
print(type(a)) #int
print(type(b)) #int
print(type(c)) #int

#using *
a,*b=10,20,30,40,50
print(a)
print(b)
print(type(a)) #int
print(type(b)) #list


# Nested tuple
nest=(1,2,3,(4,5,6),("avi",45))
print(nest)
print(type(nest))
print(nest[3])
print(nest[4][0])

