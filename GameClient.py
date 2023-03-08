import pygame
from Network import Network

width = 1280
height = 720
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("UNO_Client")

clientNumber = 0

class DataRecieve:
    def __init__(self, dataType, data):
        self.dataType = dataType
        self.data = data

    def recieve_player_redraw(self, playerName, deck, display):
        playerName.redraw_player_deck(deck, display)

