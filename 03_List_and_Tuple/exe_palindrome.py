list1 = []
list1.append(input("Enter the first number: "))
list1.append(input("Enter the second number: "))
list1.append(input("Enter the third number: "))
list1.append(input("Enter the fourth number: "))
list1.append(input("Enter the fifth number: "))

b = list1.copy()
b.reverse()
if list1 == b:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")