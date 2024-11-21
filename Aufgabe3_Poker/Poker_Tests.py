import unittest
from Poker import Karte, pruefe_hand


class TestPoker(unittest.TestCase):

    def test_royal_flush(self):
        hand = [
            Karte('10', "\u2660"),
            Karte('J', "\u2660"),
            Karte('Q', "\u2660"),
            Karte('K', "\u2660"),
            Karte('A', "\u2660"),
        ]
        pruefe_hand(hand)

    def test_drilling(self):
        hand = [
            Karte('9', "\u2665"),
            Karte('9', "\u2663"),
            Karte('9', "\u2666"),
            Karte('4', "\u2660"),
            Karte('7', "\u2665"),
        ]
        pruefe_hand(hand)

if __name__ == "__main__":
    unittest.main()
