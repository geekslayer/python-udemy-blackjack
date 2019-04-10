"""
    This deck object is at the middle of all
    this and is a crucial part of the game.
"""
from random import shuffle
from game.card import Card, Suit

class Deck():
    """
        This will hold 52 cards like a regular deck of cards.
        One by one we will remove the cards from the deck until no more.
    """
    __amount_of_cards_of_one_suit = 13

    def __init__(self):
        self.full_deck = []

        for card_suit in Suit:
            for i in range(1, Deck.__amount_of_cards_of_one_suit+1):
                self.full_deck.append(Card(card_suit, i, i >= 10, self.__get_card_value(i)))

    def shuffle_deck(self):
        """
            This will shuffle the deck and all the cards in it.

            Of course this should be done only when there's a new deck if not,
            this will still work but on a shorter deck
        """
        shuffle(self.full_deck)

    @classmethod
    def __get_card_value(cls, card_number: int):
        """
            This is to give the face value of a card.

            Numbers are easy, then the face card either J, Q, K or A.
        """
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
