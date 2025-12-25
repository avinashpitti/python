num=1

while num<5:
    print(num)
    num+=1 #without this it will run infinite times only 1


# #Infinite loop
# val=1
# while val<5:
#     print(val)


correct_password="Python"

while True:
    user_password=input("Enter your password: ")
    if user_password==correct_password:
        print("password is correct. You logged in!")
    else:
        print("password is incorrect. Try again!")


# correct_password = "Python"
# max_attempts = 3
# attempts = 0

# while attempts < max_attempts:
#     user_password = input("Enter your password: ")

#     if user_password == correct_password:
#         print("Password is correct. You logged in!")
#         break
#     else:
#         attempts += 1
#         print(f"Password is incorrect. Try again! Attempts left: {max_attempts - attempts}")

# else:
#     print("Too many failed attempts. Account locked!")



# correct_password = "Python"

# for attempt in range(1, 4):
#     user_password = input("Enter your password: ")

#     if user_password == correct_password:
#         print("Password is correct. You logged in!")
#         break
#     else:
#         print(f"Incorrect password. Attempts left: {3 - attempt}")
# else:
#     print("Too many failed attempts. Account locked!")

    

