"""
    This will have all the common values for the whole program
"""

__MIN_STAY_FOR_DEALER = 17
__MAX_FOR_BUST = 21
__BLACKJACK = 21

class NotEnoughCards(Exception):
    """
        Custom Exception for when there's no more cards in the deck
    """
    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr(self.value)
