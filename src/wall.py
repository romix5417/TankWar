# -*- coding: utf-8 -*-

# !/usr/bin/env python

import pygame

wall_image_path = "../res/wall.png"


class wall(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.wall_image = pygame.image.load(wall_image_path).convert()

    def set_location(self, x, y):
        self.x = x
        self.y = y
