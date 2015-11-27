"""import socket  # Import Socket Module
import sys  #Import System Parameter
import time  #Import Time Module
import pickle  #Import Object Serialization Module
import random  #Import Random Module
import datetime  #Import date and time module
"""

from collections import namedtuple
import pickle
import math

MSS = 64-8	#2048 - 8

DATA_TYPE = 0b0101010101010101

data_pkt = namedtuple('data_pkt', 'seq_num checksum data_type data')
seq_num = 0

#
# Add headers and pickle
#
def pack_data(message, sno):
    pkt = data_pkt(sno, calculate_checksum(message), DATA_TYPE, message)
    my_list = [pkt.seq_num, pkt.checksum, pkt.data_type, pkt.data]
    packed_pkt = pickle.dumps(my_list)
    return packed_pkt



#
# Check-Sum Calculation
#
def carry_checksum_addition(num_1, num_2):
    c = num_1 + num_2
    return (c & 0xffff) + (c >> 16)

# Calculate the checksum of the data only. Return True or False
def calculate_checksum(message):
    # print (message)
    if (len(message) % 2) != 0:
        message += bytes("0")

    checksum = 0
    for i in range(0, len(message), 2):
        my_message = str(message)
        # print(my_message[i], ord(my_message[i]))
        w = ord(my_message[i]) + (ord(my_message[i + 1]) << 8)
        # print(w)
        checksum = carry_checksum_addition(checksum, w)
    checksum = bin(checksum ^ 0xffff)
    return checksum



#send_buff = []
#send_buff_ln = 0
def rdt_send(s, msg, (peerAddress, peerPort)):
	#send_buff.append(msg)
	#send_buff_ln += len(msg)

	#if send_buff_ln < MSS:
		#pass
		# add 1 sec timer			#TODO
		#return


	# if larger, split into MSS sized segments
	segs = []
	for i in range(int(math.ceil(1.0*len(msg)/MSS))):
		segs.append(pack_data(msg[i*MSS:(i+1)*MSS], i))

	# add padding


	# send chunks till window full
	# wait
	# slide window
	# bad ack/ time out -> resend
	# if all ack return

	# add headers
	#out = pack_data(msg,seq_num)

	#s.sendto(out, (peerAddress, peerPort))

	print "sending out ", len(segs)," number of segs" 
	for seg in segs:
		s.sendto(seg, (peerAddress, peerPort))

def rdt_recv(s):
	if True:
	# until we fill buffer upto buffSize

		print "rdt_recv"
		# Strip apart the headers and Data
		message, peerAddr = s.recvfrom(MSS + 8 + 128)	# 128 added since pickling is failing without extra space
														# TODO - Fix!!
		(sq_nm, chksm, data_type, rcvd_msg) = pickle.loads(message)  #Read pickled object from the string of data
		#print "RECV"
        #print sq_nm, chksm, data_type, rcvd_msg

		#buffer += message
		# drop packets
		# strip headers
		# check cheksum
		# send ACK

	return rcvd_msg, peerAddr
