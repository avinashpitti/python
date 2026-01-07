x=lambda a :a+7
print(x(4))

y= lambda b : b*4
print(y(5))

z= lambda c : c-4
print(z(32))


def myfunc(n):
    return lambda a:a*n

mydoubler=myfunc(7)
print(mydoubler(5))  


#Map object

#Normal
prices=[98,198,298,398]
def addplus(price):
    return price+1
map_obj=map(addplus,prices)
new_price=list(map_obj)
print(new_price)

#map
quantities=[33,44,55,66,77]
print(list(map(lambda n:n+1, quantities)))



# Filter object

#Normal
numbers=[1,2,3,4,5,6,7,8,9,10]

def check_even(num):
    return num%2==0

filter_obj=filter(check_even,numbers)
even_nums=list(filter_obj)
print(even_nums)

#Filter
nums=[11,12,13,14,15,16,17,18]

print(list(filter(lambda n:n%2==0,nums)))






