from replit import clear
from Data import *

def calculo_valor(escolha_bebida, lucro):
    
    valor_bebida = MENU[escolha_bebida]['cost']
    dinheiro_inserido = 0
    
    print(f"O {escolha} custa: {valor_bebida} reais.")
    print("Por favor insira as moedas.")
    
    dinheiro_inserido = int(input("Quantas moedas de 1 Real? "))
    dinheiro_inserido += int(input("Quantas moedas de 50 Centavos? ")) * 0.5
    dinheiro_inserido += int(input("Quantas moedas de 25 Centavos? ")) * 0.25
    dinheiro_inserido += int(input("Quantas moedas de 10 Centavos? ")) * 0.1
    
    if dinheiro_inserido >= valor_bebida:
        dinheiro_inserido = round(dinheiro_inserido - valor_bebida, 2)
        print(f"O seu troco é: {dinheiro_inserido}")
        print(f"Aqui está o seu {escolha}. Aproveite!")
        lucro_real = valor_bebida + lucro
        return lucro_real
    else:
        print("Dinheiro insuficiente. O seu dinheiro vai ser estornado.")

def recursos(escolha_bebida):
    resources["milk"] = resources["milk"] - MENU[escolha_bebida]["ingredients"]["milk"]
    resources["water"] = resources["water"] - MENU[escolha_bebida]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[escolha_bebida]["ingredients"]["coffee"]

def check_recursos(escolha_bebida):
    
    if escolha_bebida == "report":
        pass
    elif escolha_bebida == "exit":
        pass
    else:
        faltando = False
        
        if resources["milk"] < MENU[escolha_bebida]["ingredients"]["milk"]:
            clear()
            print(f"Desculpa, não há leite suficiente para fazer o seu {escolha_bebida}")
            faltando = True
        elif resources["water"] < MENU[escolha_bebida]["ingredients"]["water"]:
            clear()
            print(f"Desculpa, não há água suficiente para fazer o seu {escolha_bebida}")
            faltando = True
        elif resources["coffee"] < MENU[escolha_bebida]["ingredients"]["coffee"]:
            clear()
            print(f"Desculpa, não há café suficiente para fazer o seu {escolha_bebida}")
            faltando = True
    
        return faltando 
   
def report(lucro):
    print(f"Água: {resources['water']}ml.")
    print(f"Leite: {resources['milk']}ml.")
    print(f"Café: {resources['coffee']}ml.")
    print(f"Lucro: {lucro}.")

acabou = False

lucro_real = 0.0

while not acabou:
    
    escolha = input(f"O que você gostaria? (espresso\latte\cappuccino): ").lower()
    
    acabou = check_recursos(escolha)
    
    if acabou == True:
        break        
        
    if escolha == "espresso":
        lucro_real = calculo_valor(escolha, lucro_real)
        recursos(escolha)
    elif escolha == "latte":
        lucro_real = calculo_valor(escolha, lucro_real)
        recursos(escolha)
    elif escolha == "cappuccino":
        lucro_real = calculo_valor(escolha, lucro_real)
        recursos(escolha)
    elif escolha == "report":
        report(lucro_real)
    elif escolha == "exit":
        acabou = True
    
    print("----------------------------------------------------------")
    
