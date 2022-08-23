from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine



menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


game = True
while game:
    options = menu.get_items()
    order_name = input(f"cu ce te servesc? {options}").lower()
    if order_name == "off":
        game = False
    elif order_name == "report":
        coffee_maker.report()
        money_machine.report()
    elif order_name == "latte" or order_name == "espresso" or order_name == "cappuccino":
        drink = menu.find_drink(order_name)
        if coffee_maker.is_resource_sufficient(drink):
            print(coffee_maker.make_coffee(drink.cost))






