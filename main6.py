import pygame
import random

class Card:

    def __init__(self):
        self.__colour = colour
        self.__number = number
        self.__image = image
        self.__owner = owner



        # will generate the uno deck and assign the card assets to each card
        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        data_colours = ["b", "g", "r", "y"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for colour in range(len(filename_colours)):
            for symbol in symbols:
                image_filename = None
                image_filename = "assets/" + filename_colours[colour] + "_" + symbol + ".png"
        print(image_filename)


Card()