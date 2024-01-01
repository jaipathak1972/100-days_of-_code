import art
import random

print(art.logo)
def number():
    return random.randint(1, 100)

random_num = number()

difficulty = input("Please chooose difficulty level Easy or Hard ").lower()
easy_life =10
hard_life =5


if difficulty == "easy":

    print(f"you choose {difficulty} so you have {easy_life} change ")

    while True:

        guessed_num =int(input("guess number between 1 to 100 :" ))

        if guessed_num == random_num :
            print("you guess it corret yes")
            break
        elif guessed_num < random_num :
            easy_life -= 1
            
            print("Too low")
            print (f"you have only {easy_life} left")
            if easy_life == 0:
                print("your life is endded you losse")
                break
        elif guessed_num > random_num :
            easy_life -= 1
            print("Too high")
            print (f"you have only {easy_life} left")
            if easy_life == 1:
                print("your life is endded you losse")
                break
            
elif difficulty == "hard":
    print(f"you choose {difficulty} so you have {hard_life} change ")

    while True:
        guessed_num =int(input("guess number between 1 to 100 :" ))

        if guessed_num == random_num :
            print("you guess it corret yes")
            break
        elif guessed_num < random_num and hard_life != 0  :
            hard_life -= 1
            
            print("Too low")
            print (f"you have only {hard_life} left")
            
        elif guessed_num > random_num and hard_life != 0:
            hard_life -= 1
            print("Too high")
            print (f"you have only {hard_life} left")

else:
    print("you have input wrong variable")
            


