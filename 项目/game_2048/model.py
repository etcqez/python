class DirectionModel:
    """
        方向数据
    """
    # 在整数基础上, 添加一个人容易识别的"标签"
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

class Location:
    """
        位置
    """
    def __init__(self,r,c):
        self.r_index = r
        self.c_index = c
