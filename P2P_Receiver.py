import socket  # Import Socket Module
import sys  #Import System Parameter
import time  #Import Time Module
import pickle  #Import Object Serialization Module
import random  #Import Random Module
import datetime  #Import date and time module


ack_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 62223  # Reserve a port for your service
ack_socket.bind((host, port))  # Bind to the port


#Calculate the Checksum of the data being received.
def cal_chksm(rcvd_msg):
   chksm = 0;  #Initial value for checksum
   for i in range(0, len(rcvd_msg), 2)
       msg = str(rcvd_msg)
       w = ord(msg[i]) + (ord(msg[i+1]) << 8)  #Return the unicode code point
       chksm = cary_adn(chksm, w)  #Funtion call to add carry
       return (not chksm) & 0xffff  #Returning the value as True or False


#Adding the carry to the checksum if generated.
def cary_adn(n1, n2):
    c = n1 + n2
    return (c & 0xffff) + (c >> 16)  #Returning the value after carry addtion


#Getting the values from the CLI
def parse_cli_arg():
    prt = sys.argv[1]  #Get the port number for the service
    fl_name = sys.argv[2]  #Get the filename to store the file
    prb = sys.argv[3]  #Define the probability for UDP reliability
    return int(port), fl_name, float(prb) #Return the values from CLI


#Sending the Ack to the Sender
def snd_ack(sq_nm):
    rply_msg = [sq_nm, "0000000000000000", "1010101010101010"]  #Reply Message Format
    ack_socket.sendto(pickle.dumps(rply_msg), (hst, prt))  #Send ACK to the Sender as String


#Main Function
def main():
    prt, output_file, prb_ls = parse_cli_arg()  #Function call for the values from the CLI
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #Create a socket object
    hst = socket.gethostname()  #Get local machine name
    s.bind((hst, prt))  #Bind the port
    tmstr = time.strftime("%Y%m%d-%H%M%S")  #Importing a time stamp
    lst_sq_nm = []  #Define an Array for lost srquence numbers
    prnt_msg = []  #Define an Array for Printing message
    pkt_lst = False  #Variable for defining lost packet
    exp_sq_nm = 0  #Variable for expected sequence number
    while True:
        data, addr = s.recvfrom(1000000)  #Get the Buffered data as a string and address of the socket sending data
        data = pickle.loads(data)  #Read pickled object from the string of data
        sq_nm, chksm, data_type, rcvd_msg = data[0], data[1], data[2], data[3]  #Define the parameters from the pickled object
        rnd_lst = random.random() #Return a number from 0.0 to 1.0 to implement the probability function
        if rnd_lst <= prb_ls  #Check the random number with the probability from the CLI
            print("Lost packet with sequence number = ", sq_nm)
            pkt_lst = True
            if len(lst_sq_nm) == 0:
                lst_sq_nm.append(sq_nm)  #Append the sequence number
            if len(lst_sq_nm) > 0:
                if sq_nm not in lst_sq_nm and (sq_nm>min(lst_sq_nm)):  
                    lst_sq_nm.append(sq_nm)  #Append the sequence number
                else:
                    if chksm != cal_chksm(rcvd_msg):  #Compare the calculated and the received checksum
                        print("Packet being dropped as the checksum doesn't match.")
        else:
            if chksm != cal_chksm(rcvd_msg):  #Compare the calculated and the received checksum
                        print("Packet being dropped as the checksum doesn't match.")
            else:
               if sq_nm == exp_sq_nm:
                   ack_sq = int(sq_nm)+1  #Increment the sequence number
                   snd_ack(ack_sq)  #Function call for sending the acknowledgement
                   prnt_msg.append(sq_num)  #Append the sequence number
                   with open(output_file, 'ab') as file:  #Open the File
                       file.write(msg)  #Write the message on the file
                   exp_sq_nm += 1  #Increment the Expected sequence number


if __name__ == "__main__":
    main()
