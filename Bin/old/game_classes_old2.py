import pygame
import random
import time


class Card:

    def __init__(self, colour, symbol, owner):
        self.__colour = colour
        self.__symbol = symbol
        self.__image = pygame.image.load("assets/" + self.__colour + "_" + self.__symbol + ".png")
        self.__owner = owner

    def get_colour(self):
        return self.__colour

    def get_symbol(self):
        return self.__symbol

    def get_owner(self):
        return self.__owner

    def set_owner(self, owner):
        self.__owner = owner

    def get_image(self):
        return self.__image

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
        time.sleep(0.1)


class Deck:

    def __init__(self):
        self.__list_of_cards = []
        self.__list_of_player_cards = []
        self.current_card = None

        colours = ["Blue", "Green", "Red", "Yellow"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]
        for possible_colour in colours:
            for possible_symbol in symbols:
                card_obj = Card(colour=possible_colour, symbol=possible_symbol, owner="Pile")
                self.__list_of_cards.append(card_obj)

    def display_details_deck(self):
        for card in self.__list_of_cards:
            card.display_details_card()
            card.print_card_image()
        for card in self.__list_of_player_cards:
            card.display_details_card()
            card.print_card_image()

    def shuffle(self):
        random.shuffle(self.__list_of_cards)

    # def assign_owner(self, ):
    #     owner = Card.get_owner()

    def deal_7(self, player):
        for i in range(7):
            self.obtain_card(player)

    def obtain_card(self, owner):
        card = self.__list_of_cards[0]
        card.set_owner(owner.get_name())
        self.__list_of_cards = self.__list_of_cards[1:]
        self.__list_of_player_cards.append(card)

    def get_player_cards(self):
        return self.__list_of_player_cards

    def get_deck(self):
        return self.__list_of_cards


# # def add
#  def __init__(self, currentCards):
#      self.__currentCards = currentCards
#      for card in self.__currentCards:
#          card.set_owner('Pile')


class Player:

    def __init__(self, name):
        self.__name = name
        self.__score = 0

    def get_name(self):
        return self.__name

    def get_currentCards(self, cards):
        player_cards = []
        for card in cards:
            if card.get_owner() == self.__name:
                player_cards.append(card)

    def new_score(self, new_score):
        self.__score = new_score

    def get_score(self):
        return self.__score

    def save_score(self):
        # create a file called scores if not already present, and save player scores based on playerid
        pass

    def place_card(self):
        pass


# class Pile:


# class Pickup_Pile:
#     def __init__(self, currentCards):
#         self.__currentCards = currentCards
#
#         for card in deck.list_of_cards:
#             card.assign_owner("Pickup_Pile")
#
#     def remove_card(self):
#         pass

# class Pile:
#     cards = None
#     def __init__(self, currentCards):
#         self.__cards = []

#  def add

# deck = Deck() # example of shuffling cards and giving them to player named "Player" (hardcoded)
# player = Player()
# #  deck.create_pile()
# deck.display_details_deck()
# deck.shuffle()
# deck.obtain_card("Player")
# # deck.deal_7("Player")
# print("uierhgiuofehg")
# deck.display_details_deck()
# player.get_currentCards()

# deck = Deck()
# deck.shuffle()
# player1 = Player('Grace')
# player2 = Player('Marcus')
# deck.deal_7(player1)
# deck.deal_7(player2)
# deck.display_details_deck()
