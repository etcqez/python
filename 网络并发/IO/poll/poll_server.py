"""
    linux, mac
    poll() --> (fd, event)
    fdmap (通过fd找socket) 格式: fd: socket
    PULLIN: 输入
"""
from socket import *
from select import *

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

# 创建poll对象
p = poll()

# 建立查找字典，通过一个IO的fileno找到IO对象
# fd: socket
fdmap = {s.fileno(): s}

# 关注s的输入和错误, 按位或表示具有属性
p.register(s, POLLIN | POLLERR)

# 循环监控IO
while True:
    # 阻塞等待客户端的连接
    events = p.poll()
    # 循环遍历列表，查看哪个IO就绪，进行处理
    for fd, event in events:
        # 是否是s
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print('Connetc from', addr)
            # 关注客户端链接套接字
            p.register(c, POLLIN | POLLERR)
            # 将客户端套接字加入字典
            fdmap[c.fileno()] = c
        # 收发消息, 按位与判断是否是POLLIN
        elif event & POLLIN:
            data = fdmap[fd].recv(1024).decode()
            if not data:
                p.unregister(fd)
                fdmap[fd].close()
                del fdmap[fd]
                continue
            print(data)
            fdmap[fd].send(b'OK')
