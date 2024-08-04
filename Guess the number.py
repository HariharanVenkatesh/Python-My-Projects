#Project no 7 - Guess the number

import random
import logo_art
EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
        
def check_answer(Guessed_No,answer,attempts):
    if Guessed_No < answer:
        print("Your guess is to low")
        return attempts - 1
    elif Guessed_No > answer:
        print("Your Guesss is Too High")
        return attempts - 1
    else:
        print(f"Your Guess is Right..... The Answer was : {answer}")

def game():
    print(logo_art.logo)
    print("Let me think of a number between 1 to 50.")
    answer = random.randint(1,50)

    level = input("Choose level of difficulty....Type 'easy' or 'hard': ") 
    attempts = set_difficulty(level)
    if attempts != EASY_LEVEL_ATTEMPTS and attempts != HARD_LEVEL_ATTEMPTS:
        print("You have entered wrong difficulty level...Play Again!!!!")
        return
    Guessed_No = 0
    while Guessed_No != answer:
        print (f"You Have {attempts} Remaining to Guess the No ")
        Guessed_No = int(input("Guess a No: "))
        attempts = check_answer(Guessed_No,answer,attempts)
        if attempts == 0:
            print("You are out of Guess ......You lose !....")
            return   
        elif Guessed_No != answer:
            print("Guess Again")    

game()            
