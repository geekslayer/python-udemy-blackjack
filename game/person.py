"""
    Base class for main objects player and dealer
"""
from game.deck import Deck
from game.common import NotEnoughCards

class Person():
    """
        Person is a base class than can be used either as a
        player or a dealer those are all common properties
        that both have
    """
    def __init__(self):
        self.hand = []
        self.previous_hands = []
        self.has_blackjack = False

    def throw_hand_away(self):
        """
            When the round is done we throw away the hand
        """
        [self.previous_hands.append(x) for x in self.hand]
        self.hand = []
        self.has_blackjack = False

    def get_hand(self, card):
        """
            Every card we receive we add it to our current hand
        """
        self.hand.append(card)

    def show_hand(self):
        """
            Show our current hand in a more friendly way
        """
        return " | ".join([x.visible_value for x in self.hand])

    def hand_total_value(self):
        """
            Give the real value of our hand including all face cards
        """
        hand_total = sum([x.value for x in self.hand])
        cards = [x.visible_value for x in self.hand]

        if 'A' in cards:
            hand_total += 10

            if hand_total > 21:
                hand_total -= 10

        return hand_total

    def is_busted(self):
        """
            Return the boolean if the person has a
            hand with a greater value than 21
        """
        return self.hand_total_value() > 21 #common.__MAX_FOR_BUST

class Player(Person):
    """
        This object basically gets cards and show them
    """
    def __init__(self, name):
        Person.__init__(self)
        self.name = name

    def show_hand(self):
        """
            This needed a little bit extra details so
            it has to be appended with some more text
        """
        generic_msg = Person.show_hand(self)
        return f"{self.name} (Player): \t" + generic_msg

    def __str__(self):
        return f"Hi! I'm {self.name}"

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
