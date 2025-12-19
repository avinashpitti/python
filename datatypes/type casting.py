# int() works only with numeric strings, whereas str() can convert any data type into a string
# a=int('avinash')
# b=26
# print(a+b) # ValueError: invalid literal for int() with base 10: 'avinash'
a="avinash"
b=str(26)
print(a+b)  # avinash26