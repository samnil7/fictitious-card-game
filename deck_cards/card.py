#Import libraries
import random

class Card(object):
    def __init__(self, suit, val):
        self.suit = suit
        self.value = val

    # Implementing build in methods so that you can print a card object
    def __unicode__(self):
        return self.show()

    def __str__(self):
        return self.show()

    def __repr__(self):
    # This method returns an unambigious string representation of the card object
        return self.show()

    def show(self):
        """ This method maps the card number and string reprentation 
        Returns:
            card with suit and value. eg. "One of Ace"
        """
        if self.value == 1:
            val = "Ace"
        elif self.value == 2:
            val = "Two"
        elif self.value == 3:
            val = "Three"
        elif self.value == 4:
            val = "Four"
        elif self.value == 5:
            val = "Five"
        elif self.value == 6:
            val = "Six"
        elif self.value == 7:
            val = "Seven"
        elif self.value == 8:
            val = "Eight"
        elif self.value == 9:
            val = "Nine"
        elif self.value == 10:
            val = "Ten"
        elif self.value == 11:
            val = "Jack"
        elif self.value == 12:
            val = "Queen"
        elif self.value == 13:
            val = "King"
        else:
            val = self.value

        return "{} of {}".format(val, self.suit)

class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()

    # Display all cards in the deck
    def show(self):
        for card in self.cards:
            print(card.show())

    # Generate 52 cards
    def build(self):
        self.cards = []
        for suit in ['Hearts', 'Clubs', 'Diamonds', 'Spades']:
            for val in range(1, 14):
                self.cards.append(Card(suit, val))

    # Shuffle the deck
    def shuffle(self):
        random.shuffle(self.cards)

    # Return the top card
    def deal(self):
        return self.cards.pop()



class Player(object):
    def __init__(self):

        self.hand = []

    # Draw n number of cards from a deck
    # Returns true in n cards are drawn, false if less then that
    def draw(self, deck, num=1):
        for _ in range(num):
            card = deck.deal()
            if card:
                self.hand.append(card)
            else:
                return False
        return True

    # Display all the cards in the players hand
    def showHand(self):
        print("Two cards are: {}".format(self.hand))
        return self