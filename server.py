#! bin/puthon

import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

my_socket.bind(('localhost', 5000))

my_socket.listen(1)

#waiting for connection

while True:
    print "waiting for connection"
    client, address = my_socket.accept()

#we have a connection 
    print "connection from", address
    while True:
        data = client.recv(5)
        print data
        client.sendall("Data recieved")
