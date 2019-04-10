"""
    This is the player object which does not
    have much because everything is inhereted from Person
"""
from game.person import Person

class Player(Person):
    """
        This object basically gets cards and show them
    """
    def __init__(self, name):
        Person.__init__(self)
        self.name = name

    def show_hand(self):
        """
            This needed a little bit extra details so
            it has to be appended with some more text
        """
        generic_msg = Person.show_hand(self)
        return f"{self.name} (Player): \t" + generic_msg

    def __str__(self):
        return f"Hi! I'm {self.name}"
