import socket
import sys
from xmlrpc.client import _HostType

# create a socket (connect two computers)
def create_socket():
   try:
       global host
       global port
       global sock

       host = "" # static ip address in the server that is cloud 
       port = 9999
       sock = socket.socket()
   except socket.error as msg:

        print("socket creation error " + str(msg))

# Binding the socket and listening for connection
def bind_socket():
    try:
        global host
        global port
        global sock

        print("binding the port" + str(port))

        sock.bind((host,port)) # using tuple () 
        sock.listen(5) # 5 is number attempt it try to listen too  
    except socket.error as msg:
        print("Socket Binding error " + str(msg) + "\n" + "Retrying...")
        bind_socket() #Recurring function calling the function inside the function itself

# Establish connection with a client and the (socket must be listening)

def socket_accept():
    conn,address = sock.accept()
    print("connection has been establish :"+ " IP" + address[0] + " | Port" + str(address[1]))
    send_command(conn)
    conn.close()







