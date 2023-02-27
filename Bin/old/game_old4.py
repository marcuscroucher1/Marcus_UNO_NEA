import pygame
import time

import game_classes
import display_functions

display = display_functions.Display()
display.display_background()

def create_player(player_name, yposition):
    player_name = game_classes.Player(name=str(player_name))
    deck.deal_7(player_name)
    currentcards = player_name.get_current_cards(deck.get_player_cards())
    x = 4
    for card in currentcards:
        card_image = card.get_image()
        scale = 0.25

        display.display_card(x,yposition,card_image, scale)
        x += 35

deck = game_classes.Deck()
deck.shuffle()
player1 = game_classes.Player(name="Marcus")


# create_player("Marcus", 575)
# create_player("Rachel", 100)

# deck.deal_7(player1)
# player1currentcards = player1.get_current_cards(deck.get_player_cards())
# x = 4
# for card in player1currentcards:
#     card_image = card.get_image()
#     scale = 0.25
#
#     display.display_card(x,575,card_image, scale)
#     x += 35
#
# player2 = game_classes.Player(name="Rachel")
# deck.deal_7(player2)
# player2currentcards = player2.get_current_cards(deck.get_player_cards())
# x = 4
# for card in player2currentcards:
#     card_image = card.get_image()
#     scale = 0.25
#
#     display.display_card(x,0,card_image, scale)
#     x += 35
#


# image = pygame.image.load("assets/Blue_3.png")
# display.display_card(100, 100, image)


display.dont_quit_pygame() # run this at the very end