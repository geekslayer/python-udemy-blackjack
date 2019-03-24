from suit import Suit

class Card():
    """
        This will be the class for the card object
    """
    def __init__(self, suit, value, is_face_card, visible_value):
        self.suit = suit
        self.value = value
        self.face = is_face_card
        self.visible_value = visible_value

    def get_card_suit(self):
        return self.suit

    def __str__(self):
        """
            This should print the card information, for now 
            it's only the number but it should be value and suit

            i.e: {self.visible_value} of {self.suit.name}
        """
        return f"{self.visible_value}"
