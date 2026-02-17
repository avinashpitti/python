
# try :
#     a=int(input("Enter a first number : "))
#     b=int(input("Enter a second number : "))
# except TypeError as err:
#     print(err)
# except ZeroDivisionError as err :
#     print(err)
#     print('good morning')
# finally:
#     print('give the result, no matter what')
#     print(a/b)

with open('data.txt','w') as f :
    data=f.write('good morning, avinash')
    print(data)





