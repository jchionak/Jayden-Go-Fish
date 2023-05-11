"""
The player for a game of go fish.
"""

from card import *
from deck import *
from time import sleep
from random import randint


class GoFishPlayer:
    """
    A go fish player.

    Instance Attributes:
    - hand: a list of cards in the player's hand
    - matches: the matches the players has
    """

    name: str
    hand: list[Card] = None
    matches: list[Card] = None

    def __init__(self, name: str, hand: list[Card] = None, matches: list[Card] = None):
        if hand is None:
            self.hand = []
        if matches is None:
            self.matches = []
        self.name = name

    def draw(self, deck: Deck, num_cards: int) -> bool:
        """Draws cards from a deck and puts them in the player's hand."""

        try:
            self.hand += deck.draw(num_cards)
            return True
        except NotEnoughCardsError:
            return False

    def check_matches(self) -> None:
        """
        This method will check for any matches in the hand. It's pretty inefficient so only use this to check the
        initial hand. :(
        """
        for card in self.hand:
            for other_card in self.hand:
                if card is other_card:
                    pass
                elif card.value == other_card.value:
                    self.matches.append(card)
                    self.matches.append(other_card)
                    self.hand.remove(card)
                    self.hand.remove(other_card)

    def check_for_card(self, value: int):
        """
        Checks if the player currently has a card with the specified value, and if so, removes that card from their hand
        and returns it.
        """
        for i in range(len(self.hand)):
            if self.hand[i].value == value:
                return self.hand.pop(i)

        return None  # returns None if they don't have a match

    def go_fish(self, deck: Deck):
        """
        This method will draw a single card, check if it is a match with an existing card in the hand, and if it is,
        add both cards to matches
        """
        self.draw(deck, 1)
        # we know this will add the card to the last index of self.hand
        drawn_card = self.hand[-1]
        for card in self.hand:
            if card is drawn_card:
                pass
            elif card.value == drawn_card.value:
                self.matches.append(card)
                self.matches.append(drawn_card)
                self.hand.remove(card)
                self.hand.remove(drawn_card)
                return drawn_card

        return drawn_card

    def ask_for_card(self, card: Card, opponent):
        """
        Asks the specified opponent to check for a card of the specified value, and if they have it, adds the match to
        their matches.
        """
        if card in self.hand:
            retruned_card = opponent.check_for_card(card.value)
            if retruned_card is not None:
                self.hand.remove(card)
                self.matches.append(card)
                self.matches.append(retruned_card)
                return True
            else:
                return False
        else:
            raise CardNotInHandError

    def string_hand(self):
        """
        Returns a string version of the player's current hand.
        """
        string_hand = f'These are the cards in your hand:\n '

        for card in self.hand:
            string_hand += f'{card} \n '

        return string_hand

    def string_matches(self):
        """
        Returns a string version of the player's current matches.
        """
        string_matches = f'These are your current matches:' + '\n'

        for i in range(0, len(self.matches), 2):
            string_matches += f'{self.matches[i]} and {self.matches[i + 1]}' + '\n'

        return string_matches


class ComputerPlayer(GoFishPlayer):
    """
    A computer go fish player. This player will randomly choose a card to ask for from their hand.

    Instance Attributes:
    - hand: a list of cards in the player's hand
    - matches: the matches the player has
    """
    def choose_action(self, deck: Deck, opponent: GoFishPlayer):
        """
        A random card from the player's hand is chosen and asked for. If the other player has the card they asked for,
        those cards are added to the player's matches. If not, the player draws a card.
        """
        print(f"{self.name}'s turn!")

        sleep(0.2)

        desired_card = self.hand[randint(0, len(self.hand) - 1)]

        print(f'{self.name} is asking for a {desired_card.value}.')

        success = self.ask_for_card(desired_card, opponent)

        if success:
            sleep(0.5)
            print(f'{opponent.name} gave {self.name} a {desired_card.value}!')
        else:
            sleep(0.5)
            print(f'Go Fish!')
            if not deck.is_empty():
                self.go_fish(deck)
                sleep(0.3)
                print(f'{self.name} drew a card.')
            else:
                print(f'The deck is empty, so {self.name} did not draw a card.')


class HumanPlayer(GoFishPlayer):
    """
    A human go fish player. The player must input numbers in order to choose what actions to take during their turn.
    """
    def choose_action(self, deck: Deck, opponent: GoFishPlayer):
        """
        The player is able to view their hand, view their matches, or choose a card to ask for. The player must input
        the corresponding number in order to select their action.
        """
        print(f"{self.name}'s turn!")

        sleep(0.2)

        print(f'Input 1 to check your hand, 2 to check matches, and 3 to choose a card to ask for.')

        sleep(0.2)

        selection = input(f'Make your selection (do not add a space after the number!): ')

        while selection != '3':
            if selection == '1':
                print(self.string_hand())
                sleep(0.5)
                selection = input(f'Input 1 to check your hand, 2 to check matches, and 3 to choose a card to ask for.')
            elif selection == '2':
                print(self.string_matches())
                sleep(0.5)
                selection = input(f'Input 1 to check your hand, 2 to check matches, and 3 to choose a card to ask for.')
            else:
                selection = input(f'Input 1 to check your hand, 2 to check matches, and 3 to choose a card to ask for.')

        print(f'Input the associated number of the card you want to ask for.')

        for i in range(0, len(self.hand)):
            print(f'{i}: {self.hand[i]}')

        print(f'Note: inputting a number less than 0 will result in asking for card 0, and inputting a number greater '
              f'than the highest card number will result in asking for the last card.')
        sleep(0.5)
        card_number = input('Which card do you want to ask for? (Input the associated number, not the value of the card): ')

        while True:
            try:
                card_number = int(card_number)
            except ValueError:
                card_number = input('Please input a number. ')
                continue
            else:
                break

        if card_number < 0:
            card_number = 0
        elif card_number >= len(self.hand):
            card_number = len(self.hand) - 1

        desired_card = self.hand[card_number]

        print(f'{self.name} is asking for a {desired_card.value}.')

        success = self.ask_for_card(desired_card, opponent)

        if success:
            sleep(0.5)
            print(f'{opponent.name} gave {self.name} a {desired_card.value}!')
        else:
            sleep(0.5)
            print(f'Go Fish!')
            if not deck.is_empty():
                self.go_fish(deck)
                sleep(0.3)
                print(f'{self.name} drew a card.')
            else:
                print(f'The deck is empty, so {self.name} did not draw a card.')

    def go_fish(self, deck: Deck):
        """
        This method will draw a single card, check if it is a match with an existing card in the hand, and if it is,
        add both cards to matches
        """
        self.draw(deck, 1)
        # we know this will add the card to the last index of self.hand
        drawn_card = self.hand[-1]
        print(f"{self.name} drew a {drawn_card}.")
        for card in self.hand:
            if card is drawn_card:
                pass
            elif card.value == drawn_card.value:
                sleep(1)
                print(f"Match! Added {drawn_card} and {card} to matches.")
                sleep(1)
                self.matches.append(card)
                self.matches.append(drawn_card)
                self.hand.remove(card)
                self.hand.remove(drawn_card)
                return drawn_card

        return drawn_card


class CardNotInHandError(Exception):
    """
    Called when a player tries to use a card not in their hand
    """
    def __str__(self): return "The player doesn't have that card in their hand."
