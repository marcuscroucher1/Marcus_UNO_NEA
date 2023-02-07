import game_classes
import display_functions
import game

display = display_functions.Display()
display.display_background()

deck = game_classes.Deck()

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

game = game
game.create_player("Marcus", 575)

display.dont_quit_pygame()