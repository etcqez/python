def my_enmerate(iterable_target):
    index = 0
    for item in iterable_target:
        yield index, item
        index += 1


list01 = [3, 5, 7, 11, 19]
for index, element in my_enmerate(list01):
    print(index, element)


# 自定义my_zip
list02=["孙悟空","猪八戒","唐僧","沙僧"]
list03=[101,102,103,104]
# for item in zip(list02,list03):
#     print(item)
# ('孙悟空', 101)
# ('猪八戒', 102)
# ('唐僧', 103)
# ('沙僧', 104)

def my_zip(*args):
    for i in range(len(args[0])):
        list_result=[]
        for item in args:
            list_result.append(item[i])
        yield tuple(list_result)

for item in my_zip(list02,list03):
    print(item)