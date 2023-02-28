import socket
from termcolor import colored
#
# socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#
# host = input("IP ni kiriting: ")
#
# def portscan(port):
#     if socket.connect_ex((host, port)):
#         print(colored(" %d udp porti yopiq " % port, 'red'))
#     else:
#         print(colored(" %d udp porti ochiq " % port, 'green'))
#
#
# for port in range(1,101):
#     portscan(port)

# SOCK_STREAM means that it is a TCP socket.
# SOCK_DGRAM means that it is a UDP socket.



socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = input("IP ni kiriting: ")

def portscan(port):
    if socket.connect_ex((host, port)):
        print(colored(" %d tcp porti yopiq " % port, 'red'))
    else:
        print(colored(" %d tcp porti ochiq " % port, 'green'))


for port in range(1,101):
    portscan(port)