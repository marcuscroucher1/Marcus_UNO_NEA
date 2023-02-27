import pygame
import game_classes
import display_functions
import time

display = display_functions.Display()
deck = game_classes.Deck()

# setting up game
display.display_background()
display.draw_oppnents_grid_bg()
display.display_text(400, 650, "deck to pick up from (normally cant see)")
display.display_text(950, 650, "Placed down cards")
deck.shuffle()

# currentTopCard = deck.get_current_deck_top_card().get_image()
# display.display_current_deck_top_card(currentTopCard)
# time.sleep(0.5)

# creating two players
Marcus = game_classes.Player("Marcus")
Rachel = game_classes.Player("Rachel")

deck.deal_7(Marcus)
deck.deal_7(Rachel)

Marcus.display_current_cards(deck, display, 575, 0.05)
Rachel.display_current_cards(deck, display, 100, 0.05)

currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)

deck.place_first_card()

time.sleep(0.5)

currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)


display.display_background()
display.display_text(400, 650, "deck to pick up from (normally cant see)")
display.display_text(950, 650, "Placed down cards")


currentPlacedCard = deck.get_current_placed_card().get_image()
display.display_currently_placed_cards(currentPlacedCard)

currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)

# time.sleep(0.5)

# time.sleep(1)


######

marcuscard = Marcus.get_current_cards(deck.get_player_cards())[0]
Marcus.place_selected_card(marcuscard, deck)


currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)


Marcus.display_current_cards(deck, display, 575, 0)
Rachel.display_current_cards(deck, display, 100, 0)

currentPlacedCard = deck.get_current_placed_card().get_image()
display.display_currently_placed_cards(currentPlacedCard)

######
display.draw_oppnents_grid_bg()

display.dont_quit_pygame() # place at end of file, for now