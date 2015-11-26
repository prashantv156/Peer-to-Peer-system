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


#connection handler
def peerThread(message, peerAddr):

        s = socket(AF_INET, SOCK_DGRAM)
        peerAddress = peerAddr[0]
        peerPort = peerAddr[1]
        print 'message received from peer at  ' + str(peerAddress) + '  ' + str(peerPort)
        s.sendto(message, (peerAddress, peerPort))
        s.close()     
        


# P2P process

s = createServerSocket()
print 'peer is ready to receive'

while 1:
        message, peerAddr = s.recvfrom(4096)
        print message
        for (cmd, rfc, ver), headers in parse_requests(message):
                flag, infoMessage = validate(cmd, rfc, ver, headers)
                if flag:
                        t = Thread(target=peerThread, args=(infoMessage, peerAddr,))
                        t.start()
                else:
                        s.sendto(infoMessage, (peerAddr[0], peerAddr[1]))
                         

s.close()
  
