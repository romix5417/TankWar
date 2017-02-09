# -*- coding: utf-8 -*-

from windows import *
from tank import *


def game_init():
    pass


def start():
    Windows = windows(background_image_name)
    # Wall = wall()
    # Wall.set_location(24, 24)
    # Wall_1 = wall()
    # Wall_1.set_location(40, 24)
    # Wall_2 = wall()
    # Wall_2.set_location(24, 40)
    # Wall_3 = wall()
    # Wall_3.set_location(40, 40)

    playerTank = Tank('humen', 0, 0)

    # Windows.add_surface(Wall.wall_image, Wall.x, Wall.y)
    # Windows.add_surface(Wall_1.wall_image, Wall_1.x, Wall_1.y)
    # Windows.add_surface(Wall_2.wall_image, Wall_2.x, Wall_2.y)
    # Windows.add_surface(Wall_3.wall_image, Wall_3.x, Wall_3.y)
    Windows.add_player(playerTank)

    Windows.run()


if __name__ == "__main__":
    start()
