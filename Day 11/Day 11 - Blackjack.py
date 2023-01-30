import random
from Art import logo
from replit import clear
from Functions import deal, calculate_score, compare

def jogar():
    print("---------------------------------------------------------------")
    print(logo)
    print("---------------------------------------------------------------")

    user_cards = []
    dealer_cards = []

    for i in range(2):
        user_cards.append(deal())
        dealer_cards.append(deal())

    print(f"A suas cartas são: {user_cards[0]} e {user_cards[1]}")

    fim = False

    while not fim:
    
        score = calculate_score(user_cards, dealer_cards)
        user_score = score[0]
        dealer_score = score[1]
        
        ir_de_novo = input("Você deseja tirar outra carta? 's' para sim e 'n' para não. ")
        if ir_de_novo == 's':
            user_cards.append(deal())
            dealer_cards.append(deal())
            score = calculate_score(user_cards, dealer_cards)
            user_score = score[0]
            dealer_score = score[1]
            print(f"A suas cartas são: {user_cards}")    
        if ir_de_novo == 'n':
            clear()
            while dealer_score < 17:
                dealer_cards.append(deal())
                score = calculate_score(user_cards, dealer_cards)
                dealer_score = score[1]
            fim = True  


    compare(user_score, dealer_score)  

    print(f"As suas cartas foram: ", end="")  
    print(*user_cards, sep=" ", end="")
    print(", com um total de: ", end="")
    print(f"{user_score}.")

    print(f"As cartas da casa foram: ", end="")  
    print(*dealer_cards, sep=" ", end="")
    print(", com um total de: ", end="")
    print(f"{dealer_score}.")

    print("---------------------------------------------------------------")
    again = False
    jogar_de_novo = input("Você deseja jogar novamente? Digite 's' para sim e 'n' para não ")
    if jogar_de_novo == "s":
        clear()
        jogar()
    elif jogar_de_novo == "n":
        clear()
        print("Adeus mundo cruel.")

jogar()


#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both 
# have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), 
# then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. 
# If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of 
# blackjack and show the logo from art.py.