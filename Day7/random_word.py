#Step 1 
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
chosen_word = random.choice(word_list)
print(chosen_word)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("chosen_word").lower()
#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

for word in word_list:
    if chosen_word == guess:
        print("you guess correct loser lucky mc")
    else:
        print("what else would someone expect from you ")
        break
