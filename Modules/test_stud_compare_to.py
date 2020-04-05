"""Testing all compare_to cases of stud_poker_hand module

I affirm that I have carried out my academic endeavours with full academic honesty-
Kevin Burke"""

import sys
from testing import assert_equals, assert_in, fail_on_error, start_tests, finish_tests
from community_card_set import CommunityCardSet
from stud_poker_hand import StudPokerHand
from card import Card

###
# Testing existence of required classes and methods
###


def test_create_community_cards():
    try:
        community = CommunityCardSet()
        for s, v in [('H', 2), ('H', 14), ('D', 11), ('S', 8), ('C', 8)]:
            community.add(Card(s, v))
        community_cards_string = str(community)
        for s, v in [('H', 2), ('H', 14), ('D', 11), ('S', 8), ('C', 8)]:
            msg = "The community set's string representation should contain the string " \
                  + "representation of the card " + str((s, v))
            assert_in(msg, str(Card(s, v)), community_cards_string)
    except:
        fail_on_error(
            "Trying to create a community card set and adding cards to it.",
            sys.exc_info())


def test_create_stud_poker_hand():
    try:
        community = CommunityCardSet()
        for s, v in [('H', 2), ('H', 14), ('D', 11), ('S', 8), ('C', 8)]:
            community.add(Card(s, v))
        a_hand = StudPokerHand(community)
        assert_equals("Created a new StudPokerHand object.", True, type(a_hand) is StudPokerHand)
    except:
        fail_on_error("Trying to create a StudPokerHand object.", sys.exc_info())


def test_add_to_stud_poker_hand():
    try:
        community = CommunityCardSet()
        for s, v in [('H', 2), ('H', 14), ('D', 11), ('S', 8), ('C', 8)]:
            community.add(Card(s, v))
        a_hand = StudPokerHand(community)
        a_hand.add_card(Card('S', 11))
        a_hand.add_card(Card('S', 10))
        assert_equals("Making sure that StudPokerHand object has add_card method.",
                      True,
                      type(a_hand) is StudPokerHand)
    except:
        fail_on_error("Trying to create a StudPokerHand object and add cards to it.",
                      sys.exc_info())

###
# Testing compare_to
###

def test_compare_to_safe(msg, community_cards, hole_cards_a, hole_cards_b, expected):
    try:
        community = CommunityCardSet()
        for s, v in community_cards:
            community.add(Card(s, v))
        hand_a = StudPokerHand(community)
        for s, v in hole_cards_a:
            hand_a.add_card(Card(s, v))
        hand_b = StudPokerHand(community)
        for s, v in hole_cards_b:
            hand_b.add_card(Card(s, v))
        msg += "\nA: {}\nB: {}".format(str(hole_cards_a), str(hole_cards_b))
        if expected > 0:
            assert_equals(msg, True, hand_a.compare_to(hand_b) > 0)
        elif expected < 0:
            assert_equals(msg, True, hand_a.compare_to(hand_b) < 0)
        else:
            assert_equals(msg, 0, hand_a.compare_to(hand_b))
    except:
        fail_on_error(msg, sys.exc_info())


