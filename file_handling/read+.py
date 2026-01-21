f=open('write.txt','r+')
data=f.read()
print(f.tell())
print(data)
f.write('rey')
f.close()

f=open('write.txt','r+')
print(f.tell())
f.write('java is an enterprise language')
# If we write "write" before read it overwrites from start,
# If we write "read" before write it adds content at the end.
data=f.read()
print(data)
f.close()
