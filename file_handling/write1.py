f=open('write.txt','w')
print(f.tell()) # It tells initial cursor position
data=f.write('avinash')
# print(f.read()) # It can't read since cursor is not at start
print(f.tell()) # It tells cursor position after writing avinash
f.write('we are going to learn something.')
print(f.tell()) # It tells cursor position after writing we are going to learn something
print(data)

f.close()

print("*************writ(single line)***************")


f=open('write.txt','w')
f.write('hello\n')
f.write('avinash\n')
f.write('how are you doing\n')
f.write('recently\n')


print("*************writ(multiple line)***************")

