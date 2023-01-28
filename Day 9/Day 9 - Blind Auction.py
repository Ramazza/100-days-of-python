from Art import logo
from replit import clear

print(logo)
print("Bem vindo ao leilão secreto")

participantes = {}

def vencedor(input_participantes):
    maior_aposta = 0
    vencedor = ""
    for keys in input_participantes:
        if input_participantes[keys] > maior_aposta:
            maior_aposta = input_participantes[keys]
            vencedor = keys
    print(participantes)      
    print(f"O vencedor do leilão o/a foi {vencedor}")
            

acabou = False
   
while not acabou:
    nome = input("Qual é o seu nome? ")
    valor = int(input("Qual é a sua oferta? R$"))
    outros_participantes = input("Há outros participantes no leilão? Digite 'sim' ou 'nao'\n")
    participantes[nome] = valor
    
    if outros_participantes == "nao":
        acabou = True
        clear()
        vencedor(input_participantes=participantes)
    else:
        clear()
        
    
