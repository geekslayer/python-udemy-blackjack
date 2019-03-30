from game.player import Player, Person
from game.dealer import Dealer

import game.common
######################

game_done = player_done = dealer_done = False

player = Player(input("Please enter your name: "))

dealer = Dealer('John')
dealer.shuffle()

######################

def show_game_winner(player, dealer):
    if(player.hand_total_value() <= game.common.__MAX_FOR_BUST and player.hand_total_value() > dealer.hand_total_value() and not dealer.is_busted()):
        print(f"{player.name} is the winner with a score of: {player.hand_total_value()}")
    elif(dealer.hand_total_value() <= game.common.__MAX_FOR_BUST and dealer.hand_total_value() > player.hand_total_value() and not player.is_busted()):
        print(f"{dealer.name} is the winner with a score of: {dealer.hand_total_value()}")

######################

print(player)
print(dealer)

print("Let's play blackjack!!!!")

player.get_hand(dealer.give_card())
player.get_hand(dealer.give_card())

print(player.show_hand())

dealer.get_hand(dealer.give_card())
dealer.get_hand(dealer.give_card())

print(dealer.show_first_hand())

print(player.hand_total_value())

if player.hand_total_value() == 21:
    print("Blackjack!!!!!")

while not game_done:

    ### While loop for player's turn
    while not player_done:
        print("player's turn")

        if input("Hit or stay? ").upper() in ("HIT", "H"):
            player.get_hand(dealer.give_card())
            print(player.show_hand())

            if player.hand_total_value() > game.common.__MAX_FOR_BUST:
                print("Busted! you lose this hand!")
                player_done = True
        else:
            player_done = True

    ### While loop for dealer's turn
    while not dealer_done:
        print("dealer's turn")
        print(dealer.show_hand())

        if input("Hit or stay? ").upper() in ("HIT", "H"):
            dealer.get_hand(dealer.give_card())
            print(dealer.show_hand())

            if dealer.hand_total_value() > game.common.__MAX_FOR_BUST:
                print("Busted! you lose this hand!")
                dealer_done = True
        else:
            dealer_done = True

    # if input("Hit or stay? ").upper() in ("HIT", "H"):
    #     player.get_hand(dealer.give_card())
    #     print(player.show_hand())

    #     if player.hand_total_value() > __MAX_FOR_BUST:
    #         print("Busted! you lose this hand!")
    #         game_done = True
    # else:
    #     if dealer.hand_total_value() >= __MIN_STAY_FOR_DEALER:
    #         print(dealer.show_hand())
    #         game_done = True
    #     else:
    #         dealer.get_hand(dealer.give_card())
    #         continue

    print(player.name + " has " + str(player.hand_total_value()))
    print(dealer.name + " has " + str(dealer.hand_total_value()))

    show_game_winner(player, dealer)

    game_done = True
