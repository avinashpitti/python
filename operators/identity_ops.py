#Identity operators check whether two variables refer to the
#SAME object in memory, not just the same value
#is, is not

# python usually gives small values same memory location
# but for large values it gives mostly different memory location
a=10
b=10
c=23376878996
d=23376878996
print("a is b",a is b)
print("a is not b",a is not b)
print("c is d",c is d)

print("----------------")
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False


print("----------------")

#same reference
a = [1, 2]
b = a

print(a is b)  # True

print("----------------")






