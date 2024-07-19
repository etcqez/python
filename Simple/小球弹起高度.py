height = 100
count = 0
# 经过距离
distance = height
while height / 2 > 0.01: 
    count += 1
    # 弹起
    height /= 2
    print('第%d次弹起的高度是%f'%(count, height))
    # 累加起落高度
    distance += height * 2

print('总共弹起%d次'%(count))
print('总共经过的距离是%.2f'%(distance))