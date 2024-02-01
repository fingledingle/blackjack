import random 
import os



cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card(card_list):
    random_card = random.choice(cards)
    card_list.append(random_card)
    return random_card

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def calculate_score(list_of_cards):
    summary_of_cards = sum(list_of_cards)

    if 11 in list_of_cards and 10 in list_of_cards:
        return 0
    elif 11 in list_of_cards:
        if summary_of_cards > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)
    return summary_of_cards

def compare(user_score, computer_score):
    if computer_score == user_score:
        print(f"User = {user_score} vs computer = {computer_score} \n Draw")
    elif computer_score == 0:
        print(f"User = {user_score} vs computer = {computer_score} \n User Loses")
    elif user_score == 0:
        print(f"User = {user_score} vs computer = {computer_score} \n User Wins")     
    elif user_score > 21:
        print(f"User = {user_score} vs computer = {computer_score} \n User Loses")     
    elif computer_score > 21:
        print(f"User = {user_score} vs computer = {computer_score} \n User Wins")     
    else:
        if computer_score > user_score:
            print(f"User = {user_score} vs computer = {computer_score} \n User loses")
        else:
            print(f"User = {user_score} vs computer = {computer_score}\n User Wins")

from art import logo
print(logo)

user_cards = []
computer_cards = []

for _ in range(2):
    deal_card(user_cards)
    deal_card(computer_cards)

user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"This is your current score {user_score}")
print(f"This is the computer's current score {computer_score}")

if computer_score == 0:
    print("Computer has gotten a Black Jack \n Game Over")
elif user_score == 0:
    print("User has gotten a Black Jack \n Game Over")
elif user_score > 21:
    compare(user_score, computer_score)
else:
    draw_another_card = input("Do you wanna draw another card? Y or N \n").lower()
    while draw_another_card == "y":
        deal_card(user_cards)
        calculate_score(user_cards)
        user_score = calculate_score(user_cards)
        print(f"You drew a card. Your current score: {user_score}")
        if computer_score > 17:
            deal_card(computer_cards)
            calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
        if user_score > 21:
            print(f"User = {user_score} vs computer = {computer_score}\n User Loses")
            break
        draw_another_card = input("Do you wanna draw another card? Y or N \n").lower()
    else:
        compare(user_score, computer_score)

restart_choice = input("Do you want to restart? Y or N \n").lower()
if restart_choice == "y":
    clear()
