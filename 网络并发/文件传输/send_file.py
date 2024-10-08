from socket import *

ADDR = ('127.0.0.1', 8888)

s = socket()
s.connect(ADDR)

f = open('huge.jpeg', 'rb')
while True:
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()
