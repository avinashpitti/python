age=int(input("Enter your age: "))
has_license=input("Do you have license? (yes/no):").lower()=="yes"

if age>18:
    if has_license:
        print("You can drive")
    else:
        print("you need license to drive")
else:
    print("You are under age")
