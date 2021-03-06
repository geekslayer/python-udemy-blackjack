"""
    This is the main program for blackjack.
"""

import time
from game.person import Player, Dealer
import game.common

######################

HAND_BET = 35
GAME_DONE = PLAYER_DONE = DEALER_DONE = False

PLAYER = Player(input("Please enter your name: "))

DEALER = Dealer('John')
DEALER.shuffle()

######################

def show_game_winner(current_player, current_dealer, bet_amount):
    """
        This will print who's the winner and with what score
        and also will pay the player if needs be
    """
    player_wins = False

    if(not current_player.is_busted() and not current_dealer.is_busted() and \
       current_player.hand_total_value() == current_dealer.hand_total_value()):
        print("It's a tie!!!")

    if current_player.is_busted():
        print("Dealer wins!")

    if current_dealer.is_busted():
        print(f"{current_player.name} wins!")
        player_wins = True

    if(current_player.hand_total_value() > current_dealer.hand_total_value() and \
       current_player.hand_total_value() <= game.common.__MAX_FOR_BUST):
        print(f"{current_player.name}({current_player.bankroll}) is the winner with a score of: " \
              f"{current_player.hand_total_value()}")
        player_wins = True

    if(current_dealer.hand_total_value() > current_player.hand_total_value() and \
       current_dealer.hand_total_value() <= game.common.__MAX_FOR_BUST):
        print(f"{current_dealer.name} is the winner with a score of: " \
              f"{current_dealer.hand_total_value()}")

    if player_wins:
        current_player.cash_in(bet_amount)

def start_hand(player, dealer, bet_amount):
    """
        This is how the start of hand between player and dealer
    """

    player.place_bet(bet_amount)
    player.get_hand(dealer.give_card())
    player.get_hand(dealer.give_card())

    print(player.show_hand())

    dealer.get_hand(dealer.give_card())
    dealer.get_hand(dealer.give_card())

    print(dealer.show_first_hand())

    if player.hand_total_value() == 21:
        player.has_blackjack = True

    if dealer.hand_total_value() == 21:
        dealer.has_blackjack = True

    if player.has_blackjack:
        print("Blackjack!!!")

######################

print(PLAYER)
print(DEALER)

print("Let's play blackjack!!!!")
GAME_DONE = not DEALER.has_enough_cards()
while not GAME_DONE:
    try:
        HAND_BET = int(input("Please make your bet! "))
        start_hand(PLAYER, DEALER, HAND_BET)
    except game.common.NotEnoughCards as error:
        print(str(error))
        GAME_DONE = True
        continue
    except game.common.NotEnoughChips as error:
        print(str(error))
        GAME_DONE = True
        continue
    except TypeError as type_error:
        print(str(type_error))
        continue
    except Exception as gen_error:
        print(str(gen_error))
        continue

    ### While loop for player's turn
    while not PLAYER_DONE:
        print("player's turn")

        if input("Hit or stay? ").upper() in ("HIT", "H"):
            try:
                PLAYER.get_hand(DEALER.give_card())
            except game.common.NotEnoughCards as error:
                print(str(error))
                GAME_DONE = True
                PLAYER_DONE = True
                continue

            print(PLAYER.show_hand())

            if PLAYER.hand_total_value() > game.common.__MAX_FOR_BUST:
                print("Busted! you lose this hand!")
                PLAYER_DONE = True
        else:
            PLAYER_DONE = True

    ### While loop for dealer's turn
    print("dealer's turn")

    if not PLAYER.is_busted():
        print(DEALER.show_hand(), end=" ")
    else:
        print(DEALER.show_hand())

    if DEALER.has_blackjack:
        print("Dealer's got blackjack", flush=True)

        if not PLAYER.has_blackjack:
            print("Dealer wins")

    while not DEALER_DONE and not PLAYER.is_busted():
        if DEALER.hand_total_value() < game.common.__MIN_STAY_FOR_DEALER:
            try:
                DEALER.get_hand(DEALER.give_card())
            except game.common.NotEnoughCards as error:
                print(str(error))
                GAME_DONE = True
                DEALER_DONE = True
                continue

            print(f"| {DEALER.hand[-1]} ", end="", flush=True)

            if DEALER.hand_total_value() > game.common.__MAX_FOR_BUST:
                print()
                print("Busted! you lose this hand!")
                DEALER_DONE = True
            else:
                time.sleep(2)
        else:
            print()
            DEALER_DONE = True

    print(f"{PLAYER.name} has {str(PLAYER.hand_total_value())} and " \
          f"{DEALER.name} has {str(DEALER.hand_total_value())}")

    show_game_winner(PLAYER, DEALER, HAND_BET)

    PLAYER.throw_hand_away()
    DEALER.throw_hand_away()

    if input("Do you want to continue? Type 'y' for yes or 'n' for no. ").lower()[0] != 'y':
        GAME_DONE = True
    else:
        PLAYER_DONE = False
        DEALER_DONE = False
