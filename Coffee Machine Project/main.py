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
    "water": 1000,
    "milk": 500,
    "coffee": 500,
    "Money" : 0.0
}
switch='on'


def checkResources(drink):
    pop=MENU[drink]
    ing=pop['ingredients']
    not_enough=''
    for mat in ing:
        if ing[mat]>resources[mat]:
            not_enough=mat
            break
    return not_enough


def reduce_resources(drink):
    ing=MENU[drink]['ingredients']
    for mat in ing:
        resources[mat]=resources[mat]-ing[mat]

def take_money(cost):
    print(f"You total amt is: {cost}")
    print("Insert Coins ")
    quarters=int(input("How many quarters?: "))
    dimes=int(input("How many dimes? : "))
    nickels=int(input("How many nickels? :"))
    pennies=int(input("How many pennies? :"))
    total=0.25*quarters+0.10*dimes+0.05*nickels+0.01*pennies
    return total


while switch!='off':

    drink = input("What would you like? (espresso/latte/cappuccino): ").lower().lstrip()
    if drink=='off':
        switch='off'
        continue
    if drink=='report':
        for key in resources:
            print(f"{key} : {resources[key]} ")
        continue
    cost=MENU[drink]['cost']
    resources_present = checkResources(drink)
    if resources_present!='':
        print(f"Sorry there is not enough {resources_present}")
        continue
    total = take_money(cost)
    if cost>total:
        print("Sorry. Not enough money. Money Refunded")
    if total>cost:
        print(f"Here's ${(total-cost):.2f} dollars in change")
        profit=resources['Money']
        resources['Money']=cost+profit
    reduce_resources(drink)
    print(f"Here's your {drink}. Enjoy!")





