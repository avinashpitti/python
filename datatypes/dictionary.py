#A dictionary is a built-in Python data type 
#It stores data in key : value pairs.
#Duplicate keys are not allowed(keys must be unique)
#Duplicate values are allowed

d={}#empty dictionary

student = {
    "name": "Avinash",
    "age": 22,
    "course": "BCA"
}
print(student)


#Accessing dictionary elements
print(student["age"])
print(student["course"])
#<******safest way to access using "get"******>
print(student.get("name"))
print(student.get("gender")) #returns None if key is not found


#Methods
print(student.keys()) #returns all keys
print(student.values()) #returns all values
print(student.items()) #returns all items


#Adding/Removing/Updating
student={"college":"Siddhartha"}
print(student)


student.update({"gender":"Male"}) #update
student["age"] = 23 #update
print(student)

student.pop("age") #remove
print(student)

student.popitem() #remove last item
print(student)

student={"college":"Siddhartha"}
print(student)


#Nested dictionary
stud={
    "name":"avi",
    "score":{
        "maths":90,
        "english":80,
        "science":70
    },
    "course":"BCA"
}
print(stud)
print(stud["score"])
print(stud["score"]["maths"])


# Looping through dictionary
dic={"a":1,"b":2,"c":3}
for key in dic:
    print(key,dic[key])

for key,value in dic.items():
    print(key,value)

for key in dic:
    print(key)

for value in dic.values():
    print(value)

# Dictionary comprehension
squares = {x: x*x for x in range(1, 6)}
print(squares)




