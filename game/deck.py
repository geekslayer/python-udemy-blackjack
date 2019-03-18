from Card import Card, Suit

class Deck():

    def __init__(self):
        self.full_deck = []

        for s in Suit:
            for i in range(1,14):
                self.full_deck.append(Card(s,i,i>=10,self.__get_card_value(i)))

    def shuffle(self):
        pass

    def give_card(self):
        pass

    def pay_player(self):
        pass

    def collect_from_player(self):
        pass

    def hand(self):
        pass

    def __get_card_value(self,card_number:int):
        if card_number == 1:
            return "A"
        elif card_number == 11:
            return "J"
        elif card_number == 12:
            return "Q"
        elif card_number == 13:
            return "K"
        elif card_number in (2,3,4,5,6,7,8,9,10):
            return str(card_number)
        else:
            return ""

    def __str__(self):
        return [x for x in self.full_deck]
