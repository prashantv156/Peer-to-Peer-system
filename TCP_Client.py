import socket
from C2S_Protocol import *

def openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, clientRfcDictionary):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverAddress, serverPort))
    rfcCount = len(clientRfcDictionary.keys())

    # if client has no rfc's ask server to list all rfcs
    if rfcCount == 0:     
       s.send(createLISTMessage(serverAddress, serverPort))
       serverResponse = s.recv(bufferSize)
       print serverResponse

     
    # if client has RFC's then add to the server
    
    if rfcCount > 0:
       
       for key in clientRfcDictionary.keys():
           rfcNumber = key
           rfcTitle = clientRfcDictionary[rfcNumber]
           print  rfcNumber, rfcTitle
           s.send(createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
           serverResponse = s.recv(bufferSize)
           print "<Resp>", serverResponse, "</Resp>"
           
 
    s.close()
    print "Socket Closed."


serverAddress = 'localhost'
serverPort = 12000
bufferSize = 4096
clientRfcDictionary = createClientDictionary()
    
#open a TCP Socket, send a request and print the response
openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, clientRfcDictionary)




