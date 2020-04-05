"""Class creating an object representing 5 community cards

I affirm that I have carried out my academic endeavours with full academic honesty-
Kevin Burke"""

from card import Card
from deck import Deck


class CommunityCardSet:
    def __init__(self):
        """Creates community card object with a list attribute"""
        self.community_cards = []

    def add(self, card):
        """Adds a card to set of community cards"""
        self.community_cards.append(card)

    def get_card(self, i):
        """returns ith card from set of community cards"""
        return self.community_cards[i]

    def remove_card(self, i):
        """removes ith card from set of community cards and returns it"""
        return self.community_cards.pop(i)

    def __str__(self):
        """Creates string representation of CommunityCardSet object"""
        return " | ".join([str(c) for c in self.community_cards])

    def show_string(self):
        """Returns this string representation"""
        return self.__str__()

    def test_get_card(self):
        return self.get_card(3)

    def test_remove_card(self):
        return self.remove_card(3)


if __name__ == "__main__":
    community_hand = CommunityCardSet()
    print(community_hand)
    community_hand.add(Card('D', 9))
    community_hand.add(Card('C', 10))
    community_hand.add(Card('C', 8))
    community_hand.add(Card('H', 2))
    community_hand.add(Card('C', 4))
    print(community_hand.test_get_card())
    print(community_hand.test_remove_card())


