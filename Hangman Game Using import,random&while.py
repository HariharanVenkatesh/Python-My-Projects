#Project no 3 - Hangman Game

import random
import Hangman_stages
import Word_file
lives = 6
choosen_word = random.choice(Word_file.Words_list)
print(choosen_word)
display = []
for i in range(len(choosen_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    gussed_letter = input("Guess a Letter: ").lower()
    for position in range(len(choosen_word)):
        letter = choosen_word[position]
        if letter == gussed_letter:
            display[position] = gussed_letter
    print(display)    
    if gussed_letter not in choosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You lose 👎")
    if '_' not in display:
        game_over = True
        print("You win 👍")
    print(Hangman_stages.stages[lives])
