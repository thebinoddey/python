alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount):
    original_text = original_text.lower()
    
    cipher = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        cipher += alphabet[new_position]
        
    print(f"The encoded text is: ", cipher)
    
    
def decrypt(original_text, shift_amount):
    
    cipher = ""
    for letter in original_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        cipher += alphabet[new_position]
        
    print(f"The decoded text is: ", cipher)

if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)    