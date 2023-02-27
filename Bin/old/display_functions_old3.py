import pygame
import game_classes
import time

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption('UNO!')
    def display_background(self):
        bg_image = pygame.image.load("../../assets/Table_3.png")
        self.screen.blit(bg_image, (0, 0))
        pygame.display.flip()

    def display_card(self, xCoordinate, yCoordinate, cardImage, scale):
        self.__xCoordinate = xCoordinate
        self.__yCoordinate = yCoordinate
        self.__cardImage = cardImage
        self.__scale = scale

        width = cardImage.get_rect().width
        height = cardImage.get_rect().height

        cardImage = pygame.transform.scale(cardImage, (width * scale, height * scale))
        self.screen.blit(cardImage, (xCoordinate, yCoordinate))
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


    def dont_quit_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()



#marcus = game_classes.Player(name="marcus")

#display = Display()

#display.display_background()

#cardtodisplay = marcus.get_current_cards()
#print(cardtodisplay)
#display.display_card(100, 100, )

# display.test()
# display.dont_quit_pygame()