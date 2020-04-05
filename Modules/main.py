"""Draw 5 community cards from a deck and then repeatedly:
1. Draw two new 2-card hands from the deck. These are the hole cards.
2. Shows the community cards and the two hands to the player, asking them which hand is worth more
(or if they have the same value) when added to the community cards.
3. If the player gives the correct answer, they get one point and can continue.
4. If the player gives an incorrect answer, the game is over and the total score should be indicated.
5. The game is also over if there are not enough cards left in the deck to play another round.

Author: Kevin Burke

I affirm that I have carried out my academic endeavours with full academic honesty
- Kevin Burke"""

from poker_hand import PokerHand
from stud_poker_hand import StudPokerHand
from community_card_set import CommunityCardSet
from deck import Deck

MAX_HAND_SIZE = 5
MAX_HOLE_CARDS = 2


def play_1(player):
    """User decides whether Hand #1 or Hand #2 is worth more. If user answer matches
        the correct answer given by compare_to function, user gains 1 point; if user answers
        wrong or deck runs out of cards, game ends and score is printed."""
    playing = True
    deck = Deck()
    deck.shuffle()
    score = 0
    print(input("Welcome to the casino, " + player + ". Press Enter to play the game."))
    while playing:
        if deck.out():
            print("Deck is out of cards. Game over. Your score was ", str(score))
            playing = False
        else:
            hand_a = PokerHand()
            hand_b = PokerHand()
            for i in range(0, MAX_HAND_SIZE):
                card = deck.deal()
                hand_a.add_card(card)
            for i in range(0, MAX_HAND_SIZE):
                card = deck.deal()
                hand_b.add_card(card)
            print("Hand #1: ", hand_a)
            print("Hand #2: ", hand_b, "\n")
            user_answer = int(input("Which hand is worth more? "
                                    "Type 1 if Hand #1, -1 if Hand #2, and 0 if they are worth the same\n "))
            correct_answer = hand_a.compare_to(hand_b)
            if user_answer == correct_answer:
                print("Correct! Let's try again\n")
                score += 1
            else:
                print("Game over. Your score was ", str(score))
                playing = False


def play_2(player):
    """Runs the game"""
    playing = True
    score = 0
    deck = Deck()
    deck.shuffle()
    community_card_set = CommunityCardSet()
    for i in range(0, MAX_HAND_SIZE):
        card = deck.deal()
        community_card_set.add(card)
    print(input("Hello " + player + ", press enter to play!"))
    while playing:
        if deck.out():
            print("Deck is out of cards. Game over. Your score was ", str(score))
            playing = False
        else:
            stud_hand_1 = StudPokerHand(community_card_set)
            stud_hand_2 = StudPokerHand(community_card_set)
            for i in range(0, MAX_HOLE_CARDS):
                card = deck.deal()
                stud_hand_1.add_card(card)
            for i in range(0, MAX_HOLE_CARDS):
                card = deck.deal()
                stud_hand_2.add_card(card)
            print("Here are your community cards: ", community_card_set)
            print("Hand a: ", stud_hand_1)
            print("Hand b: ", stud_hand_2)
            answer = int(input("Enter 1 for hand a, -1 for hand b, or 0 if they are equal "))
            correct_answer = stud_hand_1.compare_to(stud_hand_2)
            if answer == correct_answer:
                print("CORRECT")
                print("-------------------------------------\n")
                score += 1
            else:
                print("Game over. Your score was", str(score))
                playing = False


if __name__ == "__main__":
    # play_2("Kevin")
    play_1("Kevin")