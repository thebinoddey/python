class Hello:
    def __init__(self): #everytime this line is going to be called when an object is created
        pass

#---------------------------------------------------------------------#   
class Car:
    car_type = "Sedan"  #class attribute
    model = None

    def __init__(self, model_no, year): #constructor
        self.model = model_no #object attribute
        self.year = year
        
car = Car("BMW M4", 2009)
print(car.model)  # Output: BMW M4 (obj attr > class attr)
print(car.year)   # Output: 2009
print(car.car_type)  # Output: Sedan

# car1 = Car()
# print(car1.model)  # Output: AttributeError since model is not set
# print(car1.year)   # Output: AttributeError since year is not set

#---------------------------------------------------------------------#

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers +=1
        user.following +=1

user_1 = User("001", "Binod")
user_2 = User("002", "Anil")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


