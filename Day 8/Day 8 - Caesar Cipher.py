from Art import logo

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

print("------------------------------------------------------------")
print(logo)
print("------------------------------------------------------------\n")


def caesar(menssagem_inicial, quantidade_de_shift, direcao):

    menssagem_final = ""
        
    if direcao == "de":
        quantidade_de_shift *= -1
        
    for i in menssagem_inicial:
        if i in alfabeto:
            posicao = alfabeto.index(i)
            nova_posicao = posicao + quantidade_de_shift
            print(nova_posicao)
            menssagem_final += alfabeto[nova_posicao]
        else:
            menssagem_final += i
            
    print(f"A menssagem {direcao}criptada é: {menssagem_final}\n")


acabou = False

while not acabou:
    
    direcao = input("Digite 'en' para encriptar, digite 'de' para desencriptar:\n")
    texto = input("Digite a sua menssagem:\n").lower()
    shift = int(input("Digite o numero da deslocação:\n"))
    
    shift = shift % 26
    
    caesar(menssagem_inicial=texto, quantidade_de_shift=shift, direcao=direcao)
    
    encriptar_de_novo = input("Você deseja encriptar novamente? Digite sim ou nao\n")
    
    if encriptar_de_novo == "nao":
        acabou = True
    
  
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).


