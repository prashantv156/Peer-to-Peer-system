"""import socket  # Import Socket Module
import sys  #Import System Parameter
import time  #Import Time Module
import pickle  #Import Object Serialization Module
import random  #Import Random Module
import datetime  #Import date and time module
"""

MSS = 2048 - 8

def rdt_send(s, msg, (peerAddress, peerPort)):

	# split into MSS
	# add headers
	# send chunks till window full
	# wait
	# slide window
	# bad ack/ time out -> resend
	# if all ack return
	s.sendto(msg, (peerAddress, peerPort))

def rdt_recv(s):
	if True:
	# until we fill buffer upto buffSize
		message, peerAddr = s.recvfrom(MSS + 1024)
		#buffer += message
		# drop packets
		# strip headers
		# check cheksum
		# send ACK
	return message, peerAddr
