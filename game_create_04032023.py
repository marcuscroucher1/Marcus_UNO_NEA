import pygame
import game_classes
import display_functions
import time

display = display_functions.Display()
deck = game_classes.Deck()



# while True:
#
#     # taken from https://www.geeksforgeeks.org/how-to-create-buttons-in-a-game-using-pygame/
#
#     for event in pygame.event.get(): # event is user defined remember!
#
#         if event.type == pygame.QUIT:
#             pygame.quit()
#
#         if event.type == pygame.MOUSEBUTTONDOWN:
#             if 590 <= mouse[0] <= 670 and 315 <= mouse[1] <= 345:
#                 print("the button works!")




# setting up game
display.display_background()

display.draw_oppnents_grid_bg()

display.draw_client_player_cards_bg()

display.draw_client_name_bg()

display.draw_UNO_Button()

display.draw_pickup_cards_pile_bg()
display.draw_placed_cards_pile_bg()


display.display_text(761, 42, "Pick Up", 1)
display.display_text(1002, 44, "Place Card", 1)

# for x in range(1, 7):
#     display.draw_bg_opponent(x)
#     time.sleep(0.1)

deck.shuffle()

Grace = game_classes.Player("Grace", 1)
Marcus = game_classes.Player("Marcus", 2)
Joe = game_classes.Player("Joe", 3)
Daisy = game_classes.Player("Daisy", 4)
Molly = game_classes.Player("Molly", 5)
Player6 = game_classes.Player("Player6", 6)
Dylan = game_classes.Player("Dylan", 0)


deck.deal_7(Grace)
deck.deal_7(Marcus)
deck.deal_7(Joe)
deck.deal_7(Daisy)
deck.deal_7(Molly)
deck.deal_7(Player6)
deck.deal_7(Dylan)


#Marcus.display_current_cards(deck, display, 575, 0.05)
Grace.redraw_player_deck(deck, display)
Marcus.redraw_player_deck(deck, display)
Joe.redraw_player_deck(deck, display)
Daisy.redraw_player_deck(deck, display)
Molly.redraw_player_deck(deck, display)
Player6.redraw_player_deck(deck, display)
#Rachel.display_current_cards(deck, display, 100, 0.05)


Dylan.redraw_client_name(display)
Dylan.redraw_client_cards(deck, display)


display.create_button_zone()


deck.place_first_card()


# YOU ARE IN THE PROCESS OF MAKING THE BOTTOM CARDS WORK, THEN CREATING CLIENTS THAT CAN MOVE THE CARDS AROUND USING
# BUTTONS - CHECK THE WEBSITE ON PYGAME BUTTONS
# SOCKETS - ASK JOE?


currentPlacedCard = deck.get_current_placed_card().get_image()
display.display_currently_placed_cards(currentPlacedCard)

currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)


display.input_checks()
#display.dont_quit_pygame() # place at end of file, for now

