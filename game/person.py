"""
    Base class for main objects player and dealer
"""

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
