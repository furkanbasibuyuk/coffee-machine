logo ="""
   ___       __  __                               _     _             
  / __\___  / _|/ _| ___  ___    /\/\   __ _  ___| |__ (_)_ __   ___  
 / /  / _ \| |_| |_ / _ \/ _ \  /    \ / _` |/ __| '_ \| | '_ \ / _ \ 
/ /__| (_) |  _|  _|  __/  __/ / /\/\ \ (_| | (__| | | | | | | |  __/ 
\____/\___/|_| |_|  \___|\___| \/    \/\__,_|\___|_| |_|_|_| |_|\___| 

        /~~~~~~~~~~~~~~~~~~~/|
       /              /######/ / |
      /              /______/ /  |
     ========================= /||
     |_______________________|/ ||
      |  \****/     \__,,__/    ||
      |===\**/       __,,__     ||    
      |______________\====/%____||
      |   ___        /~~~~\ %  / |
     _|  |===|===   /      \%_/  |
    | |  |###|     |########| | /
    |____\###/______\######/__|/
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                      
"""
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

def first_request():
    print("If do you want to turn off the coffee machine, just please write -off-\nDo you want to see resources, just please write -report-")
    choice = input("What would you like to drink ? (espresso/latte/cappucino)\n")
    return choice

def need(choice):
    need_water = MENU[choice]['ingredients']['water']
    need_milk = MENU[choice]['ingredients'].get('milk', 0)  # if there is no milk, its gonna be 0
    need_coffee = MENU[choice]['ingredients']['coffee']
    return need_water, need_milk, need_coffee

while True:
    print(logo)
    money = 0
    choice = first_request()
    if choice == "espresso" or choice == "latte" or choice == "cappucino":
        need_water, need_milk, need_coffee = need(choice)

    if choice == "off":
        break
    
    if choice == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money}")
    elif choice == "espresso" or choice == "latte" or choice == "cappucino":
        cost_of_the_coffee = MENU[choice]['cost']
        quarters = float(input("how many quaters?"))
        dimes = float(input("How many dimes?"))
        nickles = float(input("How many nickles?"))
        pennies = float(input("How many pennies?"))
        money = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
        left_money = money - cost_of_the_coffee
        if need_water <= resources['water'] and need_milk <= resources['milk'] and need_coffee <= resources['coffee'] and left_money >= 0:
            resources['water'] -= need_water
            resources['milk'] -= need_milk
            resources['coffee'] -= need_coffee
            print("Here is your coffee :D")
            if left_money > 0:
                print(f"by the way dont forget take the your money : ${left_money}")
                left_money = 0
        else:
            if need_coffee > resources['water']:
                print("Sorry there is not enough water")
            if need_milk > resources['milk']:
                print("Sorry there is not enough milk")
            if need_coffee > resources['coffee']:
                print("Sorry there is not enough coffee")
            if left_money < 0:
                print("Sorry that is not enough money. Money refunded.")
                print(f"by the way dont forget take the your money : ${money}")