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
        print(self.__colour, self.__number, self.__owner) #

    def __str__(self):
        return self.__colour + str(self.__symbol) + str(self.__image)

    def print_card(self): # this print card funtion exists to display the image of the card which is
        pygame.init()
        X = 388
        Y = 562
        screen = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('image')
        image = self.__image
        screen.blit(image, (0, 0))
        pygame.display.flip()
        status = True
        while (status):
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False
        pygame.quit()



class Deck:

    def __init__(self):
        list_of_cards = []

        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        possible_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for possible_colour in filename_colours:
            for possible_symbol in possible_symbols:
                card_obj = Card(colour=possible_colour, symbol=possible_symbol)
                list_of_cards.append(card_obj)
        for card in list_of_cards: # picks the card that matches the one according to the line underneath this
            if card.get_symbol() == '5' and card.get_colour() == 'Yellow': # will find a card that is of number 5 and
                # colour yellow, and if exists, prints its matching image using the print function.
                card.print_card()


obj = Deck()    # creates an object(think like a table) called obj, and creates it using the 'instructions' set out by the Deck Class.




