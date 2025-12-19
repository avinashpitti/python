b=bytes([10,20,30,255,40])
print(type(b))
# b[0]=11 #bytes are immutable(read only), you can't modify elements
#values must be in range of 0 to 255


ba = bytearray([10,20,30,255,40])
print(type(ba))
ba[0] = 11
#ba[0] = 1111 #ValueError: byte must be in range(0, 256)
for value in ba:
    print(value)