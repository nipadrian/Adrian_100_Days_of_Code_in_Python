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

resources["money"] = 0

# TODO: 1. Print report of all coffee resources - should include current resources
# Water, milk, coffee, money
def current_resources():
    print(f"These are the current available resources: ")
    for key in resources.keys():
        print(f"{key}: {resources[key]}")

# TODO: 6. Check transaction successful

def check_transaction(coins,coffee_type):
    cost = MENU[coffee_type]["cost"]

    if coins < cost:
        print("Sorry that's not enough money. Money refunded")
    elif coins >= cost:
        resources["money"] += cost
        change = round(float(coins - cost),3)
        print(f"Here is ${change} in change.")
        make_coffee(coffee_type)

# TODO: 7. Make coffee

def make_coffee(coffee_type):
    resources["water"] -= MENU[coffee_type]["ingredients"]["water"]
    if "milk" in MENU[coffee_type]["ingredients"]:
        resources["milk"] -= MENU[coffee_type]["ingredients"]["milk"]
    resources["coffee"] -= MENU[coffee_type]["ingredients"]["coffee"]
    print(f"Here is your {coffee_type}. Enjoy!")

# coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()
#
# while coffee_type != "off":
# # TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
# # Needs to be shown every time action has completed or after teh drink has been dispensed/for the next customer
#     check_resources()
#
#
#     coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()

# TODO: 5. process coins

def process_coins(coffee_type):
    print("Please insert coins.")
    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickles = int(input("How many nickles?"))
    pennies = int(input("How many pennies?"))
    total_coins = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    print(f"You have ${total_coins}.")
    check_transaction(total_coins,coffee_type)

# TODO: 3 anytime user enters "OFF" the machine turns off and execution should end

# TODO: 4. Check if resources are sufficient

def check_resources():
    # if coffee_type == "espresso":
    # elif coffee_type == "latte":
    # elif coffee_type == "cappuccino":
    if coffee_type == "report":
        current_resources()
    elif MENU[coffee_type]["ingredients"]["water"] > resources["water"]:
        print("Sorry there is not enough water")
    elif MENU[coffee_type]["ingredients"]["coffee"] > resources["coffee"]:
        print("Sorry there is not enough coffee")
    elif "milk" in MENU[coffee_type] and MENU[coffee_type]["ingredients"]["milk"] > resources["milk"]:
        print("Sorry there is not enough milk")
    else:
        process_coins(coffee_type)



# TODO: 8. Once all resources deducted - tell user "Here is your latte. Enjoy!"
# if that was their choice of drink
coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()

while coffee_type != "off":
    # TODO: 2. Prompt user by asking "What would you like? (espresso/latte/cappuccino):"
    # Needs to be shown every time action has completed or after teh drink has been dispensed/for the next customer
    check_resources()

    coffee_type = input("What would you like? (espresso/latte/cappuccino):").lower()