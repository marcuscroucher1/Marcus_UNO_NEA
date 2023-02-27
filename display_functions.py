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
        oval_1 = pygame.image.load("assets/Oval_1.png")
        self.screen.blit(oval_1, (14, 21))
        pygame.display.flip()

    def draw_client_player_cards_bg(self):
        oval_1 = pygame.image.load("assets/Oval_2.png")
        self.screen.blit(oval_1, (273, 466))
        pygame.display.flip()

    def draw_pickup_cards_pile_bg(self):
        oval_1 = pygame.image.load("assets/Oval_3.png")
        self.screen.blit(oval_1, (717, 20))
        pygame.display.flip()

    def draw_placed_cards_pile_bg(self):
        oval_1 = pygame.image.load("assets/Oval_3.png")
        self.screen.blit(oval_1, (998, 20))
        pygame.display.flip()

    ##

    def draw_bg_opponent(self, opponentNumber):
        if opponentNumber == 1:
            x = 41
            y = 46
        elif opponentNumber == 2:
            x = 260
            y = 46
        elif opponentNumber == 3:
            x = 478
            y = 46
        elif opponentNumber == 4:
            x = 41
            y = 247
        elif opponentNumber == 5:
            x = 260
            y = 247
        elif opponentNumber == 6:
            x = 478
            y = 247
        else:
            x = 0
            y = 0
        oval_4 = pygame.image.load("assets/Oval_4.png")
        self.screen.blit(oval_4, (x, y))
        pygame.display.flip()


    ###

    def card_row_height(self):
        # fill this out later for making a ui that can adjust itself for more players
        pass

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
        self.screen.blit(currentTopCard, (450, 75))
        pygame.display.flip()

    def display_current_deck_bottom_card(self, currentBottomCard):
        self.screen.blit(currentBottomCard, (850, 75))
        pygame.display.flip()

    def display_currently_placed_cards(self, currentPlacedCard):
        self.screen.blit(currentPlacedCard, (850, 75))
        pygame.display.flip()


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