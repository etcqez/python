"""
    静态方法

    总结：
        实例方法： 操作对象的变量
        类方法： 操作类的变量
        静态方法: 即不需要操作实例变量，也不需要操作类变量
"""
list01 = [
    ["00", "01", "02", "03"],
    ["10", "11", "12", "13"],
    ["20", "21", "22", "23"],
]


class Vector2:
    """
        二维向量
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def left():
        return Vector2(0, -1)

    @staticmethod
    def right():
        return Vector2(0, 1)

    @staticmethod
    def up():
        return Vector2(-1, 0)

    @staticmethod
    def down():
        return Vector2(1, 0)


pos01 = Vector2(1, 2)
l01 = Vector2.left()
pos01.x += l01.x
pos01.y += l01.y
# print(pos01.x, pos01.y)


# 在二维列表中获取指定位置，指定方向，指定数量的元素
# 例如： list01 "10" 右边 3
class DoubleListHelper:

    @staticmethod
    def get_elements(target, vect_pos, vect_dir, count):
        list_result = []
        for i in range(count):
            vect_pos.x += vect_dir.x
            vect_pos.y += vect_dir.y
            element = target[vect_pos.x][vect_pos.y]
            list_result.append(element)
        return list_result


re = DoubleListHelper.get_elements(list01, Vector2(2, 1), Vector2.right(), 2)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(2, 1), Vector2.up(), 2)
print(re)
re = DoubleListHelper.get_elements(list01, Vector2(0, 3), Vector2.down(), 2)
print(re)
