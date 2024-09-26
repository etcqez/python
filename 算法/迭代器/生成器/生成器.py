# 让自定义类使用for
class Skill:
    pass


class SkillManager:
    def __init__(self):
        self.__skills = []

    def add_skill(self, skill):
        self.__skills.append(skill)

    def __iter__(self):
        for item in self.__skills:
            yield item


manager = SkillManager()
manager.add_skill(Skill)
manager.add_skill(Skill)
manager.add_skill(Skill)

for item in manager:
    print(item)

i = manager.__iter__()
while True:
    try:
        item=i.__next__()
        print(item)
    except StopIteration:
        break
