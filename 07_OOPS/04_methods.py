# Class can have:
# - Methods: functions defined inside a class
# - data 

class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def display_info(self):
        return f"Student Name: {self.name}, ID: {self.id}"
    
student_1 = Student("Binod", "S001")
student_2 = Student("Jay", "S002")
print(student_1.display_info())  # Output: Student Name: Binod, ID: S001