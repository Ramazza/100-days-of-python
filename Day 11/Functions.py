import random

def deal():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards, dealer_cards):
    
    user_score = sum(cards)
    dealer_score = sum(dealer_cards)
    
    if user_score == 21:
        user_score = 0
        return user_score, dealer_score
    elif dealer_score == 21:
        dealer_score = 0
        return user_score, dealer_score
    else:
        return user_score, dealer_score            

def compare(user_score, dealer_score):
    
    if user_score > 21 and dealer_score > 21:
        print("Empate.")
        print("Ninguem venceu!")
    elif user_score > 21:
        print("A casa venceu!")
    elif dealer_score > 21:
        print("Você venceu!")
    elif user_score == 0:
        print("Blackjack.")
        print("Você venceu!")
    elif dealer_score == 0:
        print("Blackjack.")
        print("A casa venceu!")
    elif user_score == dealer_score:
        print("Empate.")
        print("Ninguem venceu!")
    elif user_score > dealer_score and user_score < 21:
        print("Você venceu!")
    elif dealer_score > user_score and dealer_score < 21:
        print("A casa venceu!") 