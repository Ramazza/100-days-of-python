print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem vindo a Ilha do Tesouro.")
print("O seu objetivo é encontrar o tesouro.")

esquerda_direita = input("Você está em um encruzilhada, para onde deseja ir? Para a direita ou para a esquerda? \n")
if esquerda_direita.upper() == "DIREITA":
    print("Você caiu em um buraco.\n" + "Game Over.")
else: 
    lago = input("Você chegou em um lago. Há um ilha no meio do lago, você deseja esperar por um barco ou nadar até ela? \n")
    if lago.upper() == "NADAR":
        print("Um tubarao te devorou.\n" + "Game Over")
    else:
        porta = input("Você chegou ileso na ilha. Na ilha há uma casa e dentro dela há 2 portas. Uma vermelha, umas amarela e uma azul Deseja entrar em qual porta? \n")
        if porta.upper() == "VERMELHO":
            print("Você foi queimado por fogo.\n" + "Game Over.")
        elif porta.upper() == "BLUE":
            print("Você foi comido por um leão.\n" + "Game Over.")
        else:
            print("Você achou o tesouro!!!!")


