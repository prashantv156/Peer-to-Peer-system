def createADDMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    addMessage =  'ADD' + ' ' + 'RFC' + ' ' + str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + \
                  'Host: '  + serverAddress   + '\r\n' + \
                  'Port: '  + str(serverPort) + '\r\n' + \
                  'Title: ' + rfcTitle        + '\r\n' + '\r\n'
    return (addMessage)

def createLOOKUPMessage(rfcNumber, serverAddress, serverPort, rfcTitle):
    lookupMessage = 'LOOKUP' + ' ' + 'RFC' + ' ' +  str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + \
                    'Host: '  +  serverAddress   + '\r\n' + \
                    'Port: '  +  str(serverPort) + '\r\n' + \
                    'Title: ' + rfcTitle        + '\r\n'  + '\r\n'
    return (lookupMessage)
     
def createLISTMessage(serverAddress, serverPort):
    listMessage = 'LIST ALL' + ' ' + 'P2P-CI/1.0\r\n' + \
                  'Host: ' + serverAddress    + '\r\n' + \
                  'Port: ' + str(serverPort)  + '\r\n' + '\r\n'
    return (listMessage)


def createClientDictionary():

    #create initial dictionary of all RFCs with their titles that a client has
    clientRfcDictionary = {}
    clientRfcDictionary[413] = 'Day 0'
    clientRfcDictionary[250] = 'Day 1'
    clientRfcDictionary[758] = 'Day 2'
    clientRfcDictionary[600] = 'Day 3'
    clientRfcDictionary[981] = 'Day 4'

    return (clientRfcDictionary)
