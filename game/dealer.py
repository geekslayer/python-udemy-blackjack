from random import randint
from game.deck import Deck, Card

class Dealer():

    def __init__(self, name):
        self.name = name
        self.deck = Deck()

    def shuffle(self):
        self.deck.shuffle()

    def give_card(self):
        return self.deck.full_deck.pop(0)

    def pay_player(self, amount):
        pass

    def collect_from_player(self):
        pass

    def hand(self):
        pass

    def __str__(self):
        return f"Hi! I'm {self.name}, I will be your dealer for the evening."
