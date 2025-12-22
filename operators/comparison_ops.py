#comparison operators are used to compare two values
# ==, !=, >, <, >=, <=
# The result is always boolean

#0, 0.0, "", [], {},(), None → False
#Everything else → True for ex: " ",1,"False"


a=10
b=10
print("a is equals to b",a==b)
print("a is not equals to b",a!=b)

c=12
d=34
print("c is greater than d",c>d)
print("c is less than d",c<d)
print("c is greater than or equal to d",c>=d)
print("c is less than or equal to d",c<=d)


print(5==5.0)


#strings(lexicographically-based on ascii values)
print("abc"=="abc")
print("abc">"def")
print("abc"=="Abc")
print("apple is greater than banana", "apple">"banana")


#chained comparison
x = 10
print(5 < x < 15)   
#same as
print(5 < x and x < 15)


#comparison vs identity operator
a = [1, 2]
b = [1, 2]

print(a == b)  # True (values same)
print(a is b)  # False (memory different)#identity operator


