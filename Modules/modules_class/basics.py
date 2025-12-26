#In Python, a module is simply a file containing Python code.
#  It can define functions, classes, and variables, 
# and it can also include runnable code.

# Types of modules

#1.Built in modules : pre installed in python eg: math,datetime
import math # it is used when we want to download complete math module
from math import sqrt,pi # It is used whne we need specific one or two etc
import math as m # It is used as an alias.instead of math. u can use it as m.
#2.External modules : installed using pip eg: numpy,pandas
#3.User defined modules : created by us

import govt
print(dir(govt))
# dir stands for directory
# The dir() function is like a Table of contents for a module. 
# It returns a sorted list of strings containing everyname inside
# that module, functions,variable,class,internal attributes(--buitlins--)



