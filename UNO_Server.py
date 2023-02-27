import pygame
import game_classes
import display_functions
import time
import socket

ip = socket.gethostname()
port = 2468

class NetworkingFunctions:
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.__ip, self.__port))

    def send_data(self, client, data):
        pass

    def recieve_data(self):


deck = game_classes.Deck()

#####

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)


while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    clientsocket.send(bytes("Welcome to the server!", "utf-8"))
    clientsocket.close()

#####