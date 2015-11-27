from socket import *
from threading import Thread
from P2P_Protocol import *
import signal
import sys
from rdt import *


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
def peerThread(rfc, ver, headers, peerAddr):

        s = socket(AF_INET, SOCK_DGRAM)
        peerAddress = peerAddr[0]
        peerPort = peerAddr[1]
        print 'message received from peer_client at  ' + str(peerAddress) + '  ' + str(peerPort)
        #TODO: generate the response for a GET request and attach the RFC file to the response
        rfcCode, rfcNumber = rfc.strip().split(' ')
        filename = "haha.txt"

        try:
                with open(filename, 'rb') as f:
                        data = f.read(5*MSS)
                        while data:
                                if data:
                                        #s.sendto(data,(peerAddress, peerPort))
                                        rdt_send(s, data,(peerAddress, peerPort))
                                        print 'sending....'
                                        data = f.read(5*MSS)
                                else:
                                        break
                        

        except:
                sys.exit("Failed to open file")

        print 'File Sent'
        s.close()

        
               


# P2P process
s = createServerSocket()
print 'peer_server is ready to receive'

while True:
        message, peerAddr = s.recvfrom(4096)
        print message
        for (cmd, rfc, ver), headers in parse_requests(message):
                flag, infoMessage = validate(cmd, rfc, ver, headers)
                if flag:
                        t = Thread(target=peerThread, args=(rfc, ver, headers, peerAddr,))
                        t.start()
                else:
                        s.sendto(infoMessage, (peerAddr[0], peerAddr[1]))
                         

s.close()
  
