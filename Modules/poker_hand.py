"""A module containing a hand object

I affirm that I have carried out my academic endeavours with full academic honesty
- Kevin Burke"""

from card import Card


class PokerHand:
    def __init__(self):
        """Creates a PokerHand object with a list attribute"""
        self.hand = []

    def add_card(self, card):
        """Adds a card to the PokerHand object"""
        self.hand.append(card)

    def get_card(self, i):
        """Return the ith card of player's hand"""
        return self.hand[i]

    def remove_card(self, i):
        """Remove the ith card of the player's hand and return it."""
        return self.hand.pop(i)

    def __str__(self):
        """Creates string representation of PokerHand object"""
        return ", ".join([str(c) for c in self.hand])

    def show_string(self):
        """Returns this string representation"""
        return self.__str__()

    def test_get_card(self):
        return self.get_card(3)

    def test_remove_card(self):
        return self.remove_card(3)

    def is_pair(self):
        """Determines whether or not a PokerHand is a pair

        :return: True if hand contains two equal ranks, False if not
        """
        singles = []
        pairs = []
        for i in range(0, len(self.hand)):
            rank = Card.get_rank(self.get_card(i))
            if rank not in singles:
                singles.append(rank)
            else:
                pairs.append(rank)
        if len(pairs) > 0:
            return True
        return False

    def is_two_pair(self):
        """Determines whether or not a PokerHand is a two pair

        :return: True if two pairs of ranks (or four individual
        ranks) are equal, False if not
        """
        singles = []
        pairs = []
        for i in range (0, len(self.hand)):
            rank = Card.get_rank(self.get_card(i))
            if rank not in singles:
                singles.append(rank)
            else:
                pairs.append(rank)
        if len(pairs) > 2:
            return True
        if len(pairs) == 2:
            if pairs[0] == pairs[1]:
                return False
            return True
        else:
            return False

    def is_flush(self):
        """Determines whether or not a PokeHand is a flush

        :return: True if all five suits are equal, False if not
        """
        suits = []
        for i in range(0, len(self.hand)):
            card = self.get_card(i)
            suit = Card.get_suit(card)
            suits.append(suit)
        if len(set(suits)) == 1:
            return True
        return False

    def get_better_high_card(self, other):
        """Compares two PokerHands and determines which has a better high card

        :param self: list of cards
        :param other: list of cards
        :return: 1 if hand_a has the superior high card, -1 if hand_b does
        """
        ranks1 = []
        ranks2 = []
        for i in range(0, len(self.hand)):
            card = self.get_card(i)
            rank = Card.get_rank(card)
            ranks1.append(rank)
        for i in range(0, len(other.hand)):
            card = other.get_card(i)
            rank = Card.get_rank(card)
            ranks2.append(rank)
        ranks1 = sorted(ranks1, reverse=True)
        ranks2 = sorted(ranks2, reverse=True)
        #print(ranks1)
        #print(ranks2)
        for i in range(0, len(ranks1)):
            if ranks1[i] > ranks2[i]:
                return 1
            elif ranks1[i] < ranks2[i]:
                return -1
            else:
                return 0

    def is_three_of_a_kind(self):
        singles = []
        pairs = []
        for i in range(0, len(self.hand)):
            card = self.get_card(i)
            a_rank = Card.get_rank(card)
            if a_rank not in singles:
                singles.append(a_rank)
            else:
                pairs.append(a_rank)
        pairs = sorted(pairs, reverse=True)
        if len(pairs) == 2:
            if pairs[0] == pairs[1]:
                return True
            if pairs[0] == pairs[1]:
                return True
            return False
        return False

    def get_better_pair(self, other):
        """Compares between two PokerHands and determines which has a better pair

        :return: 1 if hand_a has superior pair/ high card, -1 if hand_b does
        """
        a_singles = []
        b_singles = []
        pairs1 = []
        pairs2 = []
        for i in range(0, len(self.hand)):
            card = self.get_card(i)
            a_rank = Card.get_rank(card)
            if a_rank not in a_singles:
                a_singles.append(a_rank)
            else:
                pairs1.append(a_rank)
        for i in range(0, len(other.hand)):
            card = other.get_card(i)
            b_rank = Card.get_rank(card)
            if b_rank not in b_singles:
                b_singles.append(b_rank)
            else:
                pairs2.append(b_rank)
        a_singles = sorted(a_singles, reverse=True)
        b_singles = sorted(b_singles, reverse=True)
        pairs1 = sorted(pairs1, reverse=True)
        pairs2 = sorted(pairs2, reverse=True)
        # Now whatever is in pairs is a duplicate number
        # removing extra pair from threes of a kind to a allow for iteration through both lists
        if self.is_three_of_a_kind():
            pairs1.pop()
        if other.is_three_of_a_kind():
            pairs2.pop()
        if pairs1 != pairs2:
            for i in range(0, len(pairs1)):
                if pairs1[i] > pairs2[i]:
                    return 1
                elif pairs1[i] < pairs2[i]:
                    return -1
        else:
            for i in range(0, len(a_singles)):
                for s in range(0, len(b_singles)):
                    if a_singles[i] > b_singles[s]:
                        return 1
                    elif a_singles[i] < b_singles[s]:
                        return -1

    def get_better_two_pair(self, other):
        """Compares between two PokerHands and determines which has a better
        two pair

        :return: 1 if hand_a has superior pair/ high card, -1 if hand_b does
        """
        a_singles = []
        b_singles = []
        pairs1 = []
        pairs2 = []
        for i in range(0, len(self.hand)):
            card = self.get_card(i)
            a_rank = Card.get_rank(card)
            if a_rank not in a_singles:
                a_singles.append(a_rank)
            else:
                pairs1.append(a_rank)
        for i in range(0, len(other.hand)):
            card = other.get_card(i)
            b_rank = Card.get_rank(card)
            if b_rank not in b_singles:
                b_singles.append(b_rank)
            else:
                pairs2.append(b_rank)
        a_singles = sorted(a_singles, reverse=True)
        b_singles = sorted(b_singles, reverse=True)
        pairs1 = sorted(pairs1, reverse=True)
        pairs2 = sorted(pairs2, reverse=True)
        # Now whatever is in pairs is a duplicate number
        # print(a_singles)
        # print(b_singles)
        # print(pairs1)
        # print(pairs2)
        if pairs1 != pairs2:
            for i in range(0, len(pairs1)):
                if pairs1[i] > pairs2[i]:
                    return 1
                elif pairs1[i] < pairs2[i]:
                    return -1
        else:
            for i in range(0, len(a_singles)):
                if a_singles[i] > b_singles[i]:
                    return 1
                elif a_singles[i] < b_singles[i]:
                    return -1

    def get_better_flush(self, other):
        """Checks which of two flushes is worth more by comparing ranks of each hand
        ::return: 1 if hand_a wins, -1 if hand_b wins
        """
        return self.get_better_high_card(other)

    def same_worth(self, other):
        """Checks to see if ranks are the same for each hand
        :return: True if hands are same, False if not"""

        if not self.is_flush() and not other.is_flush():
            ranks1 = []
            ranks2 = []
            for i in range(0, len(self.hand)):
                card1 = self.get_card(i)
                rank1 = card1.get_rank()
                ranks1.append(rank1)
            for s in range(0, len(other.hand)):
                card2 = other.get_card(s)
                rank2 = card2.get_rank()
                ranks2.append(rank2)
                #print(rank2)
            ranks1.sort()
            ranks2.sort()
            # print(ranks2)
            if ranks1 == ranks2:
                return True
            return False

    def compare_to(self, other):
        """ Determines how this hand compares to another hand, returns
        positive, negative, or zero depending on the comparison.
        :param self: The first hand to compare
        :param other: The second hand to compare
        :return: a negative number if self is worth LESS than other, zero
        if they are worth the SAME, and a positive number if
        self is worth MORE than other
        """
        if self.same_worth(other):
            print('condition a')
            return 0
        """if (self.is_pair(hand_a) or self.is_two_pair(hand_a) or self.is_flush(hand_a)) and \
                not (self.is_pair(hand_b) or self.is_two_pair(hand_b) or self.is_flush(hand_b)):"""
        if (self.is_pair() or self.is_two_pair() or other.is_flush()) and \
                not (other.is_pair() or other.is_two_pair() or other.is_flush()):
            #print('condition b')
            return 1
        if self.is_two_pair() and not (other.is_two_pair() or other.is_flush()):
            #print('condition c')
            return 1
        if self.is_flush() and not other.is_flush():
            #print('condition d')
            return 1
        if not (self.is_pair() or self.is_two_pair() or self.is_flush()) and \
                (other.is_pair() or other.is_two_pair() or other.is_flush()):
            #print('condition e')
            return -1
        if (self.is_pair() and not self.is_two_pair()) and (other.is_two_pair() or other.is_flush()):
            #print('condition f')
            return -1
        if self.is_two_pair() and other.is_flush():
            print('condition g')
            return -1
        if self.is_pair() and other.is_pair():
            return self.get_better_pair(other)
        if self.is_two_pair() and other.is_two_pair():
            return self.get_better_two_pair(other)
        if self.is_flush() and other.is_flush():
            #print('condition i')
            return self.get_better_flush(other)
        else:
            #print('condition j')
            return self.get_better_high_card(other)


if __name__ == "__main__":
    a_hand = PokerHand()
    other_hand = PokerHand()
    a_hand.add_card(Card('C', 11))
    a_hand.add_card(Card('H', 8))
    a_hand.add_card(Card('H', 9))
    a_hand.add_card(Card('H', 7))
    a_hand.add_card(Card('D', 8))
    print(a_hand.hand)
    other_hand.add_card(Card('C', 7))
    other_hand.add_card(Card('D', 7))
    other_hand.add_card(Card('C', 10))
    other_hand.add_card(Card('H', 8))
    other_hand.add_card(Card('C', 8))
    print(a_hand.test_get_card())
    print(a_hand.test_remove_card())
