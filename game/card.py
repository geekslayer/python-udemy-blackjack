import suit

class Card():

    def __init__(self, suit:suit.Suit, value:int, is_face_card:bool, visible_value:str):
        self.suit:suit.Suit = suit
        self.value = value
        self.face = is_face_card
        self.visible_value = visible_value

    def __str__(self):
        return f"{self.visible_value} of {self.suit}"