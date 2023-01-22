import pygame
import random
class Card:
    def __init__(self, card_data, filename):
        self.owner = card_data[0]
        self.colour = card_data[1]
        self.symbol = card_data[2]
        self.image = card_data[3]

class Deck:
    def __init__(self):
        # will generate the uno deck and assign the card assets to each card

        filename_colours = ["Blue", "Green", "Red", "Yellow"]
        data_colours = ["b", "g", "r", "y"]
        symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "Draw", "Reverse", "Skip"]

        rows, cols = (len(4), (len(symbols)))
        cards = [[0]*cols]*rows

        for colour in range(len(filename_colours)):
            for symbol in symbols:
                image_filename = None
                image_filename = "assets/" + filename_colours[colour] + "_" + symbol + ".png"
                #cards[0].append(data_colours)
                #cards[colour][3].append(image_filename) # list of all cards has been created, named with filename of image
        #cards.append("assets/" + "Wild.png")
        print(cards)



Deck()
#main()