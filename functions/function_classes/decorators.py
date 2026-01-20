# Decorator is a function,it takes one function as an argument,
# and modify the functionality and returns a modified function as a value.

# without decorators : not validating login status
def home_page(name,login_status):
    return 'home page'


def product_page(name,login_status):
    return 'product page'

def order_page(name,login_status):
    return 'order page'

def profile_page(name,login_status):
    return 'profile page'


print(home_page('RG',False))
print(product_page('RG',False))
print(order_page('RG',False))
print(profile_page('RG',False))


# with decorators

def login_req(func):

    def inner(name,login_status):
        if login_status==False:
            print("Login is Required")
        else:
            return func(name,login_status)
        
    return inner
    
def homeapage(name,logi_status):
    return "Home Page"

def productpage(name,logi_status):
    return "Product  Page"

@login_req
def orders(name,logi_status):
    return "Order Details Page"

@login_req
def profile(name,logi_status):
    return "Profile Page"

print(homeapage("RG",True))
print(productpage("RG",False))


print(orders("RG",False))


print(profile("RG",False))


#smart division decorator

def smart_div(func):
    def inner(a, b):
        if b == 0:
            print("cannot divide by zero")
        else:
            return func(a, b)
    return inner


@smart_div
def calc(a, b):
    print(a / b)


calc(10, 5)
calc(10, 0)







