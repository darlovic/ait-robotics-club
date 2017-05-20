#! bin/python 

from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('localhost', 5000))
s.listen(1)
conn , addr = s.accept()
print "connected by", addr
while True: 
    data = conn.recv(1024)
    print "received" , repr(data)
    reply = raw_input("reply: ")
    conn.sendall(reply)
