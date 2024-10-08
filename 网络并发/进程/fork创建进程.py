import os

# 会创建子进程, 当前进程会得到子进程id
# 子进程会复制一份代码, 但不会再次执行fork, 子进程得到0
pid = os.fork()

if pid < 0:
    print("Create process failed")
# 子进程执行的代码
elif pid == 0:
    print('The now process')
# 当前进程执行的代码
else:
    print('The old process')

print('Fork test over')
