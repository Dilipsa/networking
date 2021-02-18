#!/usr/bin/python           # This is client.py file

import socket
import os              # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '192.168.0.142'
port = 12345                # Reserve a port for your service.

s.connect((host, port))
print(s.recv(1024))
s.close()                     # Close the socket when done
