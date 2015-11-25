from socket import *
from P2P_Protocol import *
import signal

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
s.sendto(createGETMessage(750, peerAddress, peerPort),(peerAddress, peerPort))
print(s.recv(bufferSize))
s.close()




    

