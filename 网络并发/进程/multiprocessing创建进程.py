"""
    此创建的进程不能接收标准输入
"""
from multiprocessing import Process
from time import sleep


def m01():
    sleep(3)
    print("写代码")


p = Process(target=m01)

p.daemon = True  # 父进程退出, 子进程也退出
p.start()
print("Name:", p.name)  # 进程名称
print("PID:", p.pid)  # 对应子进程PID
print("is alive:", p.is_alive())  # 是否在生命周期
sleep(2)
print("吃饭")
# p.join()
