class SkillImpactEffect:
    """
    技能影响效果
    """

    def impact(self):
        raise NotImplementedError()


class DamageEffect(SkillImpactEffect):
    """
        伤害生命效果
    """
    def __init__(self, value):
        self.value = value

    def impact(self):
        print("扣你%d" % self.value)

class LowerDefenseEffect(SkillImpactEffect):
    """
        降低防御力
    """
    def __init__(self,value,time):
        self.value = value
        self.time = time

    def impact(self):
        print("降低%d防御力，持续%d秒"%(self.value,self.time))

class DizzineEffect(SkillImpactEffect):
    """
        眩晕
    """
    def __init__(self,time):
        self.time = time

    def impact(self):
        print("眩晕%d秒"%(self.time))

class SkillDeployer:
    """
        技能释放器
    """
    # 生成技能（执行效果）
    def __init__(self,name):
        self.name=name
        # 加载配置文件    {技能名称:[效果1，效果2...],...}
        self.__dict_skill_config=self.__load_config_file()
        # 创建效果对象
        self.__effect_objects=self.__create_effect_objects()

    def __load_config_file(self):
        # 加载文件
        return {
            "降龙十八掌":["DamageEffect(200)","LowerDefenseEffect(-10,5)","DizzineEffect(6)"],
            "六脉神剑":["DamageEffect(100)","DizzineEffect(6)"],
            }

    def __create_effect_objects(self):
        list_effect_name=self.__dict_skill_config[self.name]
        list_effect_object = []
        for item in list_effect_name:
            effect_object=eval(item)
            list_effect_object.append(effect_object)
        return list_effect_object

    def generate_skill(self):
        print(self.name,"技能释放啦")
        for item in self.__effect_objects:
            item.impact()


xlsbz=SkillDeployer("降龙十八掌")
xlsbz.generate_skill()

lmsj=SkillDeployer("六脉神剑")
lmsj.generate_skill()
