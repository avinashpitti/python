f=open('write.txt','a+')
f.write("prostack academy")
f.seek(0) # without this you can't read because cursor is at end 
# "a+" always appends on write,
#  reading requires seek(0).
data=f.read()
print(data)
f.close()