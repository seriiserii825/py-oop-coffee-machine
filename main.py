from askUser import askUser
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
work_is_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

while work_is_on:
    choice = askUser(menu)
    if choice == "off":
        work_is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                print(f"Please, pay {drink.cost}.")
                make_payment = money_machine.make_payment(drink.cost)
                if make_payment:
                    coffee_maker.make_coffee(drink)
            else:
                print("Sorry, there is not enough resources.")
        else:
            print("Sorry, there is no such drink in the menu.")
