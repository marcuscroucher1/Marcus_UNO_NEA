import pygame
import game_classes

class Display:
    def __init__(self):
        pass

    def display_card(self):
        pygame.init()
        screen = pygame.display.set_mode((1280, 720))
        image = pygame.image.load("assets/Blue_0.png")
        width = image.get_rect().width
        height = image.get_rect().height
        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((0, 0, 0))


        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            iterate = 1
            iterate2 = 1
            for i in range(200):

                image = pygame.transform.scale(image, (width * iterate2, height * iterate2))

                iterate2 += 0.01

                # screen.blit(background, (0, 0))
                screen.blit(image, (iterate, 100))
                iterate += 1
                pygame.display.update()

                print(iterate)

display = Display()
display.display_card()


#, xCoordinate, yCoordinate, card