import math

print(type(math))

# Math constants

print(math.pi)
print(math.e)
print(math.inf)
print(math.nan)

# Math Functions

print(math.isqrt(23))
print(math.sqrt(23))
# print(math.sqrt(-9)) # ValueError: math domain error
import cmath
print(cmath.sqrt(-9)) # output :3j

print(math.isqrt(25)) # To get int
print(math.sqrt(25)) # To get floor

print(math.pow(2,6)) # To get floor
print(math.pow(3,4)) # To get floor
print(3**4) # To get int

print(round(2.499))
print(round(2.51))
print(round(2.5))#if it's point 5 it rounded to nearest even number
print(round(3.5))#if it's point 5 it rounded to nearest even number

 
print(math.floor(8.8)) # rounds down
print(math.ceil(8.8)) # rounds up

a=0.1
b=0.2

print(float(a+b)) # floats are stored in binary.so they are inaccurate

from decimal import Decimal
a=Decimal("0.1")
b=Decimal("0.2") # To get a precise value pass strings
print(float(a+b))


print(abs(-10)) # built in function
print(math.fabs(-10)) # function inside the math module


# Trigonometric functions (angles in radians, not degrees )
print("------Trigonometric functions-------")

# radian is a degree system (full circle =360 degrees)
# full circle= 2π
#half circle(180)=π
# quarter circle(90)=π/2

# why python uses radians
# Radians are natural to mathematics used in calculus,physics,engineering

print(math.sin(math.pi / 2)) # 90 degrees
print(math.sin(90)) # 90 radians # don't use like this 

angle=0
radian=math.radians(angle)
print(math.cos(radian))
print(math.sin(radian))
print(math.tan(radian))
print(math.acos(radian))
print(math.asin(radian))
print(math.atan(radian))

print(math.tan(math.pi / 2)) #computers can't represent infinity so they give large number instead


# logarithmic functions
print("----------logarithmic functions---------")

print(math.log(10))     # natural log (base e)
print(math.log10(100))   # base 10
print(math.log2(8))      # base 2


# Facorials: Only accepts non negative integers
print("-------factorials-------")

print(math.factorial(6))
print(math.factorial(4))

# GCD & LCM
print("------GCD & LCM--------")

print(math.gcd(12,18))
print(math.lcm(12,18))

# To check all available functions

print(dir(math))

# How do you explore a module
# dir(module) # here module can be anything like math random etc
# help(module)

# help

print("----help gives description, parameters  and return type")

# print(help(math.sqrt(25)))











