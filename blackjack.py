import random
import LittleFS as lv
import hardware

# Initialize display
lv.init()
display = hardware.display()
scr = lv.obj()

def deal_card():
    return random.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11])

def calculate_score(cards):
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def update_display(player_cards, dealer_cards, message):
    scr.clean()
    label = lv.label(scr)
    label.set_text(f"Player: {player_cards} (Score: {calculate_score(player_cards)})\n"
                   f"Dealer: {dealer_cards} (Score: {calculate_score(dealer_cards)})\n"
                   f"{message}")
    label.align(lv.ALIGN.CENTER, 0, 0)
    display.load_scr(scr)

def blackjack():
    player_cards = [deal_card(), deal_card()]
    dealer_cards = [deal_card(), deal_card()]
    update_display(player_cards, dealer_cards, "Press BtnA to Hit, BtnB to Stand")
    
    while calculate_score(player_cards) < 21:
        if hardware.BtnA.was_pressed():
            player_cards.append(deal_card())
            update_display(player_cards, dealer_cards, "Press BtnA to Hit, BtnB to Stand")
        elif hardware.BtnB.was_pressed():
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
    
    update_display(player_cards, dealer_cards, message)
    hardware.sleep(5)

while True:
    blackjack()
