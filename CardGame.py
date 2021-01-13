# CardGame.py
# Janna Thomas
# This manages the generic card game functions for the blackjack game. Contains class Card, Deck, and Player
# This code borrowed heavily from https://
# Requires files: Janna_Thomas_Blackjack_Main.py, PlayHand.py, DatabaseConnection.py, and Constants.py to run
# This file has no main function and cannot be run on its own


import random

ptsDict = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}


class Card:
    def __init__(self, suit, val, pts):
        self.suit = suit
        self.value = val
        self.points = pts

    def show(self):
        print("{:>4} of {}".format(self.value, self.suit), end='')

    def getCard(self):
        return self.value, self.suit


class Deck:
    def __init__(self):
        self.cards = []

    def create_shuffled_deck(self):
        # build deck
        for s in ["\u2660", "\u2663", "\u2665", "\u2666"]:
            for v in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.cards.append(Card(s, v, ptsDict[v]))
        # shuffle
        for i in range(len(self.cards) - 1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def show(self):
        for c in self.cards:
            c.show()

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self):
        self.hand = []
        self.points = 0

    def clearHand(self):
        while len(self.hand) > 0:
            self.hand.pop()

    def draw(self, local_deck, number):
        for x in range(number):
            self.hand.append(local_deck.drawCard())
        self.updatePts()
        return self

    # return all cards in the hand
    def showHand(self):
        for card in self.hand:
            card.show()
        return self

    # return only the dealer's first card
    def dealerHint(self):
        value, suit = self.hand[0].getCard()
        return value, suit

    def updatePts(self):
        self.points = 0
        for card in self.hand:
            self.points += card.points
        # if points > 21, look for aces to reduce point count
        if self.points > 21:
            for card in self.hand:
                if card.points == 11:
                    card.points = 1
                    self.points -= 10
                    break
