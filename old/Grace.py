import pygame
import random
class Card:
    def __init__(self, colour, symbol, image, owner = None):
        pass

class Deck:
    def __init__(self):
        # will generate the uno deck and assign the card assets to each card

        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        data_colours = ["b", "g", "r", "y"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for colour in filename_colours:
            for symbol in symbols:
                pass



