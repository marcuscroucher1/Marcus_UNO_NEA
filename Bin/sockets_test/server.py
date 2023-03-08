# https://youtu.be/8A4dqoGL62E

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)
#
#
# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))



# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind((socket.gethostname(), 1234))
# s.listen(5)
#
#
# while True:
#     clientsocket, address = s.accept()
#     print(f"Connection from {address} has been established!")
#     clientsocket.send(bytes("Welcome to the server!", "utf-8"))
#     clientsocket.close()



import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 3125
s.bind((socket.gethostname(), port))
print ('Socket binded to port 3125')
s.listen(3)
print ('socket is listening')
bob=''
c, addr = s.accept()
print('Got connection from ', addr)
while bob !='exit':
    bob = (c.recv(1024)).decode('utf-8')
    print (bob)
c.close()


