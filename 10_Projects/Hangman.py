import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["mouse", "keyboard", "monitor", "computer", "printer"]

lives = 6

chosen = random.choice(words)
print(chosen)

placeholder = ""
word_length = len(chosen)
for position in range(word_length):
    placeholder += "_"
    
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter:").lower()

    display = ""
    for letter in chosen:
        if letter == guess:
            display += letter
            correct_letters.append(letter)  
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)
    
    if guess not in chosen:
        lives -= 1
    print(f"You have {lives} lives left.")
    
    if lives == 0:
        print("You lose!")
        game_over = True
        
    if "_" not in display:
        print("You win!")
        game_over = True
        
    print(stages[lives])