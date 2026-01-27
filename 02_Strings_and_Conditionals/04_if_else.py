name = input("Enter your name: ")
age = int(input("Enter your age: "))
clg_year = int(input("Enter the current year: "))

if age >= 18:
    print("You are eligible to vote, " + name + ".")    
else:
    print("You are not eligible to vote, " + name + ".")
    
if clg_year == 1:
    print("You are in your first year of college.")
elif clg_year == 2:
    print("You are in your second year of college.")
elif clg_year == 3:
    print("You are in your third year of college.")
elif clg_year == 4:
    print("You are in your fourth year of college.")
else:
    print("Invalid year entered.")