import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

decisao = input("O que você escolhe?\n" 
                 + "Digite 0 para Pedra. \n"
                 + "Digite 1 para Papel. \n"
                 + "Digite 2 para Tesoura. \n")

#A sua decisão
print("Você escolheu: \n")
if decisao == "0":
    print(rock)
elif decisao == "1":
    print(paper)
elif decisao == "2":
    print(scissors)

#A decisão do PC   
num_aleatorio = random.randint(0,2)

print("O computador escolheu: \n")
if num_aleatorio == 0:
    print(rock)
elif num_aleatorio == 1:
    print(paper)
elif num_aleatorio == 2:
    print(scissors)

#Os empates
if decisao == "0" and num_aleatorio == 0:
    print("Empate")
elif decisao == "1" and num_aleatorio == 1:
    print("Empate")
elif decisao == "2" and num_aleatorio == 2:
    print("Empate")
    
#Pedra vence ou perde   
if decisao == "0" and num_aleatorio == 1:
    print("Você perdeu!")
elif decisao == "0" and num_aleatorio == 2:
    print("Você venceu!")
    
#Papel vence ou perde
if decisao == "1" and num_aleatorio == 0:
    print("Você venceu!")
elif decisao == "1" and num_aleatorio == 2:
    print("Você perdeu!")
    
#Tesoura vence ou perde
if decisao == "2" and num_aleatorio == 0:
    print("Você perdeu!")
elif decisao == "2" and num_aleatorio == 1:
    print("Você venceu!")
