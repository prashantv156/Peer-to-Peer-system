import socket
from P2S_Protocol import *
from threading import Thread
import signal
import sys

def send_P2S_request(serverAddress, uploadPort, bufferSize, command, s):
        
    if command == 'LIST':     
       s.send(generate_request('LIST', 0, "ALL", serverAddress, uploadPort))
       serverResponse = s.recv(bufferSize)
       print "<Resp>\n", serverResponse, "</Resp>"

    
    if command == 'ADD':
        clientRfcDictionary = createClientDictionary()
        for key in clientRfcDictionary.keys():

            rfcNumber = key
            rfcTitle = clientRfcDictionary[rfcNumber]
            print  rfcNumber, rfcTitle
            
            s.send(generate_request('ADD', rfcNumber, rfcTitle, serverAddress, uploadPort))
            serverResponse = s.recv(bufferSize)
            print "<Resp>\n", serverResponse, "</Resp>"


    # Just a test-case for now. TODO : Fix it
    if command == 'LOOKUP':
        s.send(generate_request('LOOKUP', 413, "Day 0", serverAddress, uploadPort))
        serverResponse = s.recv(bufferSize)
        print "<Resp>\n", serverResponse, "</Resp>"

        

def clientToServer():

    serverAddress = 'localhost'
    serverPort = 12000
    uploadPort = 12345
    bufferSize = 4096

    #command = raw_input('Enter ADD/LOOKUP/LIST : ')

    #open a TCP Socket, send a request and print the response
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverAddress, serverPort))

    send_P2S_request(serverAddress, uploadPort, bufferSize, "ADD", s)
    send_P2S_request(serverAddress, uploadPort, bufferSize, "LIST", s)
    send_P2S_request(serverAddress, uploadPort, bufferSize, "LOOKUP", s)

    s.send("EOF")
    s.close()
    print "Socket Closed."
 

print 'the client is up and running'
client = Thread(target=clientToServer)
client.start()
