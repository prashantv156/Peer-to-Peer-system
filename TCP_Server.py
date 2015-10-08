from socket import *


def parse_request(str):
	cmd = ""
	headers = {}

	req_arr = str.strip().split("\n")	# clean up string and get lines

	cmd = req_arr[0].split(" ")			# parse the Command

	for l in req_arr[1:]:				# parse headers
		hdr = l.strip().split(": ")
		headers[hdr[0]] = hdr[1]

	print cmd
	print headers



serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)

print ('The server is ready to receive')
while 1:
     connectionSocket, addr = serverSocket.accept()
     req = connectionSocket.recv(1024)
     parse_request(req)
     break;	# DEBUG

connectionSocket.close()
serverSocket.close()