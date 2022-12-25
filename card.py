"""
Generates cards and a deck of cards.
"""


class Card:
    """
    A card to be used in a deck of cards. Note that jokers have suit = 'Joker' and always have a value of 1.

    Instance Attributes:
    - suit: the suit of the card (hearts, clubs, spades, diamonds)
    - colour: the colour of the card (red, black)
    - value: the card's value (note: ace = 1, jack = 11, queen = 12, king = 13)

    Representation Invariants:
    - self.suit in {'Hearts', 'Clubs', 'Spades', 'Diamonds', 'Joker'}
    - self.colour in {'Red', 'Black'}
    - 1 <= self.value <= 13
    """

    def __init__(self, suit: str, colour: str, value: int) -> None:
        self.suit = suit
        self.colour = colour
        self.value = value

    def __str__(self) -> str:
        return f'{self.value} of {self.suit}'
