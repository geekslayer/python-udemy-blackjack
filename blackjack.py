# from game.deck import Deck, Card
from game.player import Player
from game.dealer import Dealer

######################
# new_deck = Deck()

new_player = Player('Etienne')

new_dealer = Dealer('John')

new_dealer.shuffle()

######################
print(new_player)
print(new_dealer)
print(new_dealer.deck)

new_player.get_hand(new_dealer.give_card())
new_player.get_hand(new_dealer.give_card())

new_player.show_hand()
