import pygame
import game_classes
import display_functions
import time

display = display_functions.Display()
deck = game_classes.Deck()

# setting up game
display.display_background()

display.draw_oppnents_grid_bg()

display.draw_client_player_cards_bg()

display.draw_pickup_cards_pile_bg()
display.draw_placed_cards_pile_bg()

display.display_text(761, 42, "Pick Up", 1)
display.display_text(1002, 44, "Place Card", 1)

for x in range(1, 7):
    display.draw_bg_opponent(x)
    time.sleep(0.1)

deck.shuffle()

Marcus = game_classes.Player("Marcus")
Rachel = game_classes.Player("Rachel")

deck.deal_7(Marcus)
deck.deal_7(Rachel)




#Marcus.display_current_cards(deck, display, 575, 0.05)
Marcus.redraw_player_deck(deck, display)
#Rachel.display_current_cards(deck, display, 100, 0.05)

display.dont_quit_pygame() # place at end of file, for now

