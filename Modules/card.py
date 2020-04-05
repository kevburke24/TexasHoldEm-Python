"""A module containing a card object

I affirm that I have carried out my academic endeavours with full academic honesty
- Kevin Burke"""

ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
         'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
suits = {'Hearts': 'H', 'Clubs': 'C', 'Spades': 'S', 'Diamonds': 'D'}

class Card:
    def __init__(self, suit, rank):
        """Create a card from a given suit (string) and rank (integer)"""
        self.__suit = suit
        self.__rank = rank

    def get_rank(self):
        """Returns the rank of the card"""
        return self.__rank

    def get_suit(self):
        """Returns the suit of the card"""
        return self.__suit

    def convert_rank(self):
        """Using a dictionary, converts rank to proper string format"""
        for key in ranks:
            if ranks[key] == self.__rank:
                self.__rank = key
        return self.__rank

    def convert_suit(self):
        """Using a dictionary, converts suit to proper string format"""
        for key in suits:
            if suits[key] == self.__suit:
                self.__suit = key
        return self.__suit

    def __str__(self):
        """Makes internal representation of a card a string"""
        self.card = ''
        self.card = str(self.convert_rank()) + " of " + str(self.convert_suit())
        return str(self.card)

    def show_string(self):
        """Returns string representation of card"""
        return self.__str__


if __name__ == "__main__":
    card = Card('H', 11)
    print(card)