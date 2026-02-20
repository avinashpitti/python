# check if a number is positive, negative or zero
num=int(input("Enter a number : "))
if (num > 0):
    print(f"{num} is positive")
elif(num<0):
    print(f'{num} is negative')
else:
    print(f'{num} is neither positve nor negative')


# Check if a number is even or odd
num=int(input('Enter a number : '))
print('even' if num%2==0 else 'odd')

# Take two numbers and print the largest.
num1=int(input('Enter first number : '))
num2=int(input("Enter second number : "))
if (num1 == num2):
    print(f"{num1} and {num2} are equal")
elif(num1 > num2):
    print(f"{num1} is the largest")
else:
    print(f'{num2} is the largest')


# Check if a person is eligible to vote(age>=18)
age=int(input('Enter your age : '))
print('eligible to vote' if age >= 18 else "not eligible to vote")


# Check if a number is divisible by both 3 and 5
num=int(input('Enter a number : '))
if (num!=0 and num % 3 ==0 and num % 5 ==0) :
    print(f'{num} is divisible by both 3 and 5')
else:
    print(f'{num} is not divisible by both 3 and 5')


# Take three numbers and print the largest among them
num1=int(input('Enter first number : '))
num2=int(input("Enter second number : "))
num3=int(input("Enter third number : "))

if (num1==num2==num3):
    print('all three are equal')
elif(num1==num2 and num1 > num3):
    print(f'{num1} and {num2} are equal and greatest')
elif(num2==num3 and num2 > num1):
    print(f'{num2} and {num3} are equal and greatest')
elif(num1==num3 and num1 > num2):
    print(f'{num1} and {num3} are equal and greatest')
elif(num1 > num2 and num1 > num3):
    print(f'{num1} is the greatest')
elif(num2 > num1 and num2 > num3):
    print(f'{num2} is the greatest')
else:
    print(f'{num3} is the greatest')

# Check if a year is leap year.
# Divisible by 4 
# But divisible by 100, not a leap year
# But divisible by 100, leap year

year = int(input('Enter year : '))
if year % 400 == 0:
    print(f'{year} is a leap year')
elif year % 100 == 0:
    print(f'{year} is not a leap year')
elif year % 4 == 0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')



# Take a mark(0-100) and print the grade:
# 90+ → A
# 80+ → B
# 70+ → C
# 60+ → D
# below 60 → F

marks=int(input('Enter number of marks : '))
if(marks > 100 or marks < 0):
    print("Invalid marks")
elif(marks >=90 and marks <=100):
    print('A')
elif(marks >=80 and marks < 90):
    print('B')
elif(marks >=70 and marks < 80):
    print('C')
elif(marks >=60 and marks < 70):
    print('D')
# elif(marks >=0 and marks < 60 ):
#     print('F')
else:
    print('F')


# Check if a number is between 1 and 100(inclusive)
num=int(input('Enter a number : '))
if (num >=1 and num <=100):
    print('Inclusive')
else:
    print('Exclusive')


# Take a character and check if it's a vowel or consonant.

char=input('Enter a character : ').lower()
if(char in ('a','e','i','o','u')):
    print(f'{char} is a vowel')
else :
    print(f'{char} is a consonant')
# Modify it to take both lower and uppercase, i tired .lower() it is showing error