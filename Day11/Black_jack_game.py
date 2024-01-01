import random

def random_card():
    cards = [11,2,3,4,5,6,7,8,9,10.10,10,10]
    cards = random.choice(cards)
   
    return cards 
        
def add_up(cards):
    if sum(cards) == 21 and len(cards ) == 2:
        return 0
    if 11 in cards and sum(cards) > 21 :
        cards.remove(11)
        cards.append(1)
    return sum(cards)
    
def compare (user_score , computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score :
        return "computer wins "
    elif user_score == 0 :
        return "you win you have ace card"
    elif computer_score ==0 :
        return "computer win he have ace card"
    elif computer_score >21 :
        return "you  wins"
    elif user_score > computer_score :
        return " you wins"
    elif computer_score > user_score :
        return "computer wins"
    
        
def play_game():

    user_list = []
    com_list =  []
    for _ in range (2):
        user_list.append(random_card())
        com_list.append(random_card())
    
    while True:
        user_sum = add_up(user_list)
        com_sum = add_up(com_list)
        print(f"   Your cards: {user_list}, current score: {user_sum}")
        print(f"   Computer's first card: {com_list[0]}")

        if user_sum == 0 or com_sum == 0 or user_sum> 21:
            break
        else:
            user_add = input("press y if you want to add another card else press n :")
            if user_add == "y":
                user_list.append(random_card())
            else:
                break
    while com_sum != 0 and com_sum < 17:
        com_list.append(random_card())
        com_sum = add_up(com_list)

        print(f"   Your final hand: {user_list}, final score: {user_sum}")
        print(f"   Computer's final hand: {com_list}, final score: {com_sum}")
        print(compare(user_score=user_sum, computer_score=com_sum))    
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()