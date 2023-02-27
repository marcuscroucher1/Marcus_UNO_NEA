# https://youtu.be/8A4dqoGL62E

# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1234))
#
# msg = s.recv(1024)
# print(msg.decode("utf-8"))







# import socket
#
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((socket.gethostname(), 1234))
#
# full_msg = ''
# while True:
#     msg = s.recv(8)
#     if len(msg) <= 0:
#         break
#     full_msg += msg.decode("utf-8")
#
# print(full_msg)




import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1235))

while True:

    full_msg = ''
    new_msg = True

    while True:
        msg = s.recv(16)
        if new_msg:
            print(f"new message length: {msg[:HEADERSIZE]}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False

        full_msg += msg.decode("utf-8")

        if len(full_msg)-HEADERSIZE == msglen:
            print("full msg recieved")
            print(full_msg[HEADERSIZE:])
            new_msg = True
            full_msg = ''

    print(full_msg)

