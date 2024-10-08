import socket

# 创建tcp套接字
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址
sockfd.bind(('127.0.0.1', 8888))

# 设置监听
sockfd.listen(5)

# 阻塞等待处理连接
print('Waiting for connect...')
connfd, addr = sockfd.accept()
print('Connect from', addr)

# 收发消息
data = connfd.recv(1024)
print('收到:', data.decode())
n = connfd.send(b'Thanks')
print('发送%d字节' % n)

# 关闭套接字
connfd.close()
sockfd.close()
