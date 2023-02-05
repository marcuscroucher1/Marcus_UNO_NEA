import pygame
import time

import game_classes
import display_functions

display = display_functions.Display()
display.display_background()


deck = game_classes.Deck()
player1 = game_classes.Player(name="Marcus")
deck.shuffle()
deck.deal_7(player1)
player1currentcards = player1.get_current_cards(deck.get_player_cards())
x = 4
for card in player1currentcards:
    card_image = card.get_image()
    scale = 0.25

    display.display_card(x,575,card_image, scale)
    x += 35



# image = pygame.image.load("assets/Blue_3.png")
# display.display_card(100, 100, image)


display.dont_quit_pygame() # run this at the very end