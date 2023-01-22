import pygame
import random
from pygame.locals import *

# class Card:
#     colour = None
#     symbol = None
#     image = None
#
#     def __init__(self, colour, symbol):
#         self.colour = colour
#         self.symbol = symbol
#         self.image = pygame.image.load("assets/" + self.colour.name + self.symbol.name + ".png")
#                                                                                                                                                                                                        
# class Deck:
#     cards = None
#     # colours = ["Blue_", "Green_", "Red_", "Yellow_"]
#     # symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]
#     def __init__(self):
#         self.cards = []
#         for colour in colours:
#             for symbol in symbols:
#                 self.cards.append(Card(colour, symbol))
#         print(self.cards)



        # for each in self.colours:
        #     for symbol in self.symbols:
        #         self.currentCard.append(Card)
        # print(self.currentCard)


# Deck()

# def card():
#  pass
# def main():
#     pygame.init()
#     screen = pygame.display.set_mode((1280, 720))
#     pygame.display.set_caption("UNO")
#
#   # Fill background
#     background = pygame.Surface(screen.get_size())
#     background = background.convert()
#     background.fill((250, 250, 250))
#
#     # Display some text
#     font = pygame.font.Font(None, 36)
#     text = font.render("UNO TEST", 1, (10, 10, 10))
#     textpos = text.get_rect()
#     textpos.centerx = background.get_rect().centerx
#     textpos.centery = background.get_rect().centery
#     background.blit(text, textpos)
#
#     # Blit everything to the screen
#     screen.blit(background, (0, 0))
#     pygame.display.flip()
#
#     # Event loop
#     while True:
#         for event in pygame.event.get():
#             if event.type == QUIT:
#                 return
#
#         screen.blit(background, (0, 0))
#         pygame.display.flip()


def generate_deck():
    # will generate the uno deck and assign the card assets to each card
    cards = []
    colours = ["Blue", "Green", "Red", "Yellow"]
    symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]



    for colour in range(len(colours)):
        for symbol in symbols:
            image_filename = None
            image_filename = "assets/" + colours[colour] + "_" + symbol + ".png"
            cards.append(image_filename)
    print(cards)
    random.shuffle(cards)
    print(cards)
    thecard = cards[0]



######
    pygame.init()
    X = 388
    Y = 562
    screen = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('image')
    image = pygame.image.load(thecard).convert()
    screen.blit(image, (0, 0))
    pygame.display.flip()
    status = True
    while (status):
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False
    pygame.quit()

######

generate_deck()
#main()