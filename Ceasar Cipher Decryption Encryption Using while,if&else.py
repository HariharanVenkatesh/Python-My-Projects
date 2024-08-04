#Project no 4 - Ceasar Cipher

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
           'n','o','p','q','r','s','t','u','v','w','x','y','z']

def Encryption(plain_text,shift_key):
    cipher_text = ""
    for char in plain_text:
        if char in letters:
            position = letters.index(char)
            new_position = (position + shift_key)%26
            cipher_text += letters[new_position]
        else:
            cipher_text += char   
    print(f"Here's is the text after Encryption: {cipher_text}")

def Decryption(cipher_text,shift_key):
    plain_text = ""
    for char in cipher_text:
        if char in letters:    
            position = letters.index(char)
            new_position = (position - shift_key)%26
            plain_text += letters[new_position]
        else:
            plain_text += char
    print(f"Here's is the text after Decryption: {plain_text}")

wanna_end = False
while not wanna_end:
    what_to_do = input("Type 'Encrypt' for Encryption,Type 'Decrypt' for Decryption: ")        
    text = input("Type your Message: ").lower()
    shift = int(input("Enter Shift key: "))
    if what_to_do == "Encrypt":
        Encryption(plain_text = text,shift_key = shift)
    elif what_to_do == "Decrypt":
        Decryption(cipher_text = text,shift_key=shift)
    play_again = input("Type 'Yes' to Continue,Type 'No' to exit: ")    
    if play_again == 'No':
        wanna_end = True
        print("Have a Nice day!! Bye...")

