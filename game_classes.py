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

    def display_details_card(self):
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

    def display_details_deck(self):
        for card in self.list_of_cards:
            Card.display_details_card(card)

    def shuffle(self):
        random.shuffle(self.list_of_cards)

    def deal_7(self):
        for i in range(7):
            self.list_of_cards[i].assign_owner("Player")

class Player:

    def __init__(self, name, currentCards, score):
        self.__name = name
        self.__currentCards = currentCards
        self.__score = score

    def get_name(self):
        return self.__name

    def get_currentCards(self):
        return self.__currentCards

    def get_score(self):
        return self.__score

    def save_score(self):
        # create a file called scores if not already present, and save player scores based on playerid
        pass
    def place_card(self):
        pass








# deck = Deck() # example of shuffling cards and giving them to player named "Player" (hardcoded)
# deck.display_details_deck()
# deck.shuffle()
# deck.deal_7()
# print("uierhgiuofehg")
# deck.display_details_deck()
