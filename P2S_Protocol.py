def parse_requests(str):

	cmd, hdrs = "", {}
	ret = []	# Parsed Request Command Queue

	# Can get multiple request packets in a message.
	# Split based on P2S end-of-request delimiter

	for req in str.strip().split("\r\n\r\n"):
		# re-init
		cmd, hdrs = "", {}

		# clean up string and get lines
		req_lns = req.strip().split("\r\n")	

		# parse the P2S Command line
		cmd = req_lns[0].split(" ")			

		# parse P2S header lines
		for l in req_lns[1:]:				
			hdr = l.strip().split(" ")
			hdrs[hdr[0][:-1]] = " ".join(hdr[1:])
						# ^-- removes the ":" at the end of each header_name
	
		# add parsed command to the queue
		ret.append((cmd, hdrs))

	return (ret)




P2S_CMD = 0
ADD_RFC_NUM = 2
#P2S_VER = 3		# 2 in case of list_all

# Command Handlers for P2P 1.0 
def p2s_1_ADD():
	print "do ADD"

def p2s_1_LOOKUP():
	print "do LOOKUP"

def p2s_1_LIST():
	print "do LIST"

P2S_cmd_handler = {
	'ADD': p2s_1_ADD,
	'LOOKUP': p2s_1_LOOKUP,
	'LIST': p2s_1_LIST
}