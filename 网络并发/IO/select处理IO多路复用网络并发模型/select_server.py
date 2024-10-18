"""
    linux, windows, mac
    只能监控1024个IO
    rs: 被动接收
    rs: 主动输入
"""
from socket import *
from select import select

s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('0.0.0.0', 8888))
s.listen(3)

rlist = [s]
wlist = []
xlist = []

# 循环监控IO
while True:
    rs, ws, xs = select(rlist, wlist, xlist)

    for r in rs:
        if r is s:
            c, addr = r.accept()
            print("Connect from", addr)
            rlist.append(c)
        else:
            # 有客户端发消息
            data = r.recv(1024).decode()
            # 客户端退出
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            wlist.append(r)

    for w in ws:
        w.send(b"OK")
        # 每次处理完毕, 删除w
        wlist.remove(w)

    for x in xs:
        pass
