import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)
    return random_card


#start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()



def calculate_score(cards):
    """ Take a list of cards and return the score calculated from the cards"""
    if len(cards) == 2 and sum(cards) == 21:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw"
    elif c_score == 0:
        return "Computer wins with a blackjack!"
    elif u_score == 0:
        return "User wins with a blackjack!"
    elif u_score > 21:
        return "You busted. Computer wins!"
    elif c_score > 21:
        return "Computer busted. User wins!"
    elif u_score > c_score:
        return "User wins!"
    else:
        return "Computer wins!"

def play_game():

    computer_cards = []
    user_cards = []
    computer_score = -1
    user_score = -1
    is_game_over = False
    print(art.logo)

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        computer_score = calculate_score(computer_cards)
        user_score = calculate_score(user_cards)
        print(f"Your cards: {user_cards}, current score {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card or 'n' to pass").lower()
            if user_should_deal == "y":
                user_cards.append(deal_card())
            elif user_should_deal == "n":

                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Your final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n'").lower() == "y":
    print("\n"*20)
    play_game()
#
#
# def black_jack():
#     # sum of player and dealer hands
#     dealer_hand_total = 0
#     player_hand_total = 0
#     for i in range(0, len(dealer_hand)):
#         dealer_hand_total = dealer_hand_total + dealer_hand[i]
#     for i in range(0, len(player_hand)):
#         player_hand_total = player_hand_total + player_hand[i]
#     print(dealer_hand_total)
#     print(player_hand_total)
#     # does the player or computer have blackjack?
#     if 11 in dealer_hand and dealer_hand_total == 21:
#         print("Computer wins!")
#     elif 11 in player_hand and player_hand_total == 21:
#         print("Player wins!")
#     else:
#         # is user score over 21?
#         if player_hand_total > 21:
#             if 11 in player_hand:
#                 element = 11
#                 player_hand[player_hand.index(element)] = 1
#                 player_hand_total = sum_of_player_hand(player_hand)
#                 if player_hand_total > 21:
#                     print("Computer wins!")
#                 else:
#                     # ask the user if they want to get another card
#                     another_card = input("Do you want to get another card? Press 'y' for yes or 'n' for no").lower()
#                     #if another_card == "y":
#             else:
#                 print("Computer wins!")
#         # is user score under 21?
#         #elif player_hand_total < 21: