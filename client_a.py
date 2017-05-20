#! bin/python

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 5000))

while True:

    message = raw_input("your message: ")
    s.send(message)
    print "waiting reply"
    reply = s.recv(1024)
    print "received", repr(reply)

s.close()
