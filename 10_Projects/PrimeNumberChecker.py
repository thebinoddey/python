import math

def isPrime(number):
    if number < 1 :
        return "Enter a different number"
    elif number ==1:
        return "1 is neither prime nor a composite a prime number"
    elif number <= 2:
        return f"{number} is a prime number"
    elif number%2 == 0 or number %3 == 0:
        return f"{number} is not a prime number"
    elif number%5 == 0 or number % math.sqrt(number) == 0:
        return f"{number} is not a prime number"
    else:
        return f"{number} is a prime number"
       
    
number = int(input("Enter a number to check if it is prime: "))
print(isPrime(number))
        