from socket import *
import os, sys

ADDR = ('0.0.0.0', 8888)

# 存储用户 {name: address}
user = {}


# 登录
def do_login(s, name, address):
    if name in user or '管理员' in name:
        s.sendto('该用户存在'.encode(), address)
        return
    s.sendto(b'OK', address)  # 可以进入聊天室
    # 通知其他人
    msg = '欢迎"%s"进入聊天室' % name
    for i in user:
        s.sendto(msg.encode(), user[i])
    # 存储用户
    user[name] = address


# 聊天
def do_chat(s, name, text):
    msg = '%s: %s' % (name, text)
    for i in user:
        if i != name:
            # 排除本人, 发送给其他人
            s.sendto(msg.encode(), user[i])


# 退出
def do_quit(s, name):
    msg = '\n%s 退出聊天室' % name
    for i in user:
        if i != name:
            s.sendto(msg.encode(), user[i])
        else:
            s.sendto(b'EXIT', user[i])
    del user[name]


# 处理请求
def do_request(s):
    while True:
        data, addr = s.recvfrom(1024)
        tmp = data.decode().split(' ')
        # 根据不同的请求类型具体执行不同的事情
        # L 进入     C 聊天  Q 退出
        if tmp[0] == 'L':
            do_login(s, tmp[1], addr)
        elif tmp[0] == 'C':
            text = ' '.join(tmp[2:])
            do_chat(s, tmp[1], text)
        elif tmp[0] == 'Q':
            do_quit(s, tmp[1])


# 搭建网络
def main():
    # udp服务端
    s = socket(AF_INET, SOCK_DGRAM)
    s.bind(ADDR)

    pid = os.fork()
    # 管理员消息
    if pid == 0:
        while True:
            msg = input('管理员消息:')
            msg = 'C 管理员 ' + msg
            # 发送到自己的ip, 调用自己的do_request --> do_chat 发送给所有人
            s.sendto(msg.encode(), ADDR)
    else:
        do_request(s)


main()
