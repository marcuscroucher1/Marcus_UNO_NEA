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



    def print_card_image(self): # this print card function exists to display the image of the card which is
        pygame.init()
        X = 388
        Y = 562
        screen = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('image')
        image = self.__image
        screen.blit(image, (0, 0))
        pygame.display.flip()
        # status = True
        # while (status):
        #     for i in pygame.event.get():
        #         if i.type == pygame.QUIT:
        #             status = False
        # pygame.quit()



class Deck:

    def __init__(self):
        self.list_of_cards = []

        colours = ["Blue", "Green", "Red", "Yellow"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        for possible_colour in colours:
            for possible_symbol in symbols:
                card_obj = Card(colour=possible_colour, symbol=possible_symbol) #temporary object
                self.list_of_cards.append(card_obj)
                # card_obj.print_card_image()


    def shuffle(self):
        random.shuffle(self.list_of_cards)

        for eachcard in self.list_of_cards: # this is useful for showing that the object does in fact contain all the data - this loops through the object and prints all of the data.
            eachcard.print_card_image()
            print(eachcard.get_colour())
            print(eachcard.get_symbol())




obj = Deck()    # creates an object(think like a table) called obj, and creates it using the 'instructions' set out by the Deck Class.




