import pygame
import time
import game_classes
import display_functions




display = display_functions.Display()


# display.display_text(500, 500, "hello")


display.display_background()


deck = game_classes.Deck()
deck.shuffle()


currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)

time.sleep(1)



def create_player(player_name, yposition):
    player_name = game_classes.Player(name=str(player_name))
    deck.deal_7(player_name)
    currentcards = player_name.get_current_cards(deck.get_player_cards())
    x = 4
    for card in currentcards:
        time.sleep(0.05)
        card_image = card.get_image()
        scale = 0.25

        display.display_card(x,yposition,card_image, scale)
        x += 35

Marcus = create_player("Marcus", 575)
Rachel = create_player("Rachel", 100)



currentTopCard = deck.get_current_deck_top_card().get_image()
display.display_current_deck_top_card(currentTopCard)

currentBottomCard = deck.get_current_deck_bottom_card().get_image()
display.display_current_deck_bottom_card(currentBottomCard)


display.display_text(400, 650, "deck to pick up from (normally cant see)")
display.display_text(950, 650, "Placed down cards")

time.sleep(1)

######







######


#events.GameTurn(player="Marcus", card=)



display.dont_quit_pygame() # place at end of file, for now