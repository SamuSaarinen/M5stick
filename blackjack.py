import random
from m5stack import *
from m5ui import *
from uiflow import *

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def display_hand(player_cards, dealer_cards, message):
    lcd.clear()
    lcd.print("Blackjack", 10, 10, 0xffffff)
    lcd.print(f"Player: {player_cards} (Score: {calculate_score(player_cards)})", 10, 40, 0xff0000)
    lcd.print(f"Dealer: {dealer_cards} (Score: {calculate_score(dealer_cards)})", 10, 70, 0x00ff00)
    lcd.print(message, 10, 100, 0xffff00)

def blackjack():
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    
    while calculate_score(player_cards) < 21:
        display_hand(player_cards, dealer_cards, "Press BtnA to Hit, BtnB to Stand")
        while True:
            if btnA.wasPressed():
                player_cards.append(deal_card())
                break
            if btnB.wasPressed():
                while calculate_score(dealer_cards) < 17:
                    dealer_cards.append(deal_card())
                break
    
    player_score = calculate_score(player_cards)
    dealer_score = calculate_score(dealer_cards)
    
    if player_score > 21:
        message = "You busted! Dealer wins."
    elif dealer_score > 21 or player_score > dealer_score:
        message = "You win!"
    elif player_score < dealer_score:
        message = "Dealer wins."
    else:
        message = "It's a tie!"
    
    display_hand(player_cards, dealer_cards, message)
    wait(5)
    lcd.clear()

while True:
    blackjack()
