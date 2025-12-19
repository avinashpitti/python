#Bitwise operators work on binary (0s and 1s) of integers.
#Bitwise operators are & | ^ ~ << >>
# & is and
# | is or
# ^ is xor
# ~ is not
# << is left shift
# >> is right shift


#Bitwise AND
#Result is 1 if both bits are 1 else 0

print("bitwise and",10 & 5)

#Bitwise OR
#Result is 1 if any of the bits is 1

print("bitwise or",10 | 5)

#Bitwise XOR
#Result is 1 if only one of the bits is 1

print("bitwise xor",10 ^ 5)


#Bitwise NOT
#Result is 1 if the bit is 0

print("bitwise not",~10) #~n = -(n + 1) output is -11
print("bitwise not",~-10) #~n = -(n + 1) output is 9



#Bitwise Left Shift
#Result is 1 if the bit is 0

print( "bitwise left shift",10 << 3) #output is 80
#shifts bits left multiple by 2. # 2**3 = 8     # 10 * 8 = 80



#Bitwise Right Shift
#Result is 1 if the bit is 0

print("bitwise right shift",10 >> 2) #output is 2
#shifts bits right divide by 2. #floor division apply
# 10 // 2 = 5
# 5 // 2 = 2



