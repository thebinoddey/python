# Attributes and Methods in Class
class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def greet_user(self):
        return f"Hello, {self.username}!"