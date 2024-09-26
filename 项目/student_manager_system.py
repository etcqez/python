"""
    学生管理系统
        项目计划:
            1. 完成数据模型类StudentModel
            2. 创建逻辑控制类StudentManagerControl
"""


class StudentModel:
    def __init__(self, name="", age=0, score=0, id=0):
        self.name = name
        self.age = age
        self.score = score
        self.id = id


class StudentManagerController:
    """
        学生模型
    """
    init_id = 1000

    def __init__(self):
        self.__stu_list = []

    @property
    def stu_list(self):
        return self.__stu_list

    def add_student(self, stu_info):
        stu_info.id = self.__generate_id()
        self.__stu_list.append(stu_info)

    def __generate_id(self):
        StudentManagerController.init_id += 1
        return StudentManagerController.init_id

    def remove_student(self, id):
        for item in self.__stu_list:
            if item.id == id:
                self.__stu_list.remove(item)
                return True
        return False

    def update_student(self, stu_info):
        for item in self.__stu_list:
            if item.id == stu_info.id:
                item.name = stu_info.name
                item.age = stu_info.age
                item.score = stu_info.score
                return True
        return False

    def order_by_score(self):
        """
            根据成绩对self.__stu_list进行升序排列
        :return:
        """
        # self.__stu_list
        for r in range(len(self.__stu_list) - 1):
            for c in range(r + 1, len(self.__stu_list)):
                if self.__stu_list[r].score > self.__stu_list[c].score:
                    self.__stu_list[r], self.__stu_list[c] = self.__stu_list[c], self.__stu_list[r]


# # 测试删除学生
# manager = StudentManagerController()
# s01 = StudentModel("zs", 24, 100)
# s02 = StudentModel("ls", 25, 100)
# manager.add_student(s01)
# manager.add_student(s02)
# for item in manager.stu_list:
#     print(item.id, item.name)
# print(manager.remove_student(1002))
# print(manager.remove_student(1005))
# for item in manager.stu_list:
#     print(item.id, item.name)

# # 测试修改学生
# manager = StudentManagerController()
# s01 = StudentModel("zs", 24, 100)
# s02 = StudentModel("ls", 25, 100)
# manager.add_student(s01)
# manager.add_student(s02)
# for item in manager.stu_list:
#         print(item.id, item.name, item.age, item.score)
# manager.update_student(StudentModel("张三",30,50,1001))
# for item in manager.stu_list:
#     print(item.id, item.name, item.age, item.score)

class StudentManagerView:
    """
        学生管理器视图
    """

    def __init__(self):
        self.__manager = StudentManagerController()

    def __display_menu(self):
        print("1)添加学生")
        print("2)显示学生")
        print("3)删除学生")
        print("4)修改学生")
        print("5)按照成绩升序显示学生")

    def __select_menu(self):
        item = input("请输入:")
        if item == "1":
            self.__input_students()
        if item == "2":
            self.__output_students(self.__manager.stu_list)
        if item == "3":
            self.__delete_student()
        if item == "4":
            self.__modify_student()
        if item == "5":
            self.__output_student_by_score()

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __input_number(self, msg):
        while True:
            try:
                num = int(input(msg))
                return num
            except:
                print("输入有误，请重新输入")

    def __input_students(self):
        name = input("请输入学生姓名：")
        age = self.__input_number("请输入学生年龄：")
        score = self.__input_number("请输入学生成绩：")
        stu = StudentModel(name, age, score)
        self.__manager.add_student(stu)

    def __output_students(self, list_output):
        for item in list_output:
            print(item.id, item.name, item.age, item.score)

    def __delete_student(self):
        id = self.__input_number("请输入编号：")
        if self.__manager.remove_student(id):
            print("删除成功")
        else:
            print("删除失败")

    def __modify_student(self):
        stu = StudentModel()
        # stu.id = int(input("请输入需要修改的学生编号："))
        stu.id = self.__input_number("请输入需要修改的学生编号：")
        stu.name = input("请输入新的学生姓名：")
        stu.age = self.__input_number("请输入新的学生年龄：")
        stu.score = self.__input_number("请输入新的学生成绩：")
        if self.__manager.update_student(stu):
            print("修改成功")
        else:
            print("修改失败")

    def __output_student_by_score(self):
        self.__manager.order_by_score()
        self.__output_students(self.__manager.stu_list)


view = StudentManagerView()
view.main()
