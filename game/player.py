from game.person import Person

import game.common

class Player(Person):

    def __init__(self, name):
        Person.__init__(self)
        self.name = name

    def show_hand(self):
        generic_msg = Person.show_hand(self)
        return f"{self.name} (Player): \t" + generic_msg

    def __str__(self):
        return f"Hi! I'm {self.name}"
