from Art import logo
from replit import clear

print(logo)

def soma(numero_1, numero_2):
    return numero_1 + numero_2

def subtracao(numero_1, numero_2):
    return numero_1 - numero_2

def multiplicacao(numero_1, numero_2):
    return numero_1 * numero_2

def divisao(numero_1, numero_2):
    if numero_2 == 0:
        print("Impossivel dividir por 0.")
    else:
        return numero_1 / numero_2
    
operacoes = {
    "+": soma,
    "-": subtracao,
    "*": multiplicacao,
    "/": divisao,    
}

fim = False

while not fim:
    print("----------------------------")
    numero_1 = int(input("Qual é o primeioro numero? "))
    numero_2 = int(input("Qual é o segundo numero? "))
    print("----------------------------")

    for key in operacoes:
        print(key)
      
    print("----------------------------")  
    simbolo_da_operacao = input("Escolha a operação das linhas a cima: ")
    funcao = operacoes[simbolo_da_operacao]
    resultado = funcao(numero_1, numero_2)

    print(f"{numero_1} {simbolo_da_operacao} {numero_2} = {resultado}")
    print("----------------------------")
    
    continuar = input(f"Digite 's' se deseja continuar calculando, ou 'n' se deseja sair: ")
    
    if continuar == "n":
        fim = True
        clear()
    else:
        clear()

