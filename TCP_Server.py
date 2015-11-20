from socket import *
from P2S_Protocol import *
from threading import Thread
import signal
import sys

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

# Signal Handler for graceful connection termination
def signal_handler(signal, frame):
        print('Got SIGINT, terminating connection')
        serverSocket.close()
        sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


# Linked Lists
peer_list = []
rfc_index = []

# get upload_port from peer_list for a given address
def get_upload_port(addr):
     upload_port = -1

     for (peer_addr, uport) in peer_list:
          if peer_addr == addr:
               upload_port = uport
               break
     
     if upload_port == -1:
          print "Faiiled to find Address in peer-list"

     return upload_port

def find_rfc(rfc_num, rfc_title):
     for n, t, addr in rfc_index:
          if n == rfc_num:
               if t == rfc_title:
                    return (addr, get_upload_port(addr))
               print "Number match. Title no match!"


# Connection Handler
def threadFunc(connectionSocket, addr):
     while True:
          message = connectionSocket.recv(4096)     

          # TODO - figure out how to detect remote socket close
          if message == "EOF":
               break

          if message == "":
               continue

          # Parse P2S requests from the TCP buffer
          for (cmd, rfc, ver), headers in parse_requests(message):

               if cmd == 'ADD':
                    print "ADD - ", rfc

                    # Discover peer on ADD (since thats when we know Upload port)
                    entry = (addr[0], int(headers['Port']))
                    if entry not in peer_list:
                         peer_list.insert(0, entry)

                    # update the RFC-Index
                    entry = (int(rfc[4:]), headers['Title'], addr[0])
                    if entry not in rfc_index:
                         rfc_index.insert(0, entry)

                    # Generate and Send Response back to Client (ACK)
                    resp =  generate_resp_hdr(ver)
                    resp += generate_resp_body(rfc, headers['Title'], headers['Host'], headers['Port'])
                    resp += generate_resp_tail()

                    connectionSocket.send(resp)


               if cmd == 'LOOKUP':
                    print "LOOKUP - ", rfc

                    peer_addr, up_port = find_rfc(int(rfc[4:]), headers['Title'])

                    # Generate and Send Response back to Client
                    resp =  generate_resp_hdr(ver)
                    resp += generate_resp_body(rfc, headers['Title'], peer_addr, up_port)
                    resp += generate_resp_tail()

                    connectionSocket.send(resp)


               if cmd == 'LIST':
                    print "LIST - ALL"

                    # Generate and Send Response back to Client
                    resp =  generate_resp_hdr(ver)
                    for (rfc_num, rfc_title, ip) in rfc_index:
                         resp += generate_resp_body("RFC " + str(rfc_num), rfc_title, ip, get_upload_port(ip))
                    resp += generate_resp_tail()

                    connectionSocket.send(resp)

     print addr, " connection closed!"


# Server
print ('The server is ready to receive')
while True:
     connectionSocket, addr = serverSocket.accept()

     t = Thread(target=threadFunc, args=(connectionSocket, addr,))
     t.daemon = True
     t.start()

# Cleanup
connectionSocket.close()
serverSocket.close()
