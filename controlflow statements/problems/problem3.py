score=int(input("Enter your score: "))
attendance=int(input("Enter your attendance percentage: "))
submitted=input("Do you submitted your assignment? (yes/no)").lower()=="yes"

if score>40:
    if attendance>75:
        if submitted:
            print("you have passed in distinction due to assignment")
        else:
            print("you passed but with average marks")
    else:
        print("You just passed ")
else:
    print("You failed the exam")

