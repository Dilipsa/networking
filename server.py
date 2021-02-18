#!/usr/bin/python           # This is server.py file

import socket 
import os              # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '192.168.0.142'
port = 12345                # Reserve a port for your service.
s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print(b'Got connection from', addr)
   msg = c.recv(1024)
   print(msg)
   os.mkdir(msg)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection
