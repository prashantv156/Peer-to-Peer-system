import socket

def createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    addMessage = 'ADD' + ' ' + 'RFC' + ' ' + str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + str(serverPort) + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    return (addMessage)
    

def createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    lookupMessage = 'LOOKUP' + ' ' + 'RFC' + ' ' +  str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + str(serverPort) + '\r\n' + 'Title: ' + rfcTitle + '\r\n'
    return (lookupMessage)

     
def createLISTMessage(serverAddress, serverPort):
    listMessage = 'LIST ALL' + ' ' + 'P2P-CI/1.0\r\n' + 'Host: ' + serverAddress + '\r\n' + 'Port: ' + str(serverPort) + '\r\n'
    return (listMessage)

def checkServerResponse():
    pass

   
rfcNumber = 237
rfcTitle = 'Day 0: IP Project'
serverAddress = 'localhost'
serverPort = 12000
bufferSize = 4096

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((serverAddress, serverPort))
s.send(createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
s.send(createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
s.send(createLISTMessage(serverAddress, serverPort))
#serverResponse = s.recv(bufferSize)
#serverStatus = checkServerResponse(serverResponse)
#print(serverResponse)
s.close()
#print "received data:", data
