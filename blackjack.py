from game.player import Player, Person
from game.dealer import Dealer

######################

game_done = player_done = dealer_done = False

__MIN_STAY_FOR_DEALER = 17
__MAX_FOR_BUST = 21
__BLACKJACK = 21

player = Player(input("Please enter your name: "))

dealer = Dealer('John')
dealer.shuffle()

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
        player_done = True

    ### While loop for dealer's turn
    while not dealer_done:
        print("dealer's turn")
        dealer_done = True

    if input("Hit or stay? ").upper() in ("HIT", "H"):
        player.get_hand(dealer.give_card())
        print(player.show_hand())

        if player.hand_total_value() > __MAX_FOR_BUST:
            print("Busted! you lose this hand!")
            game_done = True
    else:
        if dealer.hand_total_value() >= __MIN_STAY_FOR_DEALER:
            print(dealer.show_hand())
            game_done = True
        else:
            dealer.get_hand(dealer.give_card())
            continue

    game_done = True
