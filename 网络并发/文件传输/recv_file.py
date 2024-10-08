from socket import *

ADDR = ('127.0.0.1', 8888)

s = socket()
s.bind(ADDR)
s.listen(3)

c, addr = s.accept()
print('Connect from', addr)

# 接收思路: 1. 打开新文件
#          2. recv内容 write文件
f = open('gg.jpg', 'wb')
while True:
    data = c.recv(1024)
    if not data:
        break
    f.write(data)

f.close()
c.close()
s.close()
