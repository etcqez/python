# 孤儿进程: 父进程先于子进程退出, 此时子进程成为孤儿进程
#          孤儿进程会被系统进程收养, 成为孤儿进程的父进程, 孤儿进程退出后会自动处理

# 僵尸进程: 子进程先于父进程退出, 父进程又没有处理子进程的退出状态, 此时子进程就会成为僵尸进程
# wait处理僵尸进程
# 因为wait是阻塞的, 会等待子进程结束后执行, 所以不好
import os
import sys

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:
    # 获得当前进程pid
    print('Child PID:', os.getpid())
    sys.exit('子进程退出')
else:
    '''
        os.wait() # 处理僵尸进程
    '''
    pid, status = os.wait()
    print("pid:", pid)
    print('status:', status)
    while True:  # 父进程不退出
        pass
