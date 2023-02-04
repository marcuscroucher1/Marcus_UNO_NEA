import pygame
import game_classes
import time

class Display:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1280, 720))
        bg_image = pygame.image.load("assets/Table_3.png")
        pygame.display.set_caption('UNO!')

        background = pygame.Surface(self.screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        self.screen.blit(background, (0, 0))
        self.screen.blit(bg_image, (0, 0))
        pygame.display.flip()
            # self.screen.blit(background, (0, 0))
            # self.screen.blit(bg_image, (0, 0))
            # pygame.display.flip()

    def display_card(self, xCoordinate, yCoordinate, cardId):
        self.__xCoordinate = xCoordinate
        self.__yCoordinate = yCoordinate
        self.__cardId = cardId + 1

        self.screen.blit(cardId)

    # def display_player_cards(self, player):
    #     self.__player = player
    #     for card in game_classes.Deck.get_player_cards():
    #         pass

    def test(self):
        testimage = pygame.image.load("assets/Blue_7.png")
        self.screen.blit(testimage, (100, 100))
        time.sleep(1)
        pygame.display.flip()

    def dont_quit_pygame(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

display = Display()

display.test()
display.dont_quit_pygame()