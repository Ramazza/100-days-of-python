from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

esta_ligada = True

while esta_ligada:
    
    opcoes = menu.get_items()
    escolha = input(f"Qual bebida você gostaria? ({opcoes}): ")
    
    if escolha == "exit":
        esta_ligada = False
    elif escolha == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        bebida = menu.find_drink(escolha)
        if coffee_maker.is_resource_sufficient(escolha) and money_machine.make_payment(escolha.cost):
            coffee_maker.make_coffee(escolha)