
class Player():

    def __init__(self, name):
        self.name = name
        self.hand = []

    def get_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        print(*self.hand, sep =  " | ")

    def __str__(self):
        return f"Hi! I'm {self.name}"
