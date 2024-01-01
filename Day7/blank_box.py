#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
display = []
for letter in chosen_word:
    display += "_"
    
while True:
    

    guess = input("Guess a letter: ").lower()


    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] =letter
            manage = display
    
    
    
    print (manage)

    if "_" not in display:
        print("loser you win how you felling")
        break

      

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
