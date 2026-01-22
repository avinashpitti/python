f=open('write.txt','r+')
data=f.read()
print(f.tell())
print(data)
f.write('rey')
f.close()

f=open('write.txt','r+')
print(f.tell())
f.write('java is an enterprise language')
# In r+ mode:
# Writing happens at the current cursor position.
# - If we read first, the cursor moves to EOF, so write() appends.
# - If we write first, the cursor is at start (0), so write() overwrites from beginning.
# r+ never automatically appends or overwrites
# It always writes where the cursor currently is
data=f.read()
print(data)
f.close()
