# Access Modifiers in Python are used to control the visibility and accessibility of class members (attributes and methods). They determine whether a member can be accessed from outside the class or only within the class itself. Python has three types of access modifiers:
class Employee:
    def __init__(self, name, dept, salary):
        self.name = name
        # 1. Public: Members declared as public can be accessed from anywhere, both inside and outside the class. By default, all members in Python are public.
        
        self._dept = dept
        # 2. Protected: Members declared as protected can be accessed within the class and its subclasses. In Python, protected members are indicated by a single underscore prefix (e.g., _protected_member).
        
        self.__salary = salary
        # 3. Private: Members declared as private can only be accessed within the class itself. In Python, private members are indicated by a double underscore prefix (e.g., __private_member).

a = Employee("Binod", "IT", 50000)
print(a.name)
#print(a.__dept) #error: can't be accessed indirectly
print(a._Employee__dept) #can be accessed


