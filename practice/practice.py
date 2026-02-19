#1
x = 10
y = 3
print(x / y) # 3.33 (division)
print(x // y) # 3 (floor division)
print(type(x / y)) # It divides as a normal division so float
print(type(x // y)) # floor division eliminates decimal part. So it becomes int

#2
s = "Hello, World!"
print(s[7:12]) # World(In slicing start value is included,end is not)
print(s[-6:-1]) # World(Negative indexing starts from -1, not 0)
print(s[::-1]) # !dlroW ,olleH(It reverses the string)
print(s[-1:-6]) # Expalin this to me in detail

#3
nums = [1, 2, 3, 4, 5]
nums.append(6)# [1,2,3,4,5,6](append adds at the end)
nums.insert(0, 0)# [0,1,2,3,4,5,6](inserting value 0 at index 0)
print(nums[::2])#[0,2,4,6](step value is 2)

#4
d = {"a": 1, "b": 2, "c": 3}
d["d"] = 4 # since key(d) is not exists, it creates one
del d["a"] # It deletes the key a
print(list(d.keys())) # {b,c,d}
print(d.get("a", "not found")) # we have used safe method get(so no error)



