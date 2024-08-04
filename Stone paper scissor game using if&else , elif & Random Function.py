#Project no 1 - Stone paper scissor game using if&else , elif & Random Function

import random
stone = '''
🪨
'''
paper = '''
📃
'''
scissor = '''
✂️
'''
game_images = [stone,paper,scissor]
user_choice = int(input("Enter your Choice: Type 0 for Stone,1 for paper,2 for scissors: "))
if user_choice >= 3 or user_choice < 0:
    print("You Entered a invalid number,Enter the valid number🥱.")
else: 
    print(game_images[user_choice])
    computer_choice =  random.randint(0,2)
    print("Computer Chose: ")
    print(game_images[computer_choice])
    if computer_choice == user_choice:
        print("It's a Draw 🤝")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose! 👎") 
    elif user_choice == 0 and computer_choice == 2:
        print("You Win 👍")
    elif computer_choice > user_choice:  #2>0
        print("You Lose! 👎")    
    elif computer_choice < user_choice:  #0<2
        print("You Win 👍")    