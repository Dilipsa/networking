#!/usr/bin/python           # This is server.py file

import socket 
import os    
import sqlite3   
conn = sqlite3.connect('new.db')
cur = conn.cursor()
print('connection')
	
try:
	cur.execute('create table ip_data (id integer primary key autoincrement ,ip varchar(100), data varchar(200))')
	pass
except:
	print("table alreay created")       # Import socket module

s = socket.socket()         # Create a socket object
# host = socket.gethostname() # Get local machine name
host = '192.168.0.142'
port = 12345               # Reserve a port for your service.
# s.bind((host, port))        # Bind to the port
s.listen(5)  
print('host is lisening at ', host , port)               # Now wait for client connection.
while True:
   c, addr = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   print(addr)
   msg = c.recv(1024)
   print(msg)
   if msg == b'decrpyt':
   		cur.execute('select data from ip_data where ip = "{}"'.format(addr[0]))
   		print(cur.fetchall())
   else:
   		cur.execute('insert into ip_data (ip,data) values ("{}","{}")'.format(addr[0],msg))
   		conn.commit()
   #os.mkdir(msg)
   c.send(b'Thank you for connecting')
   c.close()                # Close the connection
