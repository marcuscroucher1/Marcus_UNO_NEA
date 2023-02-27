import pygame
import random
import time

import display_functions


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
        self.__list_of_face_up_deck = []
        self.__list_of_player_cards = []
        self.__list_of_placed_cards = []
        self.current_card = None

        colours = ["Blue", "Green", "Red", "Yellow"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]
        for possible_colour in colours:
            for possible_symbol in symbols:
                card_obj = Card(colour=possible_colour, symbol=possible_symbol, owner="pickupPile")
                self.__list_of_face_up_deck.append(card_obj)

    def display_details_deck(self):
        for card in self.__list_of_face_up_deck:
            card.display_details_card()
            card.print_card_image()
        for card in self.__list_of_player_cards:
            card.display_details_card()
            card.print_card_image()
        for card in self.__list_of_placed_cards:
            card.display_details_card()

    def shuffle(self):
        random.shuffle(self.__list_of_face_up_deck)

    def deal_7(self, player):
        for i in range(7):
            self.obtain_card(player)

    def obtain_card(self, owner):
        card = self.__list_of_face_up_deck[0]
        card.set_owner(owner.get_name())
        self.__list_of_face_up_deck = self.__list_of_face_up_deck[1:]
        self.__list_of_player_cards.append(card)

    def get_player_cards(self):
        return self.__list_of_player_cards

    def get_deck(self):
        return self.__list_of_face_up_deck

    def get_current_deck_top_card(self):
        return self.__list_of_face_up_deck[0]

    def get_current_deck_bottom_card(self):
        return self.__list_of_face_up_deck[-1]

    def place_card(self, card): # pass in card as no. in array of current cards
        self.__list_of_placed_cards.append(card)
        # for card in self.__list_of_player_cards:
        #     if card.get_owner = player
        #         self.__list_of_player_cards


    def get_current_placed_card(self):
        return self.__list_of_placed_cards[-1]

    def place_first_card(self):
        self.__list_of_placed_cards.append(self.__list_of_face_up_deck[0])
        self.__list_of_face_up_deck = self.__list_of_face_up_deck[1:]

class Player:

    def __init__(self, name, opponentNumber):
        self.__name = name
        self.__score = 0
        self.__opponentNumber = opponentNumber

    def get_name(self):
        return self.__name

    def get_current_cards(self, cards):
        player_cards = []
        for card in cards:
            if card.get_owner() == self.__name:
                player_cards.append(card)

        for x in player_cards: # for debugging
            Card.display_details_card(x) # for debugging
        return player_cards

    def place_selected_card(self, card, deckName):
        card.set_owner(owner="placedCardsPile")
        deckName.place_card(card)


    def display_current_cards(self, deckName, displayName, xposition, yposition, timeSleep, scale, xpositiontoadvance): # use
        # with
        # redraw_player_deck
        currentcards = self.get_current_cards(deckName.get_player_cards())
        for card in currentcards:
            time.sleep(timeSleep)
            card_image = card.get_image()

            displayName.display_card(xposition, yposition, card_image, scale)
            xposition += xpositiontoadvance

    def redraw_player_deck(self, deckName, displayName):

        # yposition = 115
        # timeSleep = 0.05

        coordinates = displayName.get_coordinate_set(self.__opponentNumber)

        PlayerSquare_x = coordinates[0]
        PlayerSquare_y = coordinates[1]
        card_x = coordinates[2]
        card_y = coordinates[3]

        displayName.draw_bg_opponent(PlayerSquare_x, PlayerSquare_y)

        displayName.display_text((card_x + 6), (card_y - 45), self.__name, 1) # 1 means medium size

        self.display_current_cards(deckName, displayName, card_x, card_y, 0.05, 0.1, 16)

        #self.display_current_cards(deckName, displayName, yposition, timeSleep)

    def redraw_client_cards(self, deckName, displayName):
        self.display_current_cards(deckName, displayName, 284, 492, 0.05, 0.32, 140)

    def redraw_client_name(self, display):
        display.display_text(44, 609, self.__name, 2)









    def new_score(self, new_score):
        self.__score = new_score

    def get_score(self):
        return self.__score

    def save_score(self):
        # create a file called scores if not already present, and save player scores based on player id
        pass