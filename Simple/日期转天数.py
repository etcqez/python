day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input('请输入月份: '))
day = int(input('请输入日: '))
total_day = 0
for i in range(month - 1):
        total_day += day_of_month[i]
total_day += day
print('是这年的第%d天' % total_day)
# total_day = sum(day_of_month[:month - 1])