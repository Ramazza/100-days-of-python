import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao PyPassword Generator!")
num_letras= int(input("Quantas letras gostaria na sua senha?\n")) 
num_simbolos = int(input(f"Quantos simbolos gostaria?\n"))
num_numeros = int(input(f"Quantos números gostaria?\n"))

tamanho_senha = int(num_letras + num_numeros + num_simbolos)

letras_new = []
simbolos_new = []
numeros_new = []

for i in range(num_letras):
    letra_aleatoria = random.randint(0, 25)
    letras_new += [letras[letra_aleatoria]]
    
for i in range(num_simbolos):
    simbolo_aleatorio = random.randint(0, 8)
    simbolos_new += [simbolos[simbolo_aleatorio]]

for i in range(num_numeros):
    numero_aleatorio = random.randint(0, 9)
    numeros_new += [numeros[numero_aleatorio]]
    
senha = letras_new + numeros_new + simbolos_new
random.shuffle(senha)

print(f"A sua nova senha é: ")
print(*senha, sep = "")



    


