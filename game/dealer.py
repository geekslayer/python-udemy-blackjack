from random import randint
from game.deck import Deck, Card
from game.person import Person

class Dealer(Person):

    def __init__(self, name):
        Person.__init__(self)
        self.name = name
        self.deck = Deck()

    def show_hand(self):
        generic_msg = Person.show_hand(self)
        return f"{self.name} (Dealer) : \t" + generic_msg

    def show_first_hand(self):
        generic_msg = str(self.hand[0]) + " | "
        return f"{self.name} (Dealer) : \t" + generic_msg

    def shuffle(self):
        self.deck.shuffle()

    def give_card(self):
        return self.deck.full_deck.pop(0)

    def pay_player(self, amount):
        pass

    def collect_from_player(self):
        pass

    def __str__(self):
        return f"Hi! I'm {self.name}, I will be your dealer for the evening."
