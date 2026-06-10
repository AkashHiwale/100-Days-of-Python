from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

menu = Menu()
coffer_maker = CoffeeMaker()
money_machine = MoneyMachine()

while user_input != "off":
    if user_input == "report":
        coffer_maker.report()
        money_machine.report()
    elif menu.find_drink(user_input.lower()).name == user_input.lower():
        drink = menu.find_drink(user_input.lower())
        if coffer_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffer_maker.make_coffee(drink)
    else:
        print("Invalid input. Please choose espresso, latte, cappuccino, report, or off.")
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()