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
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    
}

money = 0

def take_user_order():
    order = input("What would you like? (espresso/latte/cappuccino) : ")
    if order == 'espresso':
        return resources_sufficient()
    elif order == 'latte':
        return resources_sufficient()
    elif order == 'cappuccino':
        return resources_sufficient()
    elif order == 'off':
        print('Turning the machine off')
        return
    elif order == 'report':
        print("The machines resources are as follows:/n")
        for key, value in resources.items():
            print("Item:", key, "--", value)        
    else:
        print('Incorrect output, please try again')
        take_user_order()
        
        
def resources_sufficient(resources,order):
    if order == 'latte':
        water_threshold = 200
        coffe_threshold = 24
        milk_threshold = 150
        if resources['Water'] < water_threshold:
            print('Sorry not enough water in the machine')
            if resources['Coffee'] < coffe_threshold:
                print('Sorry not enough coffee in the machine')
                if resources['Milk'] < milk_threshold:
                    print('Sorry not enough milk in the machine')
                else:
                    resources['Water'] -= water_threshold
                    resources['Coffee'] -= coffe_threshold
                    resources['Milk'] -= milk_threshold
                    cash_in(order)
    elif order == 'espresso':
        water_threshold = 50
        coffe_threshold = 18
        if resources['Water'] < water_threshold:
            print('Sorry not enough water in the machine')
            if resources['Coffee'] < coffe_threshold:
                print('Sorry not enough coffee in the machine')
            else:
                resources['Water'] -= water_threshold
                resources['Coffee'] -= coffe_threshold
                resources['Milk'] -= milk_threshold
                cash_in(order)
    else:
        water_threshold = 250
        coffe_threshold = 24
        milk_threshold = 100
        if resources['Water'] < water_threshold:
            print('Sorry not enough water in the machine')
            if resources['Coffee'] < coffe_threshold:
                print('Sorry not enough coffee in the machine')
                if resources['Milk'] < milk_threshold:
                    print('Sorry not enough milk in the machine')
                else:
                    resources['Water'] -= water_threshold
                    resources['Coffee'] -= coffe_threshold
                    resources['Milk'] -= milk_threshold
                    cash_in(order)
          
def cash_in(order):
    global money
    if order == 'latte':
        print('Your order costs dollars')
        quaters = int(input('How many quaters: '))
        quaters = quaters * 0.25
        dimes = int(input('How many dimes: '))
        dimes = dimes * 0.1
        nickles = int(input('How many nickles: '))
        nickles = nickles * 0.05
        pennies = int(input('How many pennies: '))
        pennies = pennies * 0.01
        total = quaters+dimes+nickles+pennies
        if total == 2.5:
            print("Making your latte!")
            money += total
        elif total > 2.5:
            print("Making your latte!")
            change = 2.5 - total
            print(f'Your change is {change}')
        else:
            print("Sorry that's not enough money. Money refunded")
    elif order == 'espresso':
        print('Your order costs dollars')
        quaters = int(input('How many quaters: '))
        quaters = quaters * 0.25
        dimes = int(input('How many dimes: '))
        dimes = dimes * 0.1
        nickles = int(input('How many nickles: '))
        nickles = nickles * 0.05
        pennies = int(input('How many pennies: '))
        pennies = pennies * 0.01
        total = quaters+dimes+nickles+pennies
        if total == 1.5:
            print("Making your espresso!")
            money += total
        elif total > 1.5:
            print("Making your espresso!")
            change = 1.5 - total
            print(f'Your change is {change}')
        else:
            print("Sorry that's not enough money. Money refunded")
    else:
        print('Your order costs dollars')
        quaters = int(input('How many quaters: '))
        quaters = quaters * 0.25
        dimes = int(input('How many dimes: '))
        dimes = dimes * 0.1
        nickles = int(input('How many nickles: '))
        nickles = nickles * 0.05
        pennies = int(input('How many pennies: '))
        pennies = pennies * 0.01
        total = quaters+dimes+nickles+pennies
        if total == 3.0:
            print("Making your cappuccino!")
            money += total
        elif total > 23.0:
            print("Making your cappuccino!")
            change = 3.0 - total
            print(f'Your change is {change}')
        else:
            print("Sorry that's not enough money. Money refunded")


