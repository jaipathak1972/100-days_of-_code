import art
print(art.logo)
dict_of_participent = {}

while True:

    name = input("Please the the name of the bitter :")
    price = input("Tell you bitting price :")

    dict_of_participent[name] = price

    again = input("Is there other you to bit yes or no :").lower()

    if again == "no":
        break

def highest_bitter():
    highest_bit = 0
    for key in dict_of_participent:
        bid_amount =int( dict_of_participent[key])
        if bid_amount > highest_bit:
            highest_bit = bid_amount
            winner = key

        
    print(f"highest bidder is {winner} with ${highest_bit}")

highest_bitter()