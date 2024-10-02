from askUser import askUser
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
work_is_on = True
while work_is_on:
    choice = askUser(menu)
    if choice == "off":
        work_is_on = False
    elif choice == "report":
        CoffeeMaker().report()
        MoneyMachine().report()
    else:
        exit()
