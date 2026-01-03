li=[1,2,3,4,5]
print(li)

li.append(6)#appends at the end
print(li)

li.extend([7,8,9])#extends at the end
print(li)

li.insert(2,10000)#inserts at the specified index
print(li)

li.remove(10000)#removes the specified element
print(li)

# li.remove(77) # value error
# print(li)

li.pop() #removes last element
print(li)

li.pop(2) #removes element at index 2
print(li)

# li.clear() #removes all elements from the list
# print(li)

li.copy() #returns a copy of the list
print(li)

li.count(2) #returns the number of times a specified value appears in the list
print(li.count(2))

li.index(2) #returns the index of the specified value
print(li.index(2))

li[2]=100 #updates the element at the specified index
print(li)

# li[10] # list assignment index out of range
# print(li)

li.reverse() #reverses the list
print(li)

li.sort() #sorts the list
print(li)

li.sort(reverse=True) #sorts the list in reverse order
print(li)

for i in li:
    print(i)

for i in range(len(li)):
    print(li[i])



#squared list
squares=[x*x for x in range(8)]
print(squares)

square=[x*x for x in range(1,8) ]
print(square)


# Nested lists
matrix=[[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
print(matrix[0])
print(matrix[0][1])
#print(matrix[1][3]) # IndexError: list index out of range


#typecasting 
#list of characters
print(list('python'))



