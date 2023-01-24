import pygame
import random


class Card:

    def __init__(self, colour, symbol):
        self.__colour = colour
        self.__symbol = symbol
        self.__image = pygame.image.load("assets/" + self.__colour + "_" + self.__symbol + ".png")
        self.__owner = None

    def get_colour(self):
        return self.__colour

    def get_symbol(self):
        return self.__symbol

    def assign_owner(self, owner):
        self.__owner = owner

    def display_details(self):
        print(self.__colour, self.__symbol, self.__owner)

    def __str__(self):
        return self.__colour + str(self.__symbol) + str(self.__image)

    def print_card_image(self):
        pygame.init()
        x = 388
        y = 562
        screen = pygame.display.set_mode((x, y))
        pygame.display.set_caption('image')
        image = self.__image
        screen.blit(image, (0, 0))
        pygame.display.flip()


class Deck:

    def __init__(self):
        self.list_of_cards = []

        colours = ["Blue", "Green", "Red", "Yellow"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]
        for possible_colour in colours:
            for possible_symbol in symbols:
                card_obj = Card(colour=possible_colour, symbol=possible_symbol)
                self.list_of_cards.append(card_obj)

    def shuffle(self):
        random.shuffle(self.list_of_cards)
