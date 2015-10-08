import socket

def openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, clientRfcDictionary):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((serverAddress, serverPort))
    rfcCount = len(clientRfcDictionary.keys())

    # if client has no rfc's ask server to list all rfcs
    if rfcCount == 0:     
       s.send(createLISTMessage(serverAddress, serverPort))

    # if client has RFC's then add to the server
    if rfcCount > 0:

       for key in clientRfcDictionary.keys():
           rfcNumber = key
           rfcTitle = clientRfcDictionary[rfcNumber]
           s.send(createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle))
       
##    serverResponse = s.recv(bufferSize)
##    print(serverResponse)
    s.close()


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


serverAddress = 'localhost'
serverPort = 12000
bufferSize = 4096

#create initial dictionary of all RFCs with their titles that a client has
clientRfcDictionary = {}
clientRfcDictionary[413] = 'Day 0 - IP Project'
clientRfcDictionary[250] = 'Day 1 - IP Project'
clientRfcDictionary[758] = 'Day 2 - IP Project'

#open a TCP Socket, send a request and print the response
openTCPSocketAndGetResponse(serverAddress, serverPort, bufferSize, clientRfcDictionary)


