list01 = [8, 9, 13, 15]
# 倒着删
for i in range(len(list01) - 1, -1, -1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01)
