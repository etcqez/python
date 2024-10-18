"""
    EPOLLET 边缘触发
        1. 水平触发: 对于已经就绪IO,未处理会一直提醒
        2. 边缘触发: 下次再有IO就绪一起处理
    # 边缘触发
    ep.register(c, EPOLLIN | EPOLLET)
"""
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
ep = epoll()

# 建立查找字典，通过一个IO的fileno找到IO对象
# fd: socket
fdmap = {s.fileno(): s}

# 关注s的输入和错误, 按位或表示具有属性
ep.register(s, EPOLLIN | EPOLLERR)

# 循环监控IO
while True:
    # 阻塞等待客户端的连接
    events = ep.poll()
    print("你有新的IO需要处理哦!")
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 是否是s
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connetc from', addr)
            # 关注客户端链接套接字
            # ep.register(c, EPOLLIN | EPOLLERR)
            # 边缘触发
            ep.register(c, EPOLLIN | EPOLLET)
            # 将客户端套接字加入字典
            fdmap[c.fileno()] = c
