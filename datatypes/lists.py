#list is a collection of elements stored in a single variable
#list is mutable(read and write)
#list is ordered and allows duplicates

# In python list is a heterogenous data structure,meaning it can store
# elements of any datatype-including other lists,sets,dictionaries,tuples etc.

#create
a=[]  #empty list
b=[10,20,30,10,20,30,True,[],(),{}]
enames=['RG','SG','PG','Modi']

#read
print(a)
print(b)
print(enames)
#read list elements using index
print(enames[0]) #RG
print(enames[1]) #SG
print(enames[2]) #PG
#print(enames[8]) #IndexError:list index out of range
print("length of enames is",len(enames))

for ename in enames:
    print(ename)
#update
enames[0]="Rahul Gandhi"
print(enames)

#delete
del enames[1]
print(enames)
print("length of enames is",len(enames))

info=[1,2.6,'avinash',True,['apple','banana','cherry'],(10,20,30),{10,20,30},{'name':'avinash','age':21}]
print(info)
print(type(info))
print("length of info is",len(info))
print(info[4][1])


#slicing: similar to string
nums=[1,2,3,4,5,6,7,8,9,10]
print(nums)
print(type(nums))
print("length of nums is",len(nums))
print(nums[4])
print(nums[4:9])
print(nums[::2])
print(nums[::-1])
print(nums[1::2])
#membership operator
print(2 in nums)
print(20 in nums)
print(20 not in nums)

#list operators
a=[1,2,3]
b=[4,5,6]
print(a+b) #concatenation
print(a*3) #repetition


names=['avinash','varun','rakesh','amar','chandu',3,['samson','gill','abhishek','ishan'],-2,45,4.8]

print(names[6][1])

#linear search vs hashing
# “Linear search checks elements sequentially, 
# while hashing uses hash functions for direct access,
# making it much faster.”

#hashing is faster than linear search
#linear search is used in lists and tuples
#hashing is used in sets and dictionaries







