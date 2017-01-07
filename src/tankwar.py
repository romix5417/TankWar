# -*- coding: utf-8 -*-

from pygame import *
from ai import *
from windows import *

background_image_name = '../res/background.png'

class tank():
    def __init__(self, tankType):
        pass


def game_init():
    pass


def start():
    Windows = windows(background_image_name)

    Windows.run()

if __name__ == "__main__":
    start()
