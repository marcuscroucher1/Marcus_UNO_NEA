import pygame
import pygame.freetype
import game_classes
import time
import sys

class Display:
    def __init__(self):

        self.__screenHeight = 720
        self.__screenWidth = 1280

        self.__CardsHeight = self.__screenHeight # only to get screen height initially

        pygame.init()
        self.screen = pygame.display.set_mode((self.__screenWidth, self.__screenHeight))
        pygame.display.set_caption('UNO!')

        self.__gameFontSmall = pygame.freetype.Font("assets/Ubuntu/Ubuntu-Regular.ttf", 24)
        self.__gameFontMedium = pygame.freetype.Font("assets/Ubuntu/Ubuntu-Regular.ttf", 40)
        self.__gameFontLarge = pygame.freetype.Font("assets/Ubuntu/Ubuntu-Regular.ttf", 56)

        # keepAlive = True
        #
        # while keepAlive:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             keepAlive = False
        # pygame.quit()

        # pygame.font.init()  # you have to call this at the start,
        # # if you want to use this module.

    def display_background(self):
        bg_image = pygame.image.load("assets/Table_1.png")
        self.screen.blit(bg_image, (0, 0))
        pygame.display.flip()


    def draw_oppnents_grid_bg(self):
        oval = pygame.image.load("assets/Oval_1.png")
        self.screen.blit(oval, (14, 21))
        pygame.display.flip()

    def draw_client_player_cards_bg(self):
        oval = pygame.image.load("assets/Oval_2.png")
        self.screen.blit(oval, (273, 466))
        pygame.display.flip()

    def draw_pickup_cards_pile_bg(self):
        oval = pygame.image.load("assets/Oval_3.png")
        self.screen.blit(oval, (717, 20))
        pygame.display.flip()

    def draw_placed_cards_pile_bg(self):
        oval = pygame.image.load("assets/Oval_3.png")
        self.screen.blit(oval, (998, 20))
        pygame.display.flip()

    def draw_client_name_bg(self):
        oval = pygame.image.load("assets/Oval_6.png")
        self.screen.blit(oval, (19, 588))
        pygame.display.flip()

    def draw_UNO_Button(self):
        oval = pygame.image.load("assets/Oval_7.png")
        self.screen.blit(oval, (96, 484))

        self.display_text(120, 508, "UNO!", 2)

        pygame.display.flip()


    ##
    def get_coordinate_set(self, opponentNumber):
        if opponentNumber == 1:
            PlayerSquare_x = 41
            PlayerSquare_y = 46

            card_x = 67
            card_y = 115
        elif opponentNumber == 2:
            PlayerSquare_x = 260
            PlayerSquare_y = 46

            card_x = 285
            card_y = 115
        elif opponentNumber == 3:
            PlayerSquare_x = 478
            PlayerSquare_y = 46

            card_x = 503
            card_y = 115
        elif opponentNumber == 4:
            PlayerSquare_x = 41
            PlayerSquare_y = 247

            card_x = 67
            card_y = 316
        elif opponentNumber == 5:
            PlayerSquare_x = 260
            PlayerSquare_y = 247

            card_x = 285
            card_y = 316
        elif opponentNumber == 6:
            PlayerSquare_x = 478
            PlayerSquare_y = 247

            card_x = 503
            card_y = 316
        else:
            PlayerSquare_x = 0
            PlayerSquare_y = 0

            card_x = 0
            card_y = 0

        return PlayerSquare_x, PlayerSquare_y, card_x, card_y

    def draw_bg_opponent(self, PlayerSquare_x, PlayerSquare_y):

        oval_4 = pygame.image.load("assets/Oval_4.png")
        self.screen.blit(oval_4, (PlayerSquare_x, PlayerSquare_y))
        pygame.display.flip()


    ###

    # def card_row_height(self):
    #     # fill this out later for making a ui that can adjust itself for more players
    #     pass

    def display_card(self, xCoordinate, yCoordinate, cardImage, scale):

        width = cardImage.get_rect().width
        height = cardImage.get_rect().height

        cardImage = pygame.transform.scale(cardImage, (width * scale, height * scale))
        self.screen.blit(cardImage, (xCoordinate, yCoordinate))
        pygame.display.flip()


    ###


    ###

    def display_text(self, xCoordinate, yCoordinate, text, size):
        if size == 0:
            textToDisplay, rect = self.__gameFontSmall.render(text, (0, 0, 0))
            self.screen.blit(textToDisplay, (xCoordinate, yCoordinate))
        elif size == 1:
            textToDisplay, rect = self.__gameFontMedium.render(text, (0, 0, 0))
            self.screen.blit(textToDisplay, (xCoordinate, yCoordinate))
        elif size == 2:
            textToDisplay, rect = self.__gameFontLarge.render(text, (0, 0, 0))
            self.screen.blit(textToDisplay, (xCoordinate, yCoordinate))
        # my_font = pygame.font.SysFont('Comic Sans MS', int(size))
        # textToDisplay = my_font.render("Hello World", False, (0, 0, 0))
        # self.screen.blit(textToDisplay, (xCoordinate, yCoordinate))
        pygame.display.flip()

    # def display_player_cards(self, player):
    #     self.__player = player
    #     for card in game_classes.Deck.get_player_cards():
    #         pass

    # def display_card2(self, xCoordinate, yCoordinate, cardId):
    #
    #     testimage = pygame.image.load("assets/Blue_7.png")
    #     self.screen.blit(testimage, (100, 100))
    #     time.sleep(1)
    #     pygame.display.flip()

    def display_current_deck_top_card(self, currentTopCard):
        self.display_card(755, 129, currentTopCard, 0.55)

    def display_current_deck_bottom_card(self, currentBottomCard):
        self.display_card(850, 75, currentBottomCard, 0.55)

    def display_currently_placed_cards(self, currentPlacedCard):
        self.display_card(1024, 111, currentPlacedCard, 0.55)

        # self.screen.blit(currentPlacedCard, (1024, 111))
        # pygame.display.flip()


    # def display_current_player_cards(self, player_name, yposition, deck, display):
    #     currentcards = player_name.get_current_cards(deck.get_player_cards())
    #     x = 4
    #     for card in currentcards:
    #         time.sleep(0.05)
    #         card_image = card.get_image()
    #         scale = 0.25
    #
    #         display.display_card(x, yposition, card_image, scale)
    #         x += 35


    def dont_quit_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



#marcus = game_classes.Player(name="marcus")

# display = Display()
#
# display.display_background()
# display.display_face_up_deck()

#cardtodisplay = marcus.get_current_cards()
#print(cardtodisplay)
#display.display_card(100, 100, )

# display.test()
# display.dont_quit_pygame()