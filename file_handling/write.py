f=open('write.txt','w') 
# If file doesn't exist it creates the empty file
data=f.write("Hello guys") 
# It writes the data you can't see output in terminal
# In write.txt file content would be Hello guys
print(data)
f.close()
print("****************write***************")

f=open('write.txt','w')
data=f.write("rich") 
# now in write.txt file contnet would be rich 
print(data)
f.close()
print("****************write(overwrites)***************")


f=open('write.txt','w')
data=f.writable()
print(data)
f.close()

print("****************boolean***************")




