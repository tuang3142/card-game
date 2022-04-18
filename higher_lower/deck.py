import random
from card import *


class Deck:
    SUIT_TUPLE = ('Diamonds', 'Clubs', 'Hearts', 'Spades')
    RANK_VALUE_DICT = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5,
                       '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                       'Jack': 11, 'Queen': 12, 'King': 13}

    def __init__(self, window):
        self.starting_deck = []
        self.playing_deck = []
        for suit in self.SUIT_TUPLE:
            for rank, value in self.RANK_VALUE_DICT.items():
                card = Card(window, rank, suit, value)
                self.starting_deck.append(card)
        self.shuffle()

    def shuffle(self):
        self.playing_deck = self.starting_deck.copy()
        for card in self.playing_deck:
            card.conceal()
        random.shuffle(self.playing_deck)

    def get_card(self):
        return self.playing_deck.pop()

    def add_card(self, card):
        self.playing_deck.insert(0, card)
