import pygame
import game_classes
import game_create
import display_functions


class GameTurn:
    def __init__(self, player, deck, card):
        game_classes.Deck.place_card(card)

