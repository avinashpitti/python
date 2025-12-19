#create
def greet():
    print("Hello")

#read
greet()

#update # we update by redefining the function
def greet():
    print("Hello, avinash")
greet()

#delete # we delete by using del keyword
del greet
greet() # NameError: name 'greet' is not defined