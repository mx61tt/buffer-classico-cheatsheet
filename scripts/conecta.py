#!/usr/bin/python
import socket

IP="10.0.2.13"
PORTA=3636

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((IP,PORTA))

print r.recv(1024)

r.close()
