from game.player import Player, Person
from game.dealer import Dealer

######################

done = False

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

while not done:
    if input("Hit or stay? ").upper() in ("HIT","H") :
        player.get_hand(dealer.give_card())
        print(player.show_hand())

        if player.hand_total_value() > 21:
            print("Busted! you lose this hand!")
            done = True
    else:
        if dealer.hand_total_value() >= 17:
            print(dealer.show_hand())
            done = True
        else:
            dealer.get_hand(dealer.give_card())
            continue

    done = True
