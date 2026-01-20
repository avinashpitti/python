f=open('data.txt','r')
print(f.readable()) 
f.close()

print('********readable*****************')

f=open('data.txt','r')
print(f.read()) 
f.close()

print('**********read***************')


f=open('data.txt','r')
print(f.readlines()) 
f.close()

print('***********readlines**************')


f=open('data.txt','r')
print(f.readline()) 
f.close()

print('**********readline***************')


f=open('data.txt','r')
print(f.readline()) 
print(f.readline()) 
f.close()

print('***********readline twice**************')

f=open('data.txt','r')
print(f.readline(2)) # it will print first 2 characters
f.close()

print('**********readline(2)***************')


f=open('data.txt','r')
print(f.readlines(3)) # Python reads "hello\n" → 6 chars ≥ 3
#Even readlines(1) or readlines(5) will still read the whole line
f.close()

print('************readlines(2)*************')





