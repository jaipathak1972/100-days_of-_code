# # Prompt user by asking “What would you like? (espresso/latte/cappuccino)

# water = 300
# milk = 200
# coffee = 100
# money = 0

# # Define the cost of each drink
# MENU = {
#     "espresso": {"cost": 1.5, "water": 50, "coffee": 18},
#     "latte": {"cost": 2.5, "water": 200, "milk": 150, "coffee": 24},
#     "cappuccino": {"cost": 3.0, "water": 250, "milk": 100, "coffee": 24},
# }

# def report():
#     print(f"water {water}ml")
#     print(f"Milk: {milk}ml")
#     print(f"Coffee: {coffee}g")
#     print(f"Money: ${money:.2f}")


# def check_resources(drink):
#     for ingredient, quantity in MENU[drink].items():
#         if ingredient != "cost" and globals()[ingredient] < quantity:
#             print(f"Sorry, there is not enough {ingredient}.")
#             return False
#     return True
# def process_coins(drink_cost):
#     print("please intert coins :")
#     quarters = int(input("How many quarters? ")) * 0.25
#     dimes = int(input("How many dimes? ")) * 0.10
#     nickels = int(input("How many nickels? ")) * 0.05
#     pennies = int(input("How many pennies? ")) * 0.01
#     total_inserted = quarters + dimes + nickels + pennies

#     if total_inserted < drink_cost:
#         print(f"you have interserted very less here you money back ${total_inserted}")
#         return False
#     elif total_inserted > drink_cost:
#         change = total_inserted - drink_cost
#         print(f"Here is ${change:.2f} in change.")

#     return True
# def make_coffee(drink):
#     for ingredient , quantity in MENU[drink].items():
#         if ingredient != "cost":
#             globals()[ingredient] -= quantity
#     global money
#     money += MENU[drink]["cost"]
#     print(f"Here is your {drink}. Enjoy!")



# while True:
#     user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
#     if user_input == "off":
#         break
#     elif user_input == "report":
#         report()
#     elif user_input in MENU:
#         if check_resources(user_input):
#             cost = MENU[user_input]["cost"]
#             if process_coins(cost):
#                 make_coffee(user_input)
#     else:
#         print("Invalid choice. Please choose from the menu.")



MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
profit =0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def is_resource_sufficient(order_ingredients):

    ''' tell if ingreadients is sufficent or not'''
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"soorry there is not enough {item}.")
            return False
    return True

def process_coin():

    ''' return coins'''
    print("Please insert coins.")
    total = int(input("how many quarters")) * 0.25
    total += int(input("how many demes")) * 0.1
    total += int(input("how many nicjles")) * 0.05
    total += int(input("how many peennies")) * 0.01

    return total


def successful(money_received , drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost,2)
        print(f"refund {change}") 
        return True
    else:
        print("sorry thats not enough ")

        return False

is_on = True

def make_coffee(drink, order_ingredients):

    for item in order_ingredients:
        resources[item ] -= order_ingredients[item]
    print(f"Here is your {drink}")




while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice =="off":
        is_on =False
    elif choice == "report":
        print(f"water: {resources['water']}ml,")
        print(f"milk: {resources['milk']}ml,")
        print(f"coffee: {resources['coffee']}g,")
        print(f"money: ${profit}")

    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coin()
            if successful(payment, drink['cost']):
                make_coffee(choice, drink["ingredients"])
