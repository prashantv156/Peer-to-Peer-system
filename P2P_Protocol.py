import platform
import os
from datetime import *
from P2S_Protocol import *


def createGETMessage(rfcNumber, serverAddress, serverPort):

    os = platform.system() + ' ' +  platform.release()
    getMessage =  'GET' + ' ' + 'RFC' + ' ' + str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + \
                  'Host: '  + str(serverAddress)   + '\r\n' + \
                  'Port: '  + str(serverPort)      + '\r\n' + \
                  'OS: '    + os                   + '\r\n' + '\r\n'
    return (getMessage)

#TODO: generate the message headers 
def generate_peer_resp_body(ver, filename, data):

    osversion = platform.system() + ' ' + platform.release()
    date = datetime.now()
    lastmodified = os.path.getmtime(filename)
    lastmodified = datetime.fromtimestamp(lastmodified)
    contentlength = len(data)

    peer_response = generate_resp_hdr(ver)  

    peer_response += 'Date:' + ' ' + str(date) + '\r\n' + \
                     'OS:'   + ' ' + str(osversion) + '\r\n' + \
                     'Last-Modified:' + ' ' + str(lastmodified) + '\r\n' + \
                     'Content-Length:' + ' ' + str(contentlength) + '\r\n' + \
                     'Content-Type:' + ' ' + 'text/text' + '\r\n' + \
                     'Message-Body:' + ' ' + data + '\r\n'

    peer_response += generate_resp_tail()

    return (peer_response)
    


def createNotFoundError():
    return('404 Not Found')

def createBadRequestError():
    return('400 Bad Request')

def createVersionError():
    return('505 P2P-CI Version Not Supported')


def ifExistsRfc(rfc):

    clientRfcDictionary = createClientDictionary()
    rfcCode, rfcNumber = rfc.strip().split(" ")
    if (int(rfcNumber) in clientRfcDictionary):
        return True
    else:
        print 'requested RFC does not exist'
        return False
    

def validate(command, rfc, version, headers):

    if (ifExistsRfc(rfc)):
        if version == 'P2P-CI/1.0' and command == 'GET':
            flag = True
            status = 'success'
        elif version != 'P2P-CI/1.0':
            flag = False
            status = createVersionError()
        elif command != 'GET':
            flag = False
            status = createBadRequestError()
    else:
        flag = False
        status = createNotFoundError()

    return (flag, status)


       


