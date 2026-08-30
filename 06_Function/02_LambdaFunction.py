# Lambda Function -> it is an anonymous function (function without name) specified using 'lambda' keyword

#Syntax -> 
#   lambda arguments: expression

lambda_sum = lambda a,b : a + b 
print(lambda_sum(5, 3))

lambda_even = lambda num : True if num % 2 == 0 else False
num = int(input("Enter a number: "))
print(lambda_even(num))

