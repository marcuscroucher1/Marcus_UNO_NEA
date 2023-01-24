import pygame
import random


class Card:

    def __init__(self, colour, symbol, owner):
        self.__colour = colour
        self.__symbol = symbol
        self.__image = pygame.image.load("assets/" + self.__colour + "_" + self.__symbol + ".png")
        self.__owner = owner

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


class Deck:

    def __init__(self):
        list_of_cards = []

        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        possible_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for possible_colour in filename_colours:
            for possible_symbol in possible_symbols:
                image = "assets/" + possible_colour + "_" + possible_symbol + ".png"
                colour = possible_colour
                symbol = possible_symbol
                print("")
                print(image)
                print(colour)
                print(symbol)


obj = Deck()

