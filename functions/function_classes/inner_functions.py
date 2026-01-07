def outer():
    print('outer function starts')

    def inner():
        print('Inner function')

    inner()
    inner()
    inner()

outer()
outer()

print("*****************************")


def outer():
    print('outer function started')

    def inner():
        print(" This is inner function")
    
    return inner

x=outer()()


print("*****************************")

def outer():
    print('outer function started')

    def inner():
        print("inner function")
    
    return inner

x=outer()
x()
x()
x()

print("*****************************")

def out():
    name='avinash'
    def inside():
        print('Hello',name)
    inside()
out()

print("*****************************")


def outsid():
    name='srinvas'
    def insid():
        print('Hello',name,'Bro')
    insid()
outsid()

print("*****************************")


