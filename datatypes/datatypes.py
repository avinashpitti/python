#Datatypes define the type of data stored in a variable
#There are 5 main datatypes in python   #1. Numeric datatypes
#2. Sequence datatypes
#3. Set datatypes
#4. Mapping datatypes
#5. Boolean datatypes

# Mutable → list, set, dict, bytearray

# Immutable → int, float, str, tuple, frozenset, bytes

price=399  #int
rating=3.8  #float
brand='MILDIN' #str
c=10+20j  #complex
discount=True  #bool 

print(type(price))
print(type(rating))
print(type(brand))
print(type(c))
print(type(discount))
print("***************")

colors=['red','blue','yellow'] #list
enames=("rahul","sonia","Priya") #tuple
sizes={'S','M','L','XL'} #set
specification={'fits':'Regular', 'size':'XXL'} #dict

print(type(colors))
print(type(enames))
print(type(sizes))
print(type(specification))

print("***************")

b=bytes([10,20,30,255]) #bytes
ba=bytearray([10,20,30,255]) #bytearray
fz=frozenset({10,20,10,20}) #frozenset
r=range(100) #range
nt=None #NoneType 

print(type(b))
print(type(ba))
print(type(fz))
print(type(r))
print(type(nt))