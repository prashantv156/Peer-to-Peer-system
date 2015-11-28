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





def generate_resp_hdr(ver):
##	return (ver + ' ' + '200' + ' ' + 'OK' + '\r\n'	+ '\r\n')
        return (ver + ' ' + '200' + ' ' + 'OK' + '\r\n')

def generate_resp_body(rfc, title, client_ip, client_up_port):
	return (rfc + ' ' + title + ' ' + client_ip + ' ' +  str(client_up_port) + '\r\n')

def generate_resp_tail():
	return ('\r\n')



def generate_request(cmd, rfcNum, Title, serverAddress, serverPort):

	if cmd == 'LIST':
		rfc_field = 'ALL'
		rfc_header = ''
	else:
		rfc_field = 'RFC' + ' ' + str(rfcNum)
		rfc_header = 'Title: ' + Title + '\r\n'

	request = cmd + ' ' + rfc_field + ' ' + 'P2P-CI/1.0\r\n' + \
              'Host: '  + serverAddress   + '\r\n' + \
              'Port: '  + str(serverPort) + '\r\n' + \
              rfc_header + '\r\n'

	return (request)



#	--------------------- DEPRECATED  ------------------------------

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

#  ----------------------------------------------------------------------

def createClientDictionary():

    #create initial dictionary of all RFCs with their titles that a client has
    clientRfcDictionary = {}
    clientRfcDictionary[1918] = 'rfc1918'
    clientRfcDictionary[250] = 'Day 1'
    clientRfcDictionary[758] = 'Day 2'
    clientRfcDictionary[600] = 'Day 3'
    clientRfcDictionary[981] = 'Day 4'

    return (clientRfcDictionary)
