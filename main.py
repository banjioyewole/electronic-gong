#!/usr/bin/env python
# from socket import *
import os
import socket
from termcolor import colored


def printg(str):
    print(colored(str, "green"))

def printb(str):
    print(colored(str, "blue"))

def network_loop():
    serverPort = 42069
    fabricated_success = "HTTP/1.1 200"
    #create an INET, STREAMing socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    #bind the socket to a public host,
    # and a well-known port
    serversocket.bind(('', serverPort))
    #become a server socket
    serversocket.listen(5)
    printb("is listening")

    while 1:
        #accept connections from outside
        (clientsocket, address) = serversocket.accept()
        printb("did get from")
        printb(address)

        didRecieve = clientsocket.recv(2048)
        print(didRecieve.decode())
        clientsocket.send(fabricated_success.encode())

        stream = os.popen('/usr/bin/mplayer /home/pi/Music/chinese-gong-daniel_simon.wav')
        output = stream.read()
        # output

        #now do something with the clientsocket
        #in this case, we'll pretend this is a threaded server
        # ct = client_thread(clientsocket)
        # ct.run()
        clientsocket.close()


    clientsocket.close()
    serversocket.close()

network_loop()
