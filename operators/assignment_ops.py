# Assignment operators are used to assign values to variables
# =, +=, -=, *=, /=, //=, %=, **=

# The basic assignment operator is =

# Rule to Remember

# ✔ Always write operator first, equals next
# ✔ +=, -=, *=, /= are valid
# ❌ =+, =-, =* are NOT compound operators



x=3
x+=2
print(x)

x=True
x+=2
print(x)

x=True
x-=2
print(x)

x = 10
x //= 3
print(x)


s = "py"
s *= 3
print(s)

x = 5
x *= 2 + 1
print(x)


#Python swaps values using tuple packing on the right-hand side and unpacking on the left-hand side.
a = 5
b = 10
a, b = b, a
print(a, b)
