#Step 4

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

end_of_game = False
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#TODO-1: - Create a variable called 'lives' to keep track of the number of lives left. 
#Set 'lives' to equal 6.

life = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter
        
    if guess not in chosen_word:
        life -= 1

    if life == 6:
        print(stages[0])
        print(f"you are left with {life} life ")
    elif life == 5:
        print(f"you are left with {life} life")
        print(stages[1])
    elif life == 4:
        print(f"you are left with {life} life ")
        print(stages[2])
    elif life == 3:
        print(f"you are left with {life} life ")
        print(stages[3])
    elif life == 2:
        print(f"you are left with {life} life ")
        print(stages[4])
    elif life == 1:
        print(f"you are left with {life} life ")
        print(stages[5])
        
    elif life == 0:
        print(f"game over mommy time now")
        
        break

        
        
    #TODO-2: - If guess is not a letter in the chosen_word,
    #Then reduce 'lives' by 1. 
    #If lives goes down to 0 then the game should stop and it should print "You lose."

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")
    
    #TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.