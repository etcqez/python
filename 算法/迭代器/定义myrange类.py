"""
    定义MyRange类，实现下面功能
        for item in range(10):
        print(item)
"""


class MyRange:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __iter__(self):
        return MyRangeIterator(self.stop_value)


class MyRangeIterator:
    def __init__(self, stop_value):
        self.__num = 0
        self.__stop_value = stop_value

    def __next__(self):
        if self.__num == self.__stop_value:
            raise StopIteration
        temp = self.__num
        self.__num += 1
        print(temp)


m = MyRange(10)
i = m.__iter__()
while True:
    try:
        i.__next__()
    except StopIteration:
        break

# for item in MyRange(10):
#     print(item)