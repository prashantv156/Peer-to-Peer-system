import socket
from C2S_Protocol import *
from threading import Thread
import signal
import sys

def openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, command):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverAddress, serverPort))
        
    if command == 'LIST':     
       s.send(createLISTMessage(serverAddress, serverPort))
       serverResponse = s.recv(bufferSize)
       print "<Resp>", serverResponse, "</Resp>"

    
    if command == 'ADD':
        clientRfcDictionary = createClientDictionary()
        for key in clientRfcDictionary.keys():

            rfcNumber = key
            rfcTitle = clientRfcDictionary[rfcNumber]
            print  rfcNumber, rfcTitle
            s.send(createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
            serverResponse = s.recv(bufferSize)
            print "<Resp>", serverResponse, "</Resp>"


    if command == 'LOOKUP':

        s.send(createLISTMessage(serverAddress, serverPort))
        serverResponse = s.recv(bufferSize)
        print "<Resp>", serverResponse, "</Resp>"
        
           
 
    s.close()
    print "Socket Closed."


def clientToServer():

    serverAddress = 'localhost'
    serverPort = 12000
    bufferSize = 4096

    command = raw_input('Enter ADD/LOOKUP/LIST : ')

    #open a TCP Socket, send a request and print the response
    openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, command)
 

print 'the client is up and running'
client = Thread(target=clientToServer)
client.start()

    

