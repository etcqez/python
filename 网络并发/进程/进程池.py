"""
    进程池使用示例
"""
from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(), '--', msg)


# 创建进程池, 默认个数为cpu核心数
pool = Pool()

# 向进程池添加事件
for i in range(10):
    msg = "worker %d" % i
    pool.apply_async(func=worker, args=(msg,))

# 关闭进程池, 不再接受事件
pool.close()
# 回收进程池
pool.join()
