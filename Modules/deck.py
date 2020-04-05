"""A module containing a deck object

I affirm that I have carried out my academic endeavours with full academic honesty
- Kevin Burke"""

import random as r
from card import Card

SUITS = ['H', 'C', 'D', 'S']
RANKS = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

class Deck:
    def __init__(self):
        """Creates a deck containing cards of every possible combination of suits and values."""
        self.__fill_deck()

    def __fill_deck(self):
        self.__deck = []
        if len(self.__deck) == 0:
            for suit in SUITS:
                for rank in RANKS:
                    card = Card(suit, rank)
                    self.__deck.append(card)
            # r.shuffle(self.__deck)

    def deal(self):
        """Returns a card from the deck."""
        return self.__deck.pop()

    def shuffle(self):
        """Shuffles the deck."""
        return r.shuffle(self.__deck)

    def gather(self):
        """Replenishes the deck."""
        return self.__fill_deck()

    def __str__(self):
        """Returns the deck as a string."""
        return ", ".join([str(c) for c in self.__deck])

    def show_deck(self):
        """Prints the deck out as a string."""
        print(self.__str__)

    def is_empty(self):
        """Returns an empty deck."""
        return len(self.__deck) == 0

    def out(self):
        return len(self.__deck) < 4

    def size(self):
        """Returns the remaining number of cards in the deck."""
        return len(self.__deck)

    def test_deal(self):
        """Tests the deal method"""
        return self.deal()

    def test_is_empty(self):
        """Test the is_empty method"""
        return self.is_empty()

    def test_size(self):
        """Tests the test_size method"""
        return self.size()


if __name__ == "__main__":
    deck = Deck()
    print(deck)
    print(deck.deal())
    print(deck)
    print(deck.is_empty())
    print(deck.size())
