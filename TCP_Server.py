from socket import *
from P2S_Protocol import *


serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

    
# RFC hash-table
rfc_ht = {}

def rfc_ht_insert(k, v):
     # init
     if k not in rfc_ht:
          rfc_ht[k] = []

     # skip if duplicate
     if v in rfc_ht[k]:
          return

     # insert
     rfc_ht[k].append(v)



print ('The server is ready to receive')
     
connectionSocket, addr = serverSocket.accept()
     
while True:

     message = connectionSocket.recv(4096)

     # Parse P2S requests from the TCP buffer
     for (cmd, rfc, ver), headers in parse_requests(message):

          if cmd == 'ADD':
               print "ADD - ", rfc

               # Add entry onto the Hash Table
               rfc_ht_insert( rfc, (addr[0], int(headers['Port'])) )

               # Send Response back to Client (ACK)
               connectionSocket.send( generate_response(cmd, rfc, ver, headers) )

          if cmd == 'LOOKUP':
               print "LOOKUP - "

          if cmd == 'LIST':
               print "LIST - ALL"
               print rfc_ht[rfc_ht.keys()[0]]

     #break;	# DEBUG

connectionSocket.close()
serverSocket.close()


   
