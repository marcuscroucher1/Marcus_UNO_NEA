import pygame
import game_classes
import display_functions
import time
import socket

display = display_functions.Display()
display.display_background()
display.draw_oppnents_grid_bg()
display.draw_client_player_cards_bg()
display.draw_pickup_cards_pile_bg()
display.draw_placed_cards_pile_bg()

display.display_text(761, 42, "Pick Up", 1)
display.display_text(1002, 44, "Place Card", 1)

#####

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

full_msg = ''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg.decode("utf-8")

print(full_msg)




display.dont_quit_pygame()