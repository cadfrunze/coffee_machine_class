from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

game = True
coffe_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while game:
    choice = input(f"Alege cafeaua: {menu.get_items()}")
    if choice == "report":
        coffe_maker.report()
        money_machine.report()
    elif choice == "off":
        game = False
    elif choice == "latte" or choice == "espresso" or choice == "cappuccino":
        drink = menu.find_drink(choice)
        resources = coffe_maker.is_resource_sufficient(drink)
        # print(drink.cost)
        # help(drink)
        if resources:
            plata = money_machine.make_payment(drink.cost)
            # print(resources)
            # print(plata)
            if plata:
                cafeaua = coffe_maker.make_coffee(drink)
                money_machine.money_received = 0
                # print(money_machine.money_received)




