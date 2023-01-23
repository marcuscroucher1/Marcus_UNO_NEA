import pygame
import random

class Card:

    def __init__(self):
        self.__colour = None
        self.__symbol = None
        self.__image = None
        self.__owner = None

    def get_colour(self):
        return self.__colour

    def get_number(self):
        return self.__number

    def assign_owner(self, owner):
        self.__owner = owner

    def display_details(self):
        print(self.__colour, self.__number, self.__owner)

    def __str__(self):
        return self.__colour + str(self.__number) + str(self.__owner)


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