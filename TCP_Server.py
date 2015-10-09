from socket import *
from P2S_Protocol import *

serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

rfc_lookup_ht = {}

def rfc_lookup_insert(k, v):
	print k, v, "key, val"
	rfc_lookup_ht[k] = v
	# TODO - handle duplicates


print ('The server is ready to receive')
while 1:
     connectionSocket, addr = serverSocket.accept()

     # Parse P2S requests from the TCP buffer
     for cmd, headers in parse_requests(connectionSocket.recv(1024)):
          #print cmd, headers

          if cmd[P2S_CMD] == 'ADD':
               rfc_lookup_insert( cmd[ADD_RFC_NUM], (addr[0], int(headers['Port'])) )

          #P2S_cmd_handler[cmd[0]]()

     print rfc_lookup_ht
     break;	# DEBUG

connectionSocket.close()
serverSocket.close()