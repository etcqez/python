"""
    2 0 4 8     游戏核心算法
"""
list_merge = [4, 4, 0, 2]


# 1. 零元素移至末尾
# [0,2,0,2] --> [2,2,0,0]
def zero_to_end():
    # 从后往前，如果发现零元素，删除并追加
    for i in range(-1, -len(list_merge) - 1, -1):
        if list_merge[i] == 0:
            del list_merge[i]
            list_merge.append(0)


# zero_to_end()
# print(list_merge)


# 2. 将相同数字合并
# [0,2,0,2] --> [4,0,0,0]
def merge():
    zero_to_end()
    for i in range(len(list_merge) - 1):
        if list_merge[i] == list_merge[i + 1]:
            # 将后一个累加前一个之上
            list_merge[i] += list_merge[i + 1]
            del list_merge[i + 1]
            list_merge.append(0)


# merge()
# print(list_merge)

# 3. 地图向左移动
map = [
    [2, 2, 0, 2],
    [2, 4, 0, 2],
    [2, 2, 4, 2],
    [4, 2, 4, 2],
]


def move_left():
    for line in map:
        global list_merge
        list_merge = line
        merge()


# move_left()
# print(map)

def move_right():
    for line in map:
        global list_merge
        # 从右向左取出数据 形成新列表
        list_merge = line[::-1]
        merge()
        # 从右向左接受 合并的后的数据
        line[::-1] = list_merge


# move_right()
# print(map)

# 4. 向上移动 向下移动
# 利用方阵转置函数
def square_matrix_transpose(sqr_matrix):
    for c in range(0, len(sqr_matrix) - 1):
        for r in range(c + 1, len(sqr_matrix)):
            sqr_matrix[r][c], sqr_matrix[c][r] = sqr_matrix[c][r], sqr_matrix[r][c]


def move_up():
    square_matrix_transpose(map)
    move_left()
    square_matrix_transpose(map)


# move_up()
# print(map)

def move_down():
    square_matrix_transpose(map)
    move_right()
    square_matrix_transpose(map)


move_down()
print(map)
