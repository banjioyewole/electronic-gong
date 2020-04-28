#!/usr/bin/env python
from termcolor import colored
import socket
from http.server import BaseHTTPRequestHandler,HTTPServer
from subprocess import Popen
import time



def printg(str):
    print(colored(str, "green"))

def printb(str):
    print(colored(str, "blue"))

p = None


class ArbitrarySoundHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        global p
        
        if p is not None:
            p.terminate()

        if self.path == '/chunli':
            p = Popen(['/usr/bin/mplayer', '/home/pi/Music/chun_li_gong.mp3']) # something long running

        if self.path == '/':
            p = Popen(['/usr/bin/mplayer', '/home/pi/Music/chinese-gong-daniel_simon.wav']) # something long running
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("E-Gong'd".encode())
        print("did call")
        # time.sleep(3)
        # p.terminate()
        return


if __name__ == "__main__":

    PORT_NUMBER = 42069

    #This class will handles any incoming request from
    #the browser
    try:
    	#Create a web server and define the handler to manage the
    	#incoming request
    	server = HTTPServer(('', PORT_NUMBER), ArbitrarySoundHandler)
    	print('Started httpserver on port ' , PORT_NUMBER)

    	#Wait forever for incoming htto requests
    	server.serve_forever()

    except KeyboardInterrupt:
    	print('^C received, shutting down the web server')
    	server.socket.close()
