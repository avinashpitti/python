name='Avinash'
print(type(name))
print(name[-1])
print(name[0])
print(name[::-1])

msg='''
This is a 
multiline 
string
'''
print(msg)
print(type(msg))

print(msg[7])
print(msg[7:])
print(msg[7::3])

course='python'
# course[0]='j' # str object doesn't support item assignment
print(course)
course='j'+course[1:]
print(course)

sub=course.upper()
print(sub)

lang='  This   is   my  backend language   '
print(lang)
print(lang.strip()) # strip removes spaces from both the ends(front and end, not in between)

print(lang.replace('backend','frontend'))

# lang.replace('my','your') # This doesn't change, it works only when you store in a variable
# print(lang)

change=lang.replace('my','your')
print(change)

print(lang.find('i'))

print('hello'.find('l')) # number of l

f_name='avi'
l_name='nash'
print(f_name+l_name)

fname='United'
lname='Kingdom'
print(fname+lname)
print(fname+" "+lname)
print((fname+" "+lname+" ")*4)
print(fname*4)
print(fname+lname*4)
print((fname+lname)*4)
print((fname+lname+" ")*4)

# my_name=input('Enter a name : ')
# print(my_name[0])
# print(my_name[-1])
# print(my_name[::-1])
# print(len(my_name))

emps=['avi','balu','chandu']
for emp in emps:
    print(emp)

language=' javascript '
print(language.strip())
print(language.rstrip())
print(language.lstrip())

para='India is my country'
para=para.split(',')
print(para)

print("avinash".isalpha())
print("arun".isnumeric())
print("arun".islower())
print("arun".isalnum())

pro_language=' Javascript '
rem=pro_language.strip()
print(rem)
print(rem.lower())

if rem.lower().startswith('a'):
    print(rem)

else:
    print("Doesn't start with a")


casc='    '
print(casc)
print(type(casc))
casc=casc.lower().strip()
if casc=="":
    print('empty string')
elif casc.lower().startswith('a'):
    print('starts with a')
else:
    print("Doesn't start with a")
