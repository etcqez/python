# 根据生日（年月日），计算活了多少天

import time


def life_days(year, month, day):
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second=time.time() - time.mktime(tuple_time)
    return life_second/60/60//24

print(life_days(1996,10,18))
