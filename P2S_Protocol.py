def parse_request(str):
	cmd = ""
	hdrs = {}

	req_arr = str.strip().split("\r\n")	# clean up string and get lines

	cmd = req_arr[0].split(" ")			# parse the Command

	for l in req_arr[1:]:				# parse headers
		hdr = l.strip().split(" ")
		hdrs[hdr[0][:-1]] = " ".join(hdr[1:])
					# ^-- remove the ":" at the end of each header_name

	return (cmd, hdrs)

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