def test_compare_flush_v_high_card():
    msg = "Hand A is flush; hand B is high card. A should win."
    community_cards = [('H', 2), ('H', 14), ('H', 11), ('S', 8), ('C', 8)]
    a_cards = [('H', 9), ('H', 5)]
    b_cards = [('H', 9), ('S', 5)]
    expected = 1   # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_high_cards():
    msg = "Hand A and Hand B are high cards. A should win."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 2), ('C', 4)]
    a_cards = [('S', 14), ('S', 3)]
    b_cards = [('C', 5), ('D', 11)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_high_cards_2():
    msg = "Hand A and Hand B are high cards. A should win."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 2), ('C', 4)]
    a_cards = [('S', 14), ('S', 5)]
    b_cards = [('C', 3), ('D', 14)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_two_pair_v_pair():
    msg = "Hand A is a two pair; Hand B is a pair. A should win."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 8), ('C', 4)]
    a_cards = [('S', 14), ('S', 4)]
    b_cards = [('C', 5), ('D', 11)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_flush_v_pair():
    msg = "Hand A is flush; hand B is a pair. A should win."
    community_cards = [('H', 2), ('H', 14), ('H', 11), ('S', 5), ('C', 8)]
    a_cards = [('H', 9), ('H', 4)]
    b_cards = [('H', 9), ('S', 5)]
    expected = 1   # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_flush_v_two_pair():
    msg = "Hand A is flush; hand B is a pair. A should win."
    community_cards = [('H', 2), ('H', 14), ('H', 11), ('S', 8), ('C', 8)]
    a_cards = [('H', 9), ('H', 5)]
    b_cards = [('H', 9), ('S', 2)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_pair_v_high_card():
    msg = "Hand A is a pair. Hand B is a high card. A should win."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 2), ('C', 4)]
    a_cards = [('S', 3), ('S', 2)]
    b_cards = [('C', 5), ('D', 11)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_two_pair_v_high_card():
    msg = "Hand A is a pair. Hand B is a high card. A should win."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 2), ('C', 4)]
    a_cards = [('S', 4), ('S', 2)]
    b_cards = [('C', 5), ('D', 11)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_flushes():
    msg = "Hand A and B are flushes, but A has a higher max."
    community_cards = [('H', 2), ('H', 14), ('H', 11), ('S', 8), ('C', 8)]
    a_cards = [('H', 13), ('H', 5)]
    b_cards = [('H', 9), ('H', 5)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_two_pair_v_two_pair():
    msg = "Hand A and B are two pairs, but hand A has one higher pair."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 8), ('C', 4)]
    a_cards = [('S', 2), ('S', 10)]
    b_cards = [('C', 14), ('D', 4)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_two_equal_two_pairs():
    msg = "Hand A and B each have two equal pairs, but A has the better high card."
    community_cards = [('D', 9), ('C', 10), ('C', 8), ('H', 8), ('C', 4)]
    a_cards = [('S', 14), ('S', 10)]
    b_cards = [('C', 2), ('D', 10)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_pair_v_pair():
    msg = "Hand A and B are pairs, but hand A has the higher pair."
    community_cards = [('H', 12), ('S', 6), ('D', 5), ('H', 10), ('S', 2)]
    a_cards = [('C', 11), ('H', 6)]
    b_cards = [('D', 6), ('S', 4)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_equal_pairs():
    msg = "Hand A and B are equal pairs, but Hand A has the better high card."
    community_cards = [('D', 9), ('C', 10), ('C', 6), ('H', 8), ('C', 4)]
    a_cards = [('S', 14), ('S', 8)]
    b_cards = [('C', 2), ('D', 8)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_compare_equal_hands():
    msg = "Hand A and B are worth the same."
    community_cards = [('D', 9), ('C', 10), ('C', 6), ('H', 8), ('C', 4)]
    a_cards = [('S', 2), ('S', 8)]
    b_cards = [('C', 2), ('D', 8)]
    expected = 0
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_two_pair_v_three_of_a_kind():
    msg = "Hand A is a two pair. Hand B is a pair (three of a kind). A should win."
    community_cards = [('H', 14), ('C', 10), ('C', 8), ('H', 8), ('C', 4)]
    a_cards = [('S', 2), ('S', 4)]
    b_cards = [('C', 11), ('D', 8)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)

def test_three_of_a_kind_v_pair():
    msg = "Hand A is a pair (three of a kind). Hand B is a pair. A has better pair."
    community_cards = [('H', 10), ('C', 4), ('C', 13), ('H', 2), ('C', 9)]
    a_cards = [('S', 10), ('S', 10)]
    b_cards = [('C', 6), ('D', 4)]
    expected = 1
    test_compare_to_safe(msg, community_cards, a_cards, b_cards, expected)


if __name__=="__main__":
    start_tests("Testing creation of community cards and stud poker hands.")
    test_create_community_cards()
    test_create_stud_poker_hand()
    test_add_to_stud_poker_hand()
    finish_tests()
    start_tests("Testing comparing two stud poker hands.")
    test_compare_flush_v_high_card()
    test_compare_flush_v_pair()
    test_compare_flush_v_two_pair()
    test_compare_two_pair_v_pair()
    test_compare_pair_v_high_card()
    test_compare_two_pair_v_high_card()
    test_compare_flushes()
    test_compare_two_pair_v_two_pair()
    test_compare_two_equal_two_pairs()
    test_compare_pair_v_pair()
    test_compare_equal_pairs()
    test_compare_high_cards()
    test_compare_high_cards_2()
    test_compare_equal_hands()
    test_two_pair_v_three_of_a_kind()
    test_three_of_a_kind_v_pair()
    finish_tests()