class Skill:
    pass


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        """
        创建一个迭代器对象
        :return:
        """
        return SkillManagerIterator(self.__skills)


class SkillManagerIterator:
    def __init__(self, target):
        self.__target = target
        self.__index = 0

    def __next__(self):
        if self.__index > len(self.__target) - 1:
            raise StopIteration
        temp = self.__target[self.__index]
        self.__index += 1
        return temp


manager = SkillManager()
manager.add_skill(Skill)
manager.add_skill(Skill)
manager.add_skill(Skill)

for item in manager:
    print(item)

i = manager.__iter__()
while True:
    try:
        item = i.__next__()
        print(item)
    except StopIteration:
        break
