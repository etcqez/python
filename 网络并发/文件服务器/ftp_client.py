"""
    1. 连接服务器
    2. 用类来封装请求
"""
from socket import *
import sys
import time

ADDR = ('127.0.0.1', 8888)


class FTPClient:
    def __init__(self, sockfd):
        self.sockfd = sockfd

    def do_list(self):
        self.sockfd.send(b"L")
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            data = self.sockfd.recv(4096)
            # 服务器用换行拼接
            print(data.decode())
        else:
            print(data)

    def do_quit(self):
        self.sockfd.send(b"Q")
        self.sockfd.close()
        sys.exit('谢谢使用')

    # 下载文件
    def do_get(self, filename):
        self.sockfd.send(('G ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            f = open(filename, 'wb')
            # 循环接收文件
            while True:
                data = self.sockfd.recv(1024)
                # 结束标志
                if data == b"##":
                    break
                f.write(data)
            f.close()
        else:
            print(data)

    # 上传文件
    def do_put(self, filename):
        try:
            f = open(filename, 'rb')
        except Exception:
            print('该文件不存在')
            return
        # 获取文件名
        filename = filename.split('/')[-1]
        self.sockfd.send(('P ' + filename).encode())
        data = self.sockfd.recv(128).decode()
        if data == 'OK':
            while True:
                data = f.read(1024)
                if not data:
                    time.sleep(0.1)
                    self.sockfd.send(b"##")
                    break
                self.sockfd.send(data)
            f.close()
        else:
            print(data)


def main():
    sockfd = socket()
    try:
        sockfd.connect(ADDR)
    except Exception as e:
        print(e)
        return

    ftp = FTPClient(sockfd)

    while True:
        print('\n==========命令==========')
        print('*******     list     *****')
        print('*******   get file   *****')
        print('*******   put file   *****')
        print('*******     quit     *****')
        print('==========================')

        cmd = input('输入命令: ')
        if cmd.strip() == 'list':
            ftp.do_list()
        elif cmd.strip() == 'quit':
            ftp.do_quit()
        # 前三个字母
        elif cmd[:3] == 'get':
            # 取文件名
            filename = cmd.strip().split(' ')[-1]
            ftp.do_get(filename)
        elif cmd[:3] == 'put':
            filename = cmd.strip().split(' ')[-1]
            ftp.do_put(filename)
        else:
            print('请输入正确命令')


if __name__ == "__main__":
    main()
