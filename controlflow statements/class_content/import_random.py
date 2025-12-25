import random
# random is a built in python module
#random.random,random.randint etc are functions of random module

print(random.random()) #It gives the value between 0 and 1 like 0.75,032 # 1 excluded
print(f'value b/w 0 and 1 is : {random.random()}')

print(f"value between 1 and 100 is : {random.randint(1,100)}") # both the values are included

nums=[1,5,12.3,6.7,42,9,100,12]

print(f"random value of nums is : {random.choice(nums)}")
#choice don't allow duplicates. It returns element.
#choices allow duplicates it always a list even though we have 1 number
print(f"random value of nums is : {random.choices(nums)}")
print(f"random value of nums is : {random.choices(nums,k=3)}")


#sample
nums = [1, 5, 123, 67, 42, 5, 100, 12]
#random.sample() guarantees uniqueness of SELECTIONS, not uniqueness of VALUES.
# “random.sample() selects unique positions from the sequence.
# If the sequence itself contains duplicate values, those values can appear multiple times in the result.”
print(f"sample values : {random.sample(nums, 3)}")



# shuffle : It returns the values in random order by shuffling

fruits=['banana','apple','cherry','mango','dragon']
random.shuffle(fruits)
print(fruits)






