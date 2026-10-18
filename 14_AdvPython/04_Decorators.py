# A decorator is a function that takes another function as an argument, adds some kind of functionality to it, and returns a new function. Decorators are often used in Python to modify the behavior of functions or methods.

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def hello():
    print("Hello!")

hello()
    