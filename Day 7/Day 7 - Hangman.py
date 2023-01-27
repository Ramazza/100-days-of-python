import random
from Art import estagios
from Words import palavras

palavra_aleatoria = random.choice(palavras).lower() #Escolhe uma palavra aleatoria da lista "palavras"
display = []

for i in range(len(palavra_aleatoria)): #Cria o display da palavra escolhida, no tamanho da mesma
    display += "_"

print("---------------------------")
print("Bem vindo ao Jogo da Forca!")
print("---------------------------")
print("A palavra: ", end="")
print(*display, sep = " ")


fim_de_jogo = False
vidas = 6

while not fim_de_jogo:
    
    if vidas == 6:
        print(estagios[6])
    else:
        print(estagios[vidas])
        
    escolha = input("\nEscolha uma letra: ")
    
    for i in range(len(palavra_aleatoria)):
        if escolha == palavra_aleatoria[i]:
            display[i] = escolha
    
    print("---------------------------")
    print("A palavra: ", end="")
    print(*display, sep = " ")
           
    if escolha not in palavra_aleatoria:
        vidas -= 1
         
    if "_" not in display:
        print("\nVoce ganhou!")
        fim_de_jogo = True
    elif vidas == 0:
        print(estagios[0])
        print("\nVoce perdeu!")
        fim_de_jogo = True