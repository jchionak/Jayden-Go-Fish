"""
An implementation of a deck of cards in Python
"""

from random import randint
from Jayden-Go-Fish.card import Card


class Deck:
    """
    A deck that holds 52 cards. Decks will always hold exactly 52 cards.

    Instance Attributes:
    - cards: a list of cards in the deck
    """

    def __init__(self) -> None:
        self.cards = []

    def is_empty(self) -> bool:
        """
        Returns whether the deck is currently empty.

        >>> deck = Deck()
        >>> deck.add_cards_jokers()
        >>> deck.is_empty()
        False
        """
        return self.cards == []

    def add_cards_jokers(self) -> None:
        """
        This method will add 54 cards to the deck, including the two jokers.
        """
        self.cards = []
        red_suits = {'Hearts', 'Diamonds'}
        black_suits = {'Clubs', 'Spades'}
        values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

        for suit in red_suits:
            for value in values:
                card = Card(suit, 'Red', value)
                self.cards.append(card)

        for suit in black_suits:
            for value in values:
                card = Card(suit, 'Black', value)
                self.cards.append(card)

        self.cards.append(Card('Joker', 'Red', 1))
        self.cards.append(Card('Joker', 'Black', 1))

    def add_cards_no_jokers(self) -> None:
        """
        This method will add 52 cards to the deck, with no jokers.
        """
        self.cards = []
        red_suits = {'Hearts', 'Diamonds'}
        black_suits = {'Clubs', 'Spades'}
        values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13}

        for suit in red_suits:
            for value in values:
                card = Card(suit, 'Red', value)
                self.cards.append(card)

        for suit in black_suits:
            for value in values:
                card = Card(suit, 'Black', value)
                self.cards.append(card)

    def shuffle(self) -> None:
        """
        This method will randomly shuffle the deck.
        """
        cards = []
        starting_len = len(self.cards)

        for _ in range(0, starting_len):
            random_card = randint(0, len(self.cards) - 1)
            cards.append(self.cards[random_card])
            self.cards.pop(random_card)

        self.cards = cards

    def draw(self, num_cards: int):
        """
        This method will return the number of cards specified and remove those cards from the deck.
        It will the last cards in the deck.
        """

        hand = []

        if len(self.cards) >= num_cards:

            for _ in range(0, num_cards):
                hand.append(self.cards.pop())

            return hand

        else:
            raise NotEnoughCardsError


class NotEnoughCardsError(Exception):
    """This error will be raised when there aren't enough cards in the deck for the desired draw."""

    def __str__(self): return "The deck doesn't have enough cards for the desired draw."
