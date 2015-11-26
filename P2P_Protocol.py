import platform



def createGETMessage(rfcNumber, serverAddress, serverPort):

    os = platform.system() + platform.release()


    getMessage =  'GET' + ' ' + 'RFC' + ' ' + str(rfcNumber) + ' ' + 'P2P-CI/1.0\r\n' + \
                  'Host: '  + str(serverAddress)   + '\r\n' + \
                  'Port: '  + str(serverPort)      + '\r\n' + \
                  'OS: '    + os                   + '\r\n' + '\r\n'
    return (getMessage)


def createNotFoundError():
    print('404 Not Found')

def createBadRequestError():
    print('400 Bad Request')

def createVersionError():
    print('505 P2P-CI Version Not Supported')


def ifExistsRfc(rfc):

    rfcCode, rfcNumber = rfc.strip().split(" ")
    print rfcCode, rfcNumber
    return False
    


def parse_requests(str):

	ret = []	# Parsed Request Command Queue

	# Can get multiple request packets in a message.
	# Split based on P2S end-of-request delimiter

	for req in str.strip().split("\r\n\r\n"):
		# re-init
		cl, hdrs = [], {}

		# clean up string and get lines
		req_lns = req.strip().split("\r\n")	

		# parse the P2S Command line
		cl = req_lns[0].split(" ")

		# parse P2S header lines
		for l in req_lns[1:]:				
			hdr = l.strip().split(" ")
			hdrs[hdr[0][:-1]] = " ".join(hdr[1:])
						# ^-- removes the ":" at the end of each header_name
	
		# add parsed command to the queue
		ret.append( ((cl[0], " ".join(cl[1:-1]), cl[-1]), hdrs) )

	return (ret)


def validate(command, rfc, version, headers):

    if ifExistsRfc(rfc):
        if version == 'P2P-CI/1.0' and command == 'GET':
            return True
        elif version != 'P2P-CI/1.0':
            createVersionError()
            return False
        elif command != 'GET':
            createBadRequestError()
            return False
    else:
        createNotFoundError()
        return False
    
       


