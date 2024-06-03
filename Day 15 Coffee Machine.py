import os, time

# ! Drinks menu
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0
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

# ! Machine starts with no resources. 
resources = {
    "water": 0,
    "milk": 0,
    "coffee": 0,
}
money = 0


def clear():
    """Clear the screen"""
    os.system("cls")


def report():
    """Returns formatted resources from the coffee machine"""
    return f"""Water: {resources["water"]}ml
Milk: {resources['milk']}ml
Coffee: {resources['coffee']}g
Money: ${money:.2f}"""


def sufficient_resources(choice, MENU, resources):
    """Returns Boolean value if resources are sufficient, takes the user choice as input"""
    if resources["water"] >= MENU[choice]["ingredients"]["water"] and resources["coffee"] >= MENU[choice]["ingredients"]["coffee"] and resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
        return True
    else:
        return False


def refill(water, milk, coffee, amount):
    """Refill the machine, takes input for all ingredients and takes out all the money"""
    resources["coffee"] += coffee
    resources["water"] += water
    resources["milk"] += milk
    global money
    money -= amount

def calculate_change(amount, cost):
    return amount - cost

power_on = True

while power_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        power_on = False
        break
    elif choice == 'refill':
        report()
        water_fill = int(input("how much water?: "))
        coffee_fill = int(input("how much coffee?: "))
        milk_fill = int(input("how much milk?: "))
        take_money = money
        refill(water=water_fill,milk=milk_fill,coffee=coffee_fill,amount=take_money)
        print("Here are the new resources: ")
        print(report())
        time.sleep(3)
        clear()
    elif choice == 'report':
        print(report())
        time.sleep(3)
        clear()
    else:
        if sufficient_resources(choice=choice, MENU=MENU, resources=resources):
            print(f"{choice} is ${MENU[choice]["cost"]:.2f}. please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))
            total_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            while MENU[choice]["cost"] > total_amount:
                if input("please insert more coins or type 'no' to cancel: ").lower() == 'no':
                    print(f"money refunded. here is your ${total_amount:}")
                    break
                else:
                    
                    quarters = quarters + int(input("How many quarters?: "))
                    dimes = dimes + int(input("How many dimes?: "))
                    nickles = nickles + int(input("How many nickles?: "))
                    pennies = pennies + int(input("How many pennies?: "))
                    total_amount = total_amount + (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
            money += MENU[choice]["cost"]
            if calculate_change(cost=MENU[choice]["cost"], amount=total_amount) != 0:
                print(f"Here is ${calculate_change(cost=MENU[choice]["cost"], amount=total_amount):.2f} change.")
            print(f"Here is your {choice} ☕ Enjoy! ")
            resources["water"] -= MENU[choice]["ingredients"]["water"]
            resources["coffee"] -= MENU[choice]["ingredients"]["coffee"]
            resources["milk"] -= MENU[choice]["ingredients"]["milk"]
            time.sleep(2)
            clear()
        else:
            if resources["water"] >= MENU[choice]["ingredients"]["water"]:
                print("Sorry, not enough water")
            elif resources["coffee"] >= MENU[choice]["ingredients"]["coffee"]:
                print("Sorry, not enough coffee")
            elif resources["milk"] >= MENU[choice]["ingredients"]["milk"]:
                print("Sorry, not enough milk")
                
                
                