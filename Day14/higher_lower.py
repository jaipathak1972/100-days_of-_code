import random 
import game_data
import art

# # make a logo 

print(art.logo)
# get list data from game_data and sperate them acording to  my need

SCORE = 0
swtich_off = True
account_b = random.choice(game_data.data)
while swtich_off:
    account_a = account_b
    account_b = random.choice(game_data.data)
    
   
    print(f"The name is {account_a['name']} he do {account_a['description']} and he is from  {account_a['country']}")

    print(art.vs)

    print(f"The name is {account_b['name']} he do {account_b['description']} and he is from  {account_b['country']}")
    user_input =input("choose Choose A or B").upper()
    if user_input == 'A' or user_input == 'B':
            if (user_input == 'A' and account_a['follower_count'] > account_b['follower_count']) or \
                (user_input == 'B' and account_b['follower_count'] > account_a['follower_count']):
                print("Correct! You guessed the account with more followers.")
                SCORE += 1
            else:
                print("your answe is incoorect you lose : ")
                print(SCORE)

                play_again = input("Do you want to play again? (yes/no): ").strip().lower()
                if play_again == 'no':
                    swtich_off = False
    else:
        print("invalid input please type A oR B")
        
    