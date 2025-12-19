#string formatting
#f-string is the best and recommended way to format strings

#1. using % operator
name="avinash"
age=21
college="siddhartha"
print("I am %s %d years old and I am studying in %s college" % (name,age,college))

#2. using format() function
name="avinash"
age=21
college="siddhartha"
print("I am {} {} years old and I am studying in {} college".format(name,age,college))

#3. using f-string
name="avinash"
age=21
college="siddhartha"
print(f"I am {name} {age} years old and I am studying in {college} college")
