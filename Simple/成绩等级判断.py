score = int(input('请输入成绩: '))
if score > 100 or score < 0:
    print('输入有误')
elif 90 <= score:
    print('优秀')
elif 80 <= score:
    print('良好')
elif 60 <= score:
    print('及格')
else:
    print('不及格')