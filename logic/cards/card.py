from logic.enums.card_type import CardType

class Card:
    def __init__(self):
        self.card_type = CardType.NONE
        self.cost = 0
        self.name = 'card'
        self.actions = []
        self.burnout = []
        self.resistance = 3
        self.fresh = True

    def my_type(self):
        return self.card_type