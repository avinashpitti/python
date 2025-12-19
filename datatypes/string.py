# string is a datatype that stores a sequence of characters enclosed in single or double quotes
#strings are immutable(read only)
name="avinash"
print(name)
print(type(name))

# In Python, almost any data type can be converted into a string using the str() function.
num=str(123)
print(num)
print(type(num))

nums="134"
print(nums)
print(type(nums))

#Indexing
# Indexing : is used to access the characters in a string
# positive indexing : starts from 0
# negative indexing : starts from -1

a='hello world'
print(a[0])
print(a[4])
print(a[-1]) #negative indexing



#Slicing
# Slicing : is used to access a part of the string

college="siddhartha"
print(len(college))
print(college[0:5])
print(college[5:])# If we dont provide end index it considers till the end from 5th character
print(college[:5])# If we dont provide start index it considers from the start till 5th character
print(college[0:11])
print(college[0:11:2])#start,stop,step
print(college[::3]) # It's not necessary to provide start and end index
print(college[::-1])
print(college[-1:-6])
print(college[-9:-2])

#string operators
# + : concatenation
# * : repetition

#concatenation
# It's used to combine two or more strings
name="avinash"
print(name+"kumar")
# python doesn't automatically add space
print(name+"26")
print("avinash"+"is"+"learning"+"python")
print("avinash "+"is "+"learning "+"python")
print("avinash"+" "+"is"+" "+"learning"+" "+"python")

#repetition
# It's used to repeat a string
print("avinash"*3)
print("avinash "*4)
college="siddhartha"
print(college*3)
print(college*0)

#membership operator
# It's used to check if a character is present in a string
city="hyderabad"
print("hy" in city)
print("delhi" in city)
print("hy" not in city)

#Escape sequence characters
# Escape Sequence,Description,Example
# \'    Single Quote       'It\'s raining'
# \"    Double Quote       "He said, \"Hello\""
# \\    Backslash          C:\Users\Documents
# \n    New Line           Hello\nWorld (Moves to next line)
# \t    Tab                Name:\tAlice (Adds a large space)
# \b    Backspace          Hello \bWorld (Removes the space)"

print("It\'s raining")
print("He said, \"Hello\"")
print("C:\\Users\\Documents")
print("Hello\nWorld")
print("Name:\tAlice")
print("Hello \bWorld")  

#string methods

#1.case conversion:
#lower() : converts all characters to lowercase
#upper() : converts all characters to uppercase
name="Avinash"
print(name.lower())
print(name.upper())
text="hello this is avinash. I am learning python full stack."
print(text.title()) #It converts the first character of each word to uppercase
print(text.capitalize()) #It converts the first character of the string to uppercase
print(text.swapcase()) #It converts uppercase to lowercase and lowercase to uppercase


#2.Remvoing spaces
country="  india  is my country  "
print(country.strip()) #It removes spaces from the start and end
print(country.lstrip()) #It removes spaces from the start
print(country.rstrip()) #It removes spaces from the end


#3.Replace
course=" I am learning java"
print(course.replace("java","python")) #It replaces a string with another string


#4.Split and join
#split() : It splits a string into a list of substrings
city="hyderabad"
print(city.split("d"))
my_city="hyderabadar" #here split removes d and returns before first d as one substring 
#after first d as another substring till netxt d then after another string
print(my_city.split("d"))

text="python is fun."
print(text.split(" "))

fruits="apple,banana,cherry"
print(fruits.split(","))

#join() : It joins a list of strings into a string
words=["hello","world"]
print(" ".join(words))  


#5.searching
s='python'
print(s.find('th')) #It returns the index of the first occurrence of the substring
t="I am a student"
print(t.count("a")) #It returns the number of occurrences of the substring
print(t.index("a")) #It returns the index of the first occurrence of the substring
print(s.startswith("py")) #It returns True if the string starts with the specified value
print(s.endswith("o")) #It returns True if the string ends with the specified value


#6.checking content
#isalnum() : It returns True if all characters are alphanumeric
#isalpha() : It returns True if all characters are alphabets
#isdigit() : It returns True if all characters are digits
#islower() : It returns True if all characters are lowercase
#isupper() : It returns True if all characters are uppercase
#isspace() : It returns True if all characters are spaces

print("checking content")
print("python123".isalnum())
print("python".isalpha())
print("123".isdigit())
print("python".islower())
print("PYTHON".isupper())
print(" ".isspace())
