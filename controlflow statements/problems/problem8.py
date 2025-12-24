numbers=[7,18,31,232,1055,8,12]

for num in numbers:
    print(num)

i=0
while i< len(numbers):
    print(numbers[i],end=" ")
    i+=1

print("************************")


# print first 10 even numbers

i=0
number=0 # 0 is an even number
limit =10

while i<limit:
    if number%2==0:
        print(number)
        i+=1
    number+=1



#print first 10 odd numbers
i=0
number=1 # Initial number
limit =10

while i<limit:
    if number%2==1:
        print(number)
        i+=1
    number+=1


number=int(input("Enter number of even number:"))

i=2
while i<=number*2:
    print(i,end=' ')
    i+=2







