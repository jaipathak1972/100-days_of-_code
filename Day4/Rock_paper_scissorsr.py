import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Get user input
user_input = input("Enter rock, paper, or scissors: ").lower().strip()


if user_input == "rock":
    print(rock)
elif user_input == "paper":
    print(paper)
elif user_input == "scissors":
    print(scissors)
else:
    print("wrong input")

# Generate a random number between 0 and 2
random_number = random.randint(0, 2)

# Map the random number to the computer's choice
if random_number == 0:
    computer_choice = "rock"
    print(rock)
elif random_number == 1:
    computer_choice = "paper"
    print(paper)
else:
    computer_choice = "scissors"
    print(scissors)

# Determine the winner
if user_input == computer_choice:
    print("It's a tie!")
elif user_input == "rock" and computer_choice == "scissors":
    print("You win!")
elif user_input == "paper" and computer_choice == "rock":
    print("You win!")
elif user_input == "scissors" and computer_choice == "paper":
    print("You win!")
else:
    print("You lose!")
