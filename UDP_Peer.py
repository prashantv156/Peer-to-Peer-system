from socket import *
from threading import Thread
from P2P_Protocol import *
import signal
import sys


# Signal Handler for graceful connection termination
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        # TODO - cleanup sockets over here
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


def createServerSocket():

        welcomePort = 11000
        s = socket(AF_INET, SOCK_DGRAM)
        s.bind(('', welcomePort))
        return s

def parseRequest(data):

        return true  


#connection handler
def peerThread(message, peerAddr):

        s = socket(AF_INET, SOCK_DGRAM)
        peerAddress = peerAddr[0]
        peerPort = peerAddr[1]
        s.sendto(message, (peerAddress, peerPort))
        s.close()     
        

# P2P process

s = createServerSocket()

while 1:
        message, peerAddr = s.recvfrom(4096)
        for (cmd, rfc, ver), headers in parse_requests(message):
                print headers
                print (cmd, rfc, ver)
                if rfc == 'RFC 750':
                        t = Thread(target=peerThread, args=(createNotFoundError(), peerAddr,))
                        t.start()
                          

s.close()
  
