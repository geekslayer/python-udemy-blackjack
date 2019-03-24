
class Person():

    def __init__(self):
        self.hand = []

    def get_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        return " | ".join([x.visible_value for x in self.hand])
    
    def hand_total_value(self):
        return sum([x.value for x in self.hand])
