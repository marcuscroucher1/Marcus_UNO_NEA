import pygame
import game_classes

class Display:
    def __init__(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        bg_image = pygame.image.load("assets/Table_3.png")
        pygame.display.set_caption('UNO!')

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((250, 250, 250))

        screen.blit(background, (0, 0))
        screen.blit(bg_image, (0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            screen.blit(background, (0, 0))
            screen.blit(bg_image, (0, 0))
            pygame.display.flip()

    def display_card(self, xCoordinate, yCoordinate, cardId):
        self.__xCoordinate = xCoordinate
        self.__yCoordinate = yCoordinate
        self.__cardId = cardId + 1

        screen.blit(cardId)

    def display_player_cards(self, player):
        self.__player = player
        for each card in game_classes.Deck.get_player_cards()

Display()