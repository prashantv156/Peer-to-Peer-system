from socket import *
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


peerAddress = 'localhost'
peerPort = 11000
s = socket(AF_INET,SOCK_DGRAM)
s.sendto(createGETMessage(1918, peerAddress, peerPort),(peerAddress, peerPort))
filename = "rfc1918copy.pdf"
try:
        with open(filename, 'wb') as f:
                #data, addr = s.recvfrom(bufferSize)
                p2p_response, addr = rdt_recv(s)
                print (p2p_response)
                while p2p_response:
                        for (cmd, rfc, ver), headers in parse_requests(p2p_response):
                                data = headers['Message-Body']
                                f.write(data)
                        s.settimeout(2)
                        #data, addr = s.recvfrom(bufferSize)
                        p2p_response, addr = rdt_recv(s)
                        print (p2p_response)
except timeout:
        f.close()
        s.close()
        print "File Downloaded" 

    

