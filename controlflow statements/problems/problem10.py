marks=int(input("Enter number of marks:"))

if(marks<0 or marks>100):
    print("invalid marks")
elif(marks>=90 and marks <=100):
    print("Grade A")
elif(marks>=80 and marks <90):
    print("Grade B")
elif(marks>=70 and marks <80):
    print("Grade C")
elif(marks>=50 and marks <70):
    print("Grade D")
elif(marks>=35 and marks <50):
    print("Grade E")
elif(marks<35):
    print("Grade F")



# marks=int(input("Enter number of marks: "))

# if marks>40 and marks<=100:
#     print("qualified")

#     if marks >90 and marks <=100:
#         print("A Grade")
#     elif marks >80 and marks <=90:
#         print("B Grade")
#     elif marks >70 and marks <=80:
#         print("C Grade")
#     elif marks >55 and marks <=70:
#         print("D Grade")
#     elif marks >40 and marks <=55:
#         print("E Grade")
    
# elif marks>100 or marks <0:
#     print("Marks out of range,Enter correct marks")
# else:
#     print("Fail")
