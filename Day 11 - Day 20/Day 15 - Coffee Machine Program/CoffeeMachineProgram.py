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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

total_money_spent = 0.0

def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money_spent}")

def check_resources(drink):
    for item in drink["ingredients"]:
        if resources[item] < drink["ingredients"][item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total_money

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        return True
    
def make_coffee(drink_name, drink):
    for item in drink["ingredients"]:
        resources[item] -= drink["ingredients"][item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

while user_input != "off":
    if user_input == "report":
        report()
    elif user_input in MENU:
        drink = MENU[user_input]
        if check_resources(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_input, drink)
                total_money_spent += drink["cost"]
    else:
        print("Invalid input. Please choose espresso, latte, cappuccino, report, or off.")
    
    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

