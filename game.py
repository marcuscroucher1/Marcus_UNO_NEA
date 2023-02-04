import pygame
import time

import game_classes
import display_functions

display = display_functions.Display()
display.display_background()


deck = game_classes.Deck()
player1 = game_classes.Player(name="player1")

deck.deal_7(player1)
player1currentcards = player1.get_current_cards(deck.get_player_cards())

for card in player1currentcards:
    card_image = card.get_image()

    display.display_card(100,100,card_image)







image = pygame.image.load("assets/Blue_3.png")
display.display_card(100, 100, image)




display.dont_quit_pygame() # run this at the very end