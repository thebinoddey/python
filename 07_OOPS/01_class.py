#Class: It is a blueprint for creating objects.

class student:
    name = "Binod Dey"
    age = 20
    cgpa = 9.75
    
s1 = student() #s1 is an object
print(s1.name) #accessing the name attribute of the student class
print(s1.age) #accessing the age attribute of the student class

print(type(s1)) #Output: <class '__main__.student'> (s1 is an object of student class)