import socket

def createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    addMessage = 'ADD' + ' ' + 'RFC' + ' ' + rfcNumber + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    return (addMessage)
    

def createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    lookupMessage = 'LOOKUP' + ' ' + 'RFC' + ' ' +  rfcNumber + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    return (lookupMessage)

     
def createLISTMessage(serverAddress, serverPort):
    listMessage = 'LIST ALL' + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + serverPort + '\r\n'
    return (listMessage)


rfcNumber = '237'
rfcTitle = 'Day 0: IP Project'
serverAddress = 'localhost'
serverPort = 12000
bufferSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverAddress, serverPort))
s.send(createADDMessage(rfcNumber, serverAddress, str(serverPort), rfcTitle))
s.send(createLOOKUPMessage(rfcNumber, serverAddress, str(serverPort), rfcTitle))
s.send(createLISTMessage(serverAddress, str(serverPort)))
#data = s.recv(BUFFER_SIZE)
s.close()
#print "received data:", data
