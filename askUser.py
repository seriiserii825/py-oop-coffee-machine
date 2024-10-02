def askUser(menu):
    menu_items = menu.get_items()
    print(f"What would you like? ({menu_items}), for develop(off, report):")
    return input()

