#OPERATOR PRECEDENCE decides which operator is executed first
#It is same like bodmas in maths
#Exponent has right to left associativity
#remaining all operators have left to right associativity
'''
| Priority | Operator       | Meaning                      |
| -------- | -------------- | ---------------------------- |
| 1️⃣      | `()`           | Parentheses                  |
| 2️⃣      | `**`           | Exponent (right to left)     |
| 3️⃣      | `+  -` (unary) | Unary plus/minus             |
| 4️⃣      | `*  /  //  %`  | Multiply, divide, floor, mod |
| 5️⃣      | `+  -`         | Addition, subtraction        |
| 6️⃣      | `<  <=  >  >=` | Comparisons                  |
| 7️⃣      | `==  !=`       | Equality                     |
| 8️⃣      | `not`          | Logical NOT                  |
| 9️⃣      | `and`          | Logical AND                  |
| 🔟       | `or`           | Logical OR                   |
| 🔚       | `=` `+=` etc.  | Assignment (last)            |
'''

print(10 - 2 ** 2 * 3)
print(10 > 5 and 3 < 1) # True and False = False
print(not True and False or True)
print(5 and 0 or 10)
x = 10
print(5 < x < 15)
print(5 > 3 == 3 < 4)
print(0 or 5 and 0 or 10)

print("----------------")
x = 4
x *= 1 + 2 ** 2 # 2 square 4 then add 1 then multiply with x
print(x)


print("----------------")
#Unary operators 
#Unary operators are operators that take only one operand
#Unary operators are + and -
#Unary + does nothing
#Unary - changes the sign of the operand
#It has less precedence that ** but more than * and / and %

print(-3 ** 2)#-9 (exponent has more precedence than unary)
print((-3) ** 2)#9 (unary has more precedence than exponent,it's inside
#Parentheses)

x = 4
print(-x * 2)# unary has more precedence than multiplication


print(2 ** 3 ** 2)
print((2 ** 3) ** 2)

print(0 or 1 and 2)

print(not False == True)# precedence of == is more than not

print(5 > 3 == 3 < 5)
# chained comparison:5 > 3 and 3 == 3 and 3 < 5

print(0 or 1 and 2)# precedence of "and" is more than "or"
# and / or return actual values, not always True/False

10 > 5 or 3 < 1 and 4 == 4
# True or False and True
# True or False
# True


print(1 and 0 or 1)

print(not 2 ** 2 == 4)
# precedence of "==" is more than "not"

print(3 < 4 < 5 == True)
# chained comparison:3 < 4 and 4 < 5 and 5 == True

print(3<4<5<6<7<8<9<10)

print(True + False * 3)
# True + False * 3
# True + 0
# 1

print(0 and 1 or 2 and 3)
# 0 and 1  = 0 (and returns first false value)
# 2 and 3 = 3 (and returns last true value)
# 0 or 3 =3
# 3

print(2 or 5)

















