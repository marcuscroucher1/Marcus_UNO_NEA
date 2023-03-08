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



z=''
import socket

s = socket.socket()
port = 3125
s.connect((socket.gethostname(), port))
while z != 'exit':
    z = input('card')
    s.sendall(z.encode())


s.close()