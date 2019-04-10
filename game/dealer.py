"""
    This is where all the magic happens for the dealer object
"""
from game.deck import Deck
from game.person import Person
from game.common import NotEnoughCards

class Dealer(Person):
    """
        This class inherits from Person which has a lot of stuff in common with the player
    """

    def __init__(self, name):
        Person.__init__(self)
        self.name = name
        self.deck = Deck()

    def show_hand(self):
        """
            Show the current hand
        """
        generic_msg = Person.show_hand(self)
        return f"{self.name} (Dealer) : \t" + generic_msg

    def show_first_hand(self):
        """
            Show the first hand because for the dealer
            until it's his turn we only see one card
        """
        generic_msg = str(self.hand[0]) + " | "
        return f"{self.name} (Dealer) : \t" + generic_msg

    def shuffle(self):
        """
            Shuffle all the cards before the round starts
        """
        self.deck.shuffle_deck()

    def has_enough_cards(self):
        """
            Check if there's enough cards left in the deck for a round
        """
        enough = len(self.deck.full_deck) > 6

        return enough

    def give_card(self):
        """
            Give a card from the deck to a player
        """
        has_enough = self.has_enough_cards()

        if has_enough:
            return self.deck.full_deck.pop(0)

        raise NotEnoughCards("No more cards, need new deck!")

    def pay_player(self, amount):
        """
            This would be a method that would pay the player.
            With a multiplier according to the hand in play.
        """

    def collect_from_player(self):
        """
            This would be if the player had to pay the dealer
        """

    def __str__(self):
        return f"Hi! I'm {self.name}, I will be your dealer for the evening."
