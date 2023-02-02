import random
from replit import clear
from Art import *
from Game_data import * 

def printagem(data, aux):
    
    """Seleciona e printa o famoso A e o famoso B"""    
    if aux == 0:
        a = random.choice(data)
        
        print(f"Compare A: ", end="")
        print(a["name"], end="")
        print(f", a ", end="")
        print(a["description"], end="")
        print(f", from ", end="")
        print(a["country"], end="")
        print(".")
            
        b = random.choice(data)
            
        if a == b:
            a = random.choice(data)
        else:
            print(vs)
            print(f"Compare B: ", end="")
            print(b["name"], end="")
            print(f", a ", end="")
            print(b["description"], end="")
            print(f", from ", end="")
            print(b["country"], end="")
            print(".")
            print("---------------------------------------")
            return a, b
    else:
        b = random.choice(data)
        print(vs)
        print(f"Compare B: ", end="")
        print(b["name"], end="")
        print(f", a ", end="")
        print(b["description"], end="")
        print(f", from ", end="")
        print(b["country"], end="")
        print(".")
        print("---------------------------------------")
        return  b  

def compara(a, b, escolha, score):
    
    """Compara qual famoso tem mais seguidores e checa se o usuario fez a escolha certa"""
    
    if escolha == 'A' and a["follower_count"] > b["follower_count"]:
        score += 1
        fim = False
        return score, fim, a
    elif escolha == 'B' and a["follower_count"] < b["follower_count"]:
        score += 1
        fim = False
        return score, fim, b
    elif escolha == 'A' and a["follower_count"] < b["follower_count"]:
        clear()
        print(a["name"], end="")
        print(f" tem menos seguidores.")
        print("Você perdeu.")
        print(f"A sua pontuação foi: {score}")
        fim = True
        return score, fim
    else:
        clear()
        print(b["name"], end="")
        print(f" tem menos seguidores.")
        print("Você perdeu.")
        print(f"A sua pontuação foi: {score}")
        fim = True
        return score, fim

def game():
     
    fim = False
    score = 0
    aux = 0
        
    while not fim:
        
        if score == 0:
            print("---------------------------------------")
            print(logo)
            print("---------------------------------------")
        
            printado = printagem(data, aux)
            a = printado[0]
            b = printado[1]
                    
            escolha = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").upper()
        
            comparado = compara(a=a, b=b, escolha=escolha, score=score)
            score = comparado[0]
            fim = comparado[1]
        else:
            
            aux = 1
            
            print("---------------------------------------")
            print(logo)
            print("---------------------------------------")
            print(f"A sua ponuação é: {score}")
            
            a = comparado[2]
            
            print(f"Compare A: ", end="")
            print(a["name"], end="")
            print(f", a ", end="")
            print(a["description"], end="")
            print(f", from ", end="")
            print(a["country"], end="")
            print(".")
            print(a["follower_count"])
            
            printado = printagem(data, aux)
            b = printado
            
            escolha = input("Quem tem mais seguidores? Digite 'A' ou 'B': ").upper()
        
            comparado = compara(a=a, b=b, escolha=escolha, score=score)
            score = comparado[0]
            fim = comparado[1]
    
    dnv = input("Deseja jogar novamente? Digite 's' ou 'n': ")
    
    if dnv == 'n':
        clear()
        print("Até a proxima...")
    else:
        game()
                 
game()