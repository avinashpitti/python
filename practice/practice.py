nums=[1,2]
print(type(nums))
nums.append(3)
print(nums)
nums.append(4)
print(nums)
nums.pop()
print(nums)
nums.append(6)
# nums.extend([6])
print(nums)
print(len(nums))
nums.insert(1,1000)
print(nums)
# nums.remove(50) # removes by value, value error
nums.remove(3)
print(nums)
nums.pop(0)
print(nums)
print(nums.index(2))
print(nums)
print(nums.count(1000))
print(nums)
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)

numbers=[10,20,30]
numbers.append([40,50])
print(numbers)
numbers.extend(nums)
print(numbers)

numbers.extend([56,67,78,89,100])
print(numbers)


