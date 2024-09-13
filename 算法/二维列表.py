list01 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

# 打印第三行的每个元素
for item in list01[2]:
    print(item)

for item in range(len(list01[2])):
    print(list01[2][item])

# 打印第一列的每个元素
for item in range(len(list01)):
    print(list01[item][0])

# 矩阵转置
list02 = []
for row in range(len(list01[0])):
    list02.append([])
    for line in range(len(list01)):
        list02[row].append(list01[line][row])

print(list02)
