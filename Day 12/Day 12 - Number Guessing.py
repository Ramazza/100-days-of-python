import random
from Art import logo
from replit import clear

DIFICIL = 5
FACIL = 10

def check_resposta(guess, resposta, chances):
    if guess > resposta:
            print("Muito alto")
            return chances - 1
    elif guess < resposta:
            print("Muito baixo")
            return chances - 1
    else:
        print(f"Você acertou! A resposta era: {resposta}")
        
print("---------------------------------------------------------------------------------------")
print(logo)
print("---------------------------------------------------------------------------------------")
print("Bem vindo ao Adivinha Numeros!")
print("Estou pensando em um numero entre 0 e 100.")

numero_aleatorio = random.randint(0,100)

dificuldade = input("Escolha uma dificuldade. Digite 'facil' ou 'dificil': ")
print("------------------------------------------------------")

if dificuldade == "facil":
    chances = FACIL
else:
    chances = DIFICIL
    
print(f"Você tem {chances} chances para acertar o numero.")
numero_guess = int(input("Tente adivinhar o numero: "))
print("--------------------------------------------------")

if numero_aleatorio == numero_guess:
    print(f"Você acertou! A resposta era: {numero_aleatorio}")

while numero_guess != numero_aleatorio:
    
    chances = check_resposta(numero_guess, numero_aleatorio, chances)
    
    if chances == 0:
        print("A suas chances acabaram, Você perdeu!")
        print(f"A resposta era : {numero_aleatorio}.")
        break
    else:
        print(f"Você tem {chances} chances para acertar o numero.")
        numero_guess =  int(input("Tente novamente: "))
        print("--------------------------------------------------")
        
    if numero_aleatorio == numero_guess:
        print(f"Você acertou! A resposta era: {numero_aleatorio}")
    
    
    
    
    
    
