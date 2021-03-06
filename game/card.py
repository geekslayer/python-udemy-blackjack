"""
    This will be the class for the card object
"""

from game.suit import Suit

class Card():
    """
        This will be the class for the card object
    """

    def __init__(self, suit, value, is_face_card, visible_value):
        self.suit = suit
        self.actual_value = value
        self.face = is_face_card
        self.visible_value = visible_value

        if self.face:
            self.value = 10
        else:
            self.value = self.actual_value

    def get_card_suit(self) -> Suit:
        """
            Get the suit of the current card
        """

        return self.suit

    def __str__(self):
        """
            This should print the card information, for now
            it's only the number but it should be value and suit

            i.e: {self.visible_value} of {self.suit.name}
        """

        return f"{self.visible_value}"
