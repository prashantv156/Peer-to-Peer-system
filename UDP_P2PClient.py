from socket import *
from P2P_Protocol import *
import signal
import sys

# Signal Handler for graceful connection termination
def signal_handler(signal, frame):
        print('You pressed Ctrl+C!')
        # TODO - cleanup sockets over here
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)


peerAddress = 'localhost'
peerPort = 11000
bufferSize = 4096
s = socket(AF_INET,SOCK_DGRAM)
s.sendto(createGETMessage(250, peerAddress, peerPort),(peerAddress, peerPort))
print('\r\n' + s.recv(bufferSize))
s.close()

    

