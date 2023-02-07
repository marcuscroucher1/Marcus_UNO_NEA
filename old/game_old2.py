import pygame
from pygame.locals import *

import game_classes

def main():
    deck = game_classes.Deck()
    card = deck.get_deck()[0]
    pygame.init()
    screen = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('UNO!')

  # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    screen.blit(card.get_image(), (100, 100))


    # Event loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                return

        screen.blit(background, (0, 0))
        screen.blit(card.get_image(), (0, 0))
        pygame.display.flip()



if __name__ == '__main__': main()
