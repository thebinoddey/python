import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

random_letters = [random.choice(alphabet) for _ in range(nr_letters)]
random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

password_list = random_letters + random_symbols + random_numbers
random.shuffle(password_list)

password = ''.join(password_list)
print(password)
