#!/usr/bin/python

import os
import sys
file_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(file_path, './../'))
import deck_cards.card as card


def test_shuffle():
    myDeck = card.Deck()
    sufulled_deck = myDeck.shuffle()
    assert myDeck != sufulled_deck

def test_valid_card():
    my_card = card.Card("hearts", 1)
    show_card = my_card.show()
    assert show_card == "Ace of hearts"

def test_invalid_card():
    my_card = card.Card("hearts", 14)
    show_card = my_card.show()
    assert show_card != "forteen of hearts"

# def test_building_cards():
#     deck = card.Deck()
#     all_cards= deck.show()
