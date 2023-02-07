import pygame
import time
import game_classes
import display_functions


class GameStats:
    def __init__(self):
        self.__playerCount = 0

    def increasePlayerCount(self):
        self.__playerCount += 1

    def decreasePlayerCount(self):
        self.__playerCount -= 1

    def givePlayerCount(self):
        return self.__playerCount

class CreateDisplay:
    display = display_functions.Display()
    display.display_background()

class CreateDeck:
    deck = game_classes.Deck()



class CreatePlayer:
    def __init__(self, player_name,):
        player_name = game_classes.Player(name=str(player_name))
        deck.deal_7(player_name)
        currentcards = player_name.get_current_cards(deck.get)


class CreateGame:
    pass
 # integrate all above into this class