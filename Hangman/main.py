#Day 07: Hangman
#Step 01

import random
# from replit import clear
from hangman_words import word_list
from hangman_art import stages

#lives of user
lives = 6
 
# Randomly choosing a word from the word_list
chosen_word = random.choice(word_list)

#Testing code
print(f"Pssst, the solution is {chosen_word}.")

#Creating a empty list display
display = []
word_length = len(chosen_word)
for i in range(word_length):
    display += "_"

#Getting the input(letter) from user
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    # clear()
#Checking whether it is already guessed or not
    if guess in display:
        print(f"You have already guessed the letter '{guess}'! Give another guess.")

#Checking if the letter the user guessed(guess) is one of the letters in the choosen_word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess


    if guess not in chosen_word:
        print(f"You guessed '{guess}', that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    
    print(f"{''.join((display))}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])