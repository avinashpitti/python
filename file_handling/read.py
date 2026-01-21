f=open('read.txt','r')
data=f.read() # It displays the data in text file
print(data)
f.close()
print("**********read************")


with open('read.txt', 'r') as f:
    data = f.read() # It is same as above, by using with we no need to close
    print(data)

print("**********read with************")

f=open('read.txt') # r mode is default, so it's optional to mention it.
data=f.readline() # It displays the firstline
print(data)
f.close()

print("**********readline(to display first line)************")

f=open('read.txt')
data=f.readline() # To display multiple lines we have to print multiple times
print(data)
print(data)
f.close()

print("**********readline(multiple)************")

f=open('read.txt','r')
data=f.readlines() # It reads all the lines in the textfile with \n
print(data)
f.close()

# read vs readline
# read() returns the entire file as a single string,
# while readlines() returns a list where each element is one line.
print("**********readlines(reads all lines)************")

f=open('read.txt','r')
data=f.readable() # Gives boolean value
print(data)
f.close() 

print("**********readable(boolean)************")

f=open('read.txt','r')
print(f.closed) # False
data=f.read()
print(data)
f.close()
print(f.closed) # True

print("**********closed(mostly not useful)************")

with open('read.txt', 'r') as f:
    for line in f:
        print(line.strip())


print("**********file iteration(preferred over readlines)************")






