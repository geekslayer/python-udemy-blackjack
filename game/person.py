
class Person():

    def __init__(self):
        self.hand = []
        self.previous_hands = []
        self.has_blackjack = False

    def throw_hand_away(self):
        [self.previous_hands.append(x) for x in self.hand]
        self.hand = []
        self.has_blackjack = False

    def get_hand(self, card):
        self.hand.append(card)

    def show_hand(self):
        return " | ".join([x.visible_value for x in self.hand])
    
    def hand_total_value(self):
        hand_total = sum([x.value for x in self.hand])
        cards = [x.visible_value for x in self.hand]

        if 'A' in cards:
            hand_total += 10
        
            if hand_total > 21:
                hand_total -= 10

        return hand_total

    def is_busted(self):
        return self.hand_total_value() > 21 #common.__MAX_FOR_BUST
