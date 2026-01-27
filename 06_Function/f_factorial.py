def factorial(a):
    if a==0 or a==1:
        return 1
    else:
        return a*factorial(a-1)

num = int(input("Enter a number: "))
print(f"The factorial of {num} is {factorial(num)}")