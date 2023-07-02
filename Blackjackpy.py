# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 13:42:34 2022

@author: Sajjad
"""
import random , sys

logo="""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def score(given_cards):
    total_score = sum(given_cards)
    if total_score == 21 and len(given_cards) == 2:
        return 0
    
    if total_score > 21 and 11 in given_cards:
        given_cards[given_cards.index(11)] = 1
    return sum(given_cards)
                                                
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

if input("Do you want to play a game of Blackjack?Type 'y' or 'n': ") == 'y':
    decision_play= True
else: 
    decision_play= False
    sys.exit()
    
while decision_play:
    print(chr(27) + "[H" + chr(27) + "[J")
    print(logo)
    your_cards = [random.choice(cards),random.choice(cards)]
    print(f"Your cards: {your_cards}, current score: {score(your_cards)}")
    computer_cards = [random.choice(cards)]
    print(f"Computer's first card: {computer_cards[0]}")
    while score(your_cards) <= 21:
        if score(your_cards) == 0:
            print("You are blackjack!")
            break
        get_or_pass = input("Type 'y' to get another card, type 'n' to pass: ")
        if get_or_pass == 'y':
           your_cards.append(random.choice(cards))
           print(f"Your cards: {your_cards}, current score: {score(your_cards)}")
           print(f"Computer's first card: {computer_cards[0]}")
        else:
            break
    computer_cards.append(random.choice(cards))

    while score(computer_cards) <= 17:
        if score(computer_cards) == 0:
           print("Computer is blackjack!")
           break
        computer_cards.append(random.choice(cards))
    break

your_final_score = score(your_cards)
computer_final_score = score(computer_cards)

print(f"Your final hand: {your_cards}, final score: {your_final_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_final_score}")  
if your_final_score == 0 and computer_final_score == 0:
    print("Draw!")
elif your_final_score == 0 and computer_final_score != 0:
    print("You are blackjack.You won.")
elif your_final_score != 0 and computer_final_score == 0:
    print("Computer is blackjack.You lost.")
elif your_final_score > 21:
   print("You went over, You lose.")     
elif computer_final_score <= 21 and computer_final_score > your_final_score:
   print("Computer won.")
elif computer_final_score <= 21 and computer_final_score < your_final_score:
   print("You won.")
elif computer_final_score <= 21 and computer_final_score == your_final_score:
   print("Draw!")
elif computer_final_score > 21:
   print("Computer Bust, You won!")
        
    
    
