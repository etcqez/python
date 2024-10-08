import time


def print_execute_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execute_time = time.time() - start_time
        print("执行时间是: ", execute_time)
        return result
    return wrapper


@print_execute_time
def fun01():
    time.sleep(2)
    print("fun01执行完成了")


@print_execute_time
def fun02(a):
    time.sleep(1)
    print("fun02执行完成了, 参数是: ", a)


fun01()
fun02(100)
