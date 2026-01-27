import random
print('''
   ___                            _     _              _  _                  _                
  / __|  _  _   ___   ___  ___   | |_  | |_    ___    | \| |  _  _   _ __   | |__   ___   _ _ 
 | (_ | | || | / -_) (_-< (_-<   |  _| | ' \  / -_)   | .` | | || | | '  \  | '_ \ / -_) | '_|
  \___|  \_,_| \___| /__/ /__/    \__| |_||_| \___|   |_|\_|  \_,_| |_|_|_| |_.__/ \___| |_|  
                                                                                              
''')
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 
           39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 
           57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 
           75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,  90, 91, 92, 
           93, 94, 95, 96, 97, 98, 99, 100]


attempts = 0 
print("Welcome to the Number Guessing Game/")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")   
else:
    print("Invalid difficulty level. Please restart the game and choose 'easy' or 'hard'.")

chosen_number = random.choice(numbers)
game_over = False
while not game_over:
    guess = int(input("Make a guess: "))
    if guess == chosen_number:
        print(f"You got it! The answer was {chosen_number}.")
        game_over = True
    elif guess < chosen_number:
        attempts -=1
        print("Too low.")
        print(f"You have {attempts} attempts remaining to guess the number.")
    elif guess > chosen_number:
        attempts -= 1
        print("Too high.")
        print(f"You have {attempts} attempts remaining to guess the number.")
        
    if attempts == 0:
        game_over = True
        print("You've run out of guesses, you lose.")
        print(f"The number was {chosen_number}.")
        
        
