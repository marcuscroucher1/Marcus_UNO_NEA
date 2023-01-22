class Card:

    def __init(self, colour, number):
        self.__colour = colour
        self.__number = number
        self.__owner = None

    def get_colour(self):
        return self.__colour

    def get_number(self):
        return self.__number

    def assign_owner(self, owner):
        self.__owner = owner

    def display_details(self):
        print(self.__colour + self.__number + self.__owner)

    def __str__(self):
        return self.__colour + str(self.__number) + str(self.__owner)

list_of_cards = []
