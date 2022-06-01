import ingredients as ingredients
import money as money
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "ingredients": {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
}
resources['money'] = 0.0

def report(resources):
        print(resources)

def make_coffee(users_choice, resources):
    if users_choice == "latte":
        for key in resources['ingredients']:
            resources['ingredients'][key] -= MENU['latte']['ingredients'][key]
        print("Here is your latte. Enjoy!")
    elif users_choice == 'cappuccino':
        for key in resources['ingredients']:
            resources['ingredients'][key] -= MENU['cappuccino']['ingredients'][key]
        print("Here is your cappuccino. Enjoy!")
    else:
        for key in resources['ingredients']:
            resources['ingredients'][key] -= MENU['espresso']['ingredients'][key]
        print("Here is your espresso. Enjoy!")

def check_resources(users_choice, resources):
    if users_choice == "latte":
        for key in resources['ingredients']:
            if resources['ingredients'][key] < MENU['latte']['ingredients'][key]:
                return print("Sorry there is not enough " + key)
        resources['money'] += MENU['latte']['cost']
        make_coffee(users_choice, resources)
    elif users_choice == 'cappuccino':
        for key in resources['ingredients']:
            if resources['ingredients'][key] < MENU['cappuccino']['ingredients'][key]:
                return print("sorry there is not enough " + key)
        resources['money'] += MENU['cappuccino']['cost']
        make_coffee(users_choice, resources)
    else:
        for key in resources['ingredients']:
            if resources['ingredients'][key] < MENU['espresso']['ingredients'][key]:
                return print("sorry there is not enough " + key)
        resources['money'] += MENU['espresso']['cost']
        make_coffee(users_choice, resources)

def process_coins(users_choice, resources):
    quarter = float(input("Insert quarter coins "))
    dimes = float(input("Insert dimes coins "))
    nickel = float(input("Insert nickel coins "))
    pennies = float(input("Insert pennies coins "))
    total_coins_value = (quarter * 0.25) + (dimes * 0.10) + (nickel * 0.05) + (pennies * 0.01)

    if users_choice == "latte":
        if total_coins_value < MENU['latte']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        elif total_coins_value >= MENU['latte']['cost']:
            if total_coins_value > MENU['latte']['cost']:
                change = total_coins_value - MENU['latte']['cost']
                round(change)
                change = str(change)
                print("Here's your $" + change + " in change")

            check_resources(users_choice, resources)

    elif users_choice == "cappuccino":
        if total_coins_value < MENU['cappuccino']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        elif total_coins_value >= MENU['cappuccino']['cost']:
            if total_coins_value > MENU['cappuccino']['cost']:
                change = total_coins_value - MENU['cappuccino']['cost']
                round(change)
                change = str(change)
                print("Here's your $" + change + " in change")

            check_resources(users_choice, resources)

    else:
        if total_coins_value < MENU['espresso']['cost']:
            print("Sorry that's not enough money. Money refunded.")
            return
        elif total_coins_value >= MENU['espresso']['cost']:
            if total_coins_value > MENU['espresso']['cost']:
                change = total_coins_value - MENU['espresso']['cost']
                round(change)
                change = str(change)
                print("Here's your $" + change + " in change")

            check_resources(users_choice, resources)

coffee_machine = True

while(coffee_machine):
    users_choice = input("What would you like? (espresso/latte/cappuccino) ")

    if users_choice == "report":
        report(resources)
    elif users_choice == "latte" or users_choice == "espresso" or users_choice == "cappuccino":
        process_coins(users_choice, resources)
    elif users_choice == "off":
        coffee_machine = False



