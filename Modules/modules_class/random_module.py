import secrets
import random

random.seed(10) # It gives the same random value "if" the same seed value.
print(random.random()) 


print(f"It gives the random value b/w 0 and 1 : {random.random()}")

print(f'It gives the radom value b/w start and stop value: {random.randint(10,20)}')

print(f'random range value: {random.randrange(10)}')
print(f'random range value: {random.randrange(5,10)}')
print(f'random range value: {random.randrange(10,25,2)}')


# choice

marks=[71,35,89,44,71,88,89,78,90]
print(f"random marks: {random.choice(marks)}")

# choices : returns multiple random elements(duplicates allowed).

# It always returns a list

print(f"random marks: {random.choices(marks)}")
print(f"random marks(duplicates allowed): {random.choices(marks,k=3)}")

#sample: returns unique random elements(no duplicates)

print(f"random marks(no duplicates): {random.sample(marks,k=3)}")

# shuffle : works only on mutable types(lists)

random.shuffle(marks)
print(marks)

# uniform : returns a float b/w a and b

print(f"returns a float b/w a and b: {random.uniform(1.6,4.2)}")


# secrets: secrets is used to generate secure random values. 

import secrets

print(secrets.randbelow(10))#Safer replacement for random.randrange()

letters="ABCDEFGHIJ"
print(secrets.choice(letters))
#secure version of choice used for passwords. 


