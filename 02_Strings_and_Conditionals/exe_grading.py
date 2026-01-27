name = input("Enter your name: ")
marks = int(input("Enter your marks (0-100): "))

if marks >= 90 and marks <= 100:
    grade = 'A'
elif marks < 90 and marks >= 80:
    grade = 'B'
elif marks < 80 and marks >= 70:
    grade = 'C'
elif marks < 70 and marks >= 60:
    grade = 'D'
else:
    grade = 'E'
    
print(name + ", your grade is: " + grade)