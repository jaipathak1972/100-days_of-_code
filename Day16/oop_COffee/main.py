from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


is_on =True

while is_on:
    user = input("Enter which flavour coffee you want latte").lower()
    if user == "off":
        is_on = False
    elif user == "report":
        print(CoffeeMaker.report)
    else:
        drink = Menu.get_items(user)
        if CoffeeMaker.is_resource_sufficient(drink) and MoneyMachine.process_coins:
            CoffeeMaker.make_coffee
            