"""import socket  # Import Socket Module
import sys  #Import System Parameter
import time  #Import Time Module
import pickle  #Import Object Serialization Module
import random  #Import Random Module
import datetime  #Import date and time module
"""

MSS = 2048 - 8

DATA_TYPE = 0b0101010101010101

data_pkt = namedtuple('data_pkt', 'seq_num checksum data_type data')
ack_pkt = namedtuple('ack_pkt', 'seq_num zero_field data_type')
seq_num = 0

def pack_data(message, seq_num):
    # pkt = data_pkt(seq_num, calculate_checksum(message), DATA_TYPE, message)
    # print(message, seq_num)
    # print(calculate_checksum(message))
    pkt = data_pkt(seq_num, calculate_checksum(message), DATA_TYPE, message)
    # print(pkt)
    # packed_pkt = pack('ihh' + str(DATA_SIZE) + 's', pkt.seq_num, pkt.checksum, pkt.data_type, bytes(pkt.data,'utf-8'))
    my_list = [pkt.seq_num, pkt.checksum, pkt.data_type, pkt.data]
    packed_pkt = pickle.dumps(my_list)
    return packed_pkt


"""def prepare_pkts(file_content, seq_num):
    pkts_to_send = []
    seq_num = 0
    #print(file_content)
    for item in file_content:  # Every MSS bytes should be packaged into segment Foo
        # print(item)
        # print(pkts_to_send)
        pkts_to_send.append(pack_data(item, seq_num))
        seq_num += 1
        # print(seq_num)
        # print(pkts_to_send)
    return pkts_to_send
"""

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



def rdt_send(s, msg, (peerAddress, peerPort)):

	# split into MSS
	# add headers
	# send chunks till window full
	# wait
	# slide window
	# bad ack/ time out -> resend
	# if all ack return
	s.sendto(msg, (peerAddress, peerPort))
	print msg, (calculate_checksum(msg))

def rdt_recv(s):
	if True:
	# until we fill buffer upto buffSize
		message, peerAddr = s.recvfrom(MSS + 8)
		#buffer += message
		# drop packets
		# strip headers
		# check cheksum
		# send ACK
	return message, peerAddr
