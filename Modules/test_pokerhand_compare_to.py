"""Testing all compare_to cases of poker_hand module

I affirm that I have carried out my academic endeavours with full academic honesty-
Kevin Burke"""

import sys
from testing import assert_equals, assert_in, fail_on_error, start_tests, finish_tests
from poker_hand import PokerHand
from card import Card

###
# Testing existence of required classes and methods
###

def test_create_poker_hand():
    try:
        a_hand = PokerHand()
        assert_equals("Created a new PokerHand object.", True, type(a_hand) is PokerHand)
    except:
        fail_on_error("Trying to create a PokerHand object.", sys.exc_info())


def test_add_to_poker_hand():
    try:
        a_hand = PokerHand()
        a_hand.add_card(Card('S', 11))
        a_hand.add_card(Card('S', 10))
        assert_equals("Making sure that PokerHand object has add_card method.",
                      True,
                      type(a_hand) is PokerHand)
    except:
        fail_on_error("Trying to create a PokerHand object and add cards to it.",
                      sys.exc_info())


def test_str():
    try:
        a_hand = PokerHand()
        a_hand.add_card(Card('S', 11))
        a_hand.add_card(Card('S', 10))
        a_hand_string = str(a_hand)
        assert_in("Added card 'S11'. String representation of hand should contain 'Jack of Spades'.",
                  "Jack of Spades",
                  a_hand_string)
        assert_in("Added card 'S10'. String representation of hand should contain '10 of Spades'.",
                  "10 of Spades",
                  a_hand_string)
    except:
        fail_on_error("Runtime error when calling __str__ of PokerHand object.", sys.exc_info())


###
# Testing compare_to
###

def test_compare_to_safe(msg, cards_a, cards_b, expected):
    try:
        hand_a = PokerHand()
        for s, v in cards_a:
            hand_a.add_card(Card(s, v))
        hand_b = PokerHand()
        for s, v in cards_b:
            hand_b.add_card(Card(s, v))
        msg += "\nA: {}\nB: {}".format(str(cards_a), str(cards_b))
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
    a_cards = [('H', 2), ('H', 14), ('H', 11), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 8), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_flush_v_pair():
    msg = "Hand A is flush; hand B is a pair. A should win."
    a_cards = [('H', 2), ('H', 14), ('H', 11), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_flush_v_two_pair():
    msg = "Hand A is flush; hand B is a pair. A should win."
    a_cards = [('H', 2), ('H', 14), ('H', 11), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 14), ('D', 9), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_two_pair_v_pair():
    msg = "Hand A is a two pair; hand B is a pair. A should win."
    a_cards = [('C', 8), ('H', 14), ('H', 9), ('H', 8), ('D', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_two_pair_v_high_card():
    msg = "Hand A is a two pair; hand B is a high card. A should win."
    a_cards = [('C', 8), ('H', 11), ('H', 9), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 11), ('H', 14), ('H', 4), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_pair_v_high_card():
    msg = "Hand A is pair; hand B is a high card. A should win."
    a_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    b_cards = [('C', 3), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_flushes():
    msg = "Hand A is flush; hand B is a flush; A has the better high card."
    a_cards = [('H', 2), ('H', 14), ('H', 11), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 13), ('H', 11), ('H', 8), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_two_pair_v_two_pair():
    msg = "Hand A is a two pair; hand B is a two pair. A has one better pair."
    a_cards = [('C', 8), ('H', 14), ('D', 9), ('H', 8), ('H', 9)]
    b_cards = [('C', 2), ('H', 14), ('D', 9), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_two_equal_two_pairs():
    msg = "Hand A and Hand B are equal two pairs; Hand A has the better high card"
    a_cards = [('C', 8), ('H', 14), ('D', 9), ('H', 8), ('H', 9)]
    b_cards = [('C', 8), ('H', 13), ('C', 9), ('H', 8), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_pair_v_pair():
    msg = "Hand A is a pair; Hand B is a pair. A has the better pair."
    a_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 9), ('C', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 9), ('D', 2)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_equal_pairs():
    msg = "Hand A is a pair; Hand B is a pair. A has the better pair."
    a_cards = [('C', 2), ('H', 14), ('H', 13), ('H', 9), ('C', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 9), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_high_cards():
    msg = "Hand A is a high card; hand B is a high card. A has the better one."
    a_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    b_cards = [('C', 2), ('H', 13), ('H', 11), ('H', 2), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_high_cards_2():
    msg = "Hand A is a high card; hand B is a high card. A has the second best."
    a_cards = [('C', 5), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 4), ('H', 9)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_compare_equal_hands():
    msg = "Hand A and Hand B are worth the same."
    a_cards = [('H', 2), ('D', 14), ('C', 11), ('S', 2), ('S', 9)]
    b_cards = [('C', 2), ('H', 14), ('H', 11), ('H', 2), ('H', 9)]
    expected = 0  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_two_pair_v_three_of_a_kind():
    msg = "Hand A is a two pair; Hand B is a pair (three of a kind). A should win"
    a_cards = [('C', 2), ('H', 14), ('H', 2), ('H', 9), ('C', 9)]
    b_cards = [('C', 11), ('H', 14), ('H', 11), ('H', 9), ('D', 11)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)

def test_three_of_a_kind_v_pair():
    msg = "Hand A is a pair (three of a kind). Hand B is a pair. A has better pair."
    a_cards = [('C', 2), ('H', 14), ('D', 9), ('H', 9), ('C', 9)]
    b_cards = [('C', 11), ('H', 14), ('H', 7), ('H', 9), ('D', 7)]
    expected = 1  # 1 --> positive; -1 --> negative; 0 --> zero
    test_compare_to_safe(msg, a_cards, b_cards, expected)


if __name__=="__main__":
    start_tests("Testing creation of poker hands.")
    test_create_poker_hand()
    test_add_to_poker_hand()
    test_str()
    finish_tests()
    start_tests("Testing comparing two poker hands.")
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
    finish_tests()