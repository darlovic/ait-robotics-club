#!bin/python

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.connect(('localhost', 5000))

while True:
    
    ch = raw_input("you>>")
    my_socket.sendall(ch)
