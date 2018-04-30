import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    suits = ["Spades", "Clubs", "Hearts", "Diamonds"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    def __init__(self):
        self.cards = [Card(suit, value) for suit in Deck.suits for value in Deck.values]

    def __repr__(self):
        return "Deck of {} cards".format(self.count())

    def count(self):
        return len(self.cards)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        else:
            return random.shuffle(self.cards)

    def _deal(self, num):
        if self.count() == 0:
            raise ValueError("All cards have been dealt")
        else:
            actual = min([self.count(), num])
            cards = self.cards[-actual:]
            self.cards = self.cards[:-actual]
            return cards

    def deal_card(self):
        return self._deal(1)[0]

    def deal_hand(self, num):
        return self._deal(num)
