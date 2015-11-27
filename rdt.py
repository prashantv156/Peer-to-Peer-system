"""import socket  # Import Socket Module
import sys  #Import System Parameter
import time  #Import Time Module
import pickle  #Import Object Serialization Module
import random  #Import Random Module
import datetime  #Import date and time module
"""

MSS = 2048 - 8

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
        print(w)
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
	print(calculate_checksum(msg))

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
