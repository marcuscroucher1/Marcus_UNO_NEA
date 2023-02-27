import pygame
import random

class Card:

    def __init__(self):
        self.__colour = None
        self.__symbol = None
        self.__image = None
        self.__owner = None



        # will generate the uno deck and assign the card assets to each card
        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        data_colours = ["b", "g", "r", "y"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for colour in filename_colours:
            for symbol in symbols:
                self.__image = "assets/" + colour + "_" + symbol + ".png"
                self.__colour = colour
                self.__symbol = symbol
                print("")
                print(self.__image)
                print(self.__colour)
                print(self.__symbol)



Card()