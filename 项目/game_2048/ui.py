"""
    2048控制台界面
"""
from bll import GameCoreController
from model import DirectionModel


class GameConsoleView:
    def __init__(self):
        self.__controller = GameCoreController()

    def main(self):
        self.__start()

    def __start(self):
        # 产生两个数字
        self.__controller.generate_new_number()
        self.__controller.generate_new_number()
        # 绘制界面
        self.__draw_map()

    def __draw_map(self):
        for line in self.__controller.map:
            for item in line:
                print(item, end=" ")
            print()

    def __update(self):
        # 判断玩家输入, 移动地图
        self.__move_map_for_input()
        # 产生新数字
        self.__controller.generate_new_number()
        # 绘制界面
        self.__draw_map()
        # 判断结束
        self.__controller.is_game_over()


    def __move_map_for_input(self):
        dir = input("请输入方向wasd")
        # if dir == "w":
        #     self.__controller.move(DirectionModel.UP)
        # elif dir == "s":
        #     self.__controller.move(DirectionModel.DOWN)
        # elif dir == "a":
        #     self.__controller.move(DirectionModel.LEFT)
        # elif dir == "d":
        #     self.__controller.move(DirectionModel.RIGHT)
        dict_dir = {
            "w": DirectionModel.UP,
            "s": DirectionModel.DOWN,
            "a": DirectionModel.LEFT,
            "d": DirectionModel.RIGHT
        }
        if dir in dict_dir:
            self.__controller.move(dict_dir[dir])


if __name__ == '__main__':
    view = GameConsoleView()
    view.main()
