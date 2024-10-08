from socket import *
import os
import signal

HOST = '0.0.0.0'
PORT = 8888
ADDR = (HOST, PORT)


# 具体处理客户端请求
def handle(c):
    # 循环接收消息
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print('Listen the port 8888...')

while True:
    try:
        # 循环处理客户端请求
        c, addr = s.accept()
        print('Connect from', addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 循环创建子进程处理客户端事物
    pid = os.fork()
    if pid == 0:
        s.close()  # 子进程不需要s
        handle(c)  # 处理具体事物
        os._exit(0)  # 销毁子进程
    else:
        c.close()  # 父进程不需要和客户端通信
