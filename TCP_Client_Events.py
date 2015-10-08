##def main():
##
##    rfcNumber = '247'
##    serverAddress = '10.139.50.209'
##    serverPort = '7734'
##    rfcTitle = 'IP project'
##
##    createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle)
##    createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle)
##    createLISTMessage(serverAddress, serverPort)
##
##main()

import socket

def createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle):

    
    addMessage = 'ADD' + ' ' + 'RFC' + ' ' + rfcNumber + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    print(addMessage)
    

def createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle):

    
    lookupMessage = 'LOOKUP' + ' ' + 'RFC' + ' ' +  rfcNumber + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    print(lookupMessage)

     
def createLISTMessage(serverAddress, serverPort):

    
    listMessage = 'LIST ALL' + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n'
    print(listMessage)


rfcNumber = '237'
rfcTitle = 'Day 0: IP Project'
serverAddress = '10.139.58.194'
serverPort = 12000
bufferSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverAddress, serverPort))
s.send(createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
#data = s.recv(BUFFER_SIZE)
s.close()
#print "received data:", data
