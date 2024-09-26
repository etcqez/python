"""
    列表助手模块
"""


class ListHelper:
    """
        列表助手类
    """

    @staticmethod
    def find_all(list_target, func_condition):
        """
            通用的查找某个条件的所有元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件, 函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素, 生成器类型
        """
        for item in list_target:
            if func_condition(item):
                yield item

    @staticmethod
    def find_single(list_target, func_condition):
        """
            通用的查找某个条件的单个元素方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件, 函数类型
                函数名(参数) --> bool
        :return: 需要查找的元素
        """
        for item in list_target:
            if func_condition(item):
                return item

    @staticmethod
    def get_count(list_target, func_condition):
        """
            通用的计算满足某个条件的元素数量的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件, 函数类型
                函数名(参数) --> int
        :return: 满足条件元素的数量
        """
        count_value = 0
        for item in list_target:
            if func_condition(item):
                count_value += 1
                return count_value

    @staticmethod
    def is_exists(list_target, func_condition):
        """
            通用的判断满足某个条件是否存在元素的方法
        :param list_target: 需要查找的列表
        :param func_condition: 需要查找的条件, 函数类型
                函数名(参数) --> bool
        :return: true表示存在, false表示不存在
        """
        for item in list_target:
            if func_condition(item):
                return True
            return False

    @staticmethod
    def sum(list_target, func_handle):
        """
            通用的求和方法
        :param list_target: 需要求和的列表
        :param func_handle: 需要求和的处理逻辑, 函数类型
        :return: 和
        """
        sum_value=0
        for item in list_target:
            sum_value += func_handle()
            return sum_value

    @staticmethod
    def select(list_target, func_handle):
        """
            通用的筛选方法
        :param list_target: 需要筛选的列表
        :param func_handle: 需要筛选的处理逻辑, 函数类型
        :return: 生成器
        """
        for item in list_target:
            yield func_handle(item)

    @staticmethod
    def get_max(list_target, func_handle):
        """
            通用的获取最大元素方法
        :param list_target: 需要搜索的列表
        :param func_handle: 需要搜索的处理逻辑, 函数类型
        :return: 生成器
        """
        max_value=list_target[0]
        for i in range(1,len(list_target)):
            if func_handle(max_value) < func_handle(list_target[i]):
                max_value = list_target[i]
        return  max_value
