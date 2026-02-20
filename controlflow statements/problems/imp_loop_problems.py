#1
i = 0
while i < 3:
    print(i)
    i += 1
    if i == 2:
        continue
    print("Hello") 



#2
i = 1
while i <= 3:
    print(i)
    if i == 2:
        break
    i += 1

print("Done")

#3
i = 1

while i <= 3:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("Finished")


#4
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)