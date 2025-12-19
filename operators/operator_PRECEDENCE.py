#OPERATOR PRECEDENCE decides which operator is executed first
#It is same like bodmas in maths

'''
| Priority | Operator       | Meaning                      |
| -------- | -------------- | ---------------------------- |
| 1️⃣      | `()`           | Parentheses                  |
| 2️⃣      | `**`           | Exponent                     |
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



