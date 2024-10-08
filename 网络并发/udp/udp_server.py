from socket import *

ADDR = ('127.0.0.1', 8888)

sockfd = socket(AF_INET, SOCK_DGRAM)
sockfd.bind(ADDR)

while True:
    data, addr = sockfd.recvfrom(1024)
    print('收到消息:', data.decode())
    sockfd.sendto(b'Thanks', addr)

sockfd.close()
