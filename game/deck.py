from random import shuffle

from game.card import Card, Suit

class Deck():
    __amount_of_cards_of_one_suit = 13

    def __init__(self):
        self.full_deck = []

        for card_suit in Suit:
            for i in range(1, Deck.__amount_of_cards_of_one_suit+1):
                self.full_deck.append(Card(card_suit, i, i >= 10, self.__get_card_value(i)))

    def shuffle(self):
        shuffle(self.full_deck)

    @classmethod
    def __get_card_value(cls, card_number: int):
        if card_number in (2, 3, 4, 5, 6, 7, 8, 9, 10):
            return str(card_number)

        if card_number == 1:
            return "A"

        if card_number == 11:
            return "J"

        if card_number == 12:
            return "Q"

        if card_number == 13:
            return "K"

        return None

    def __str__(self):
        return f"This deck has {len(self.full_deck)} cards which here they are: \n" + \
               f"{[x.visible_value for x in self.full_deck]}"
