#Static Method: Methods that do not use the "self" parmaeter

class User:
    @staticmethod  #decorator
    def greet():
        print("Hello, welcome to the User class!")
        
user1 = User()
user1.greet()  # Output: Hello, welcome to the User class