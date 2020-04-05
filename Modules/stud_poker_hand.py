"""Class creating an object representing a stud poker hand consisting of 2 hole cards

I affirm that I have carried out my academic endeavours with full academic honesty-
Kevin Burke"""


from card import Card
from community_card_set import CommunityCardSet
from itertools import combinations
from poker_hand import PokerHand


class StudPokerHand:
    def __init__(self, community_cards):
        """Creates a StudPokerHand object with list and community card attributes"""
        self.stud_hand = []
        self.community_card_set = community_cards

    def add_card(self, card):
        """Adds a card to stud hand object"""
        self.stud_hand.append(card)

    def get_card(self, i):
        """Returns ith card from stud hand object"""
        return self.stud_hand[i]

    def remove_card(self, i):
        """Removes ith card from stud hand object and returns it"""
        return self.stud_hand.pop(i)

    def __str__(self):
        """Creates string representation of stud hand object"""
        return ", ".join([str(c) for c in self.stud_hand])

    def test_get_card(self):
        return self.get_card(3)

    def test_remove_card(self):
        return self.remove_card(3)

    def compare_to(self, other):
        """Compare this hand (self) to another hand (other) taking into
        account the community cards, and return a positive number,
        negative number, or zero depending on which is worth more.
        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: a negative number if self is worth LESS than other, zero
        if they are worth the SAME, and a positive number if self is worth
        MORE than other
        """
        best_hand1 = self.__get_best_five_card_hand()
        best_hand2 = other.__get_best_five_card_hand()
        if best_hand1.compare_to(best_hand2) > 0:
            return 1
        if best_hand1.compare_to(best_hand2) < 0:
            return -1
        else:
            return 0

    def __get_all_five_card_hands(self):
        """Determines all possible 5-card PokerHand objects from combined stud and community
        cards and returns them"""
        for i in range(0, len(self.community_card_set.community_cards)):
            card = self.community_card_set.get_card(i)
            self.add_card(card)
        five_card_hands = combinations(self.stud_hand, 5)
        a_list = []
        for combination in five_card_hands:
            hand = PokerHand()
            for i in range(0, len(combination)):
                card = combination[i]
                hand.add_card(card)
            a_list.append(hand)
        return a_list

    def __get_best_five_card_hand(self):
        """Determine the best possible 5-card PokerHand object from
        the available hole and community cards and return it.
        """
        hands = self.__get_all_five_card_hands()
        best_so_far = hands[0]
        for i in range(1, len(hands)):
            if hands[i].compare_to(best_so_far) > 0:
                best_so_far = hands[i]
        return best_so_far


if __name__ == "__main__":
    community_card_set = CommunityCardSet()
    community_card_set.add(Card('D', 9))
    community_card_set.add(Card('C', 10))
    community_card_set.add(Card('C', 8))
    community_card_set.add(Card('H', 2))
    community_card_set.add(Card('C', 4))
    stud_hand = StudPokerHand(community_card_set)
    stud_hand.add_card(Card('D', 2))
    stud_hand.add_card(Card('S', 3))
    other_stud_hand = StudPokerHand(community_card_set)
    other_stud_hand.add_card(Card('S', 5))
    other_stud_hand.add_card(Card('C', 6))
    print(stud_hand.compare_to(other_stud_hand))
    print(community_card_set.test_get_card())
    print(community_card_set.test_remove_card